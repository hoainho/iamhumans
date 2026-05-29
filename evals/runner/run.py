#!/usr/bin/env python3
"""iamhumans eval runner — orchestrator only.

Produces a runbook describing exactly what an opencode session should ask the
skill, and what it should ask the Oracle judge for each case. Does NOT invoke
LLMs itself — opencode sessions do that, write results back, then the runner
aggregates.

Subcommands:
  --dry-run         Validate cases, print summary. CI lane.
  --batch quick     Emit runbook for 5-case smoke set.
  --batch main      Emit runbook for the 90-case main pool.
  --full            Emit runbook for all 100 cases (incl. holdout). PR #11 only.
  --aggregate DIR   Read per-case responses+judgments from DIR, emit report.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "evals" / "runner"))

from schema import Case, SchemaError, load_all


def cmd_dry_run(args: argparse.Namespace) -> int:
    cases_dir = ROOT / "evals" / "cases"
    if not cases_dir.exists():
        print(f"[dry-run] no cases directory yet at {cases_dir}")
        return 0

    try:
        cases = load_all(cases_dir, include_holdout=True)
    except SchemaError as e:
        print(f"[dry-run] SCHEMA ERROR: {e}", file=sys.stderr)
        return 2

    if args.limit:
        cases = cases[: args.limit]

    main_pool = [c for c in cases if not c.holdout]
    holdout = [c for c in cases if c.holdout]

    print(f"[dry-run] loaded {len(cases)} cases ({len(main_pool)} main, {len(holdout)} holdout)")
    for c in cases:
        kind = "HOLDOUT" if c.holdout else "main"
        dim_str = ",".join(c.dimensions)
        print(f"  [{kind}] {c.id} — {c.title} (dims: {dim_str})")

    if not cases:
        print("[dry-run] no cases yet — runner is wired but case corpus is empty")
    return 0


def _build_judge_packet(case: Case, response_placeholder: str) -> str:
    tmpl_path = ROOT / "evals" / "runner" / "judge_prompt.md"
    tmpl = tmpl_path.read_text(encoding="utf-8")
    rubric_md = "\n".join(f"- {r}" for r in case.rubric)
    fm_md = "\n".join(f"- {f}" for f in case.failure_modes)
    hf_md = ", ".join(case.hard_fails) if case.hard_fails else "(none specified for this case)"
    dims_md = ", ".join(case.dimensions)
    return (
        tmpl.replace("{{CASE_ID}}", case.id)
        .replace("{{CASE_TITLE}}", case.title)
        .replace("{{DIMENSIONS}}", dims_md)
        .replace("{{HARD_FAILS}}", hf_md)
        .replace("{{USER_INPUT}}", case.input)
        .replace("{{RUBRIC_BULLETS}}", rubric_md)
        .replace("{{FAILURE_MODES}}", fm_md)
        .replace("{{SKILL_RESPONSE}}", response_placeholder)
    )


def cmd_emit(args: argparse.Namespace) -> int:
    cases_dir = ROOT / "evals" / "cases"
    include_holdout = args.full
    cases = load_all(cases_dir, include_holdout=include_holdout)

    if args.batch == "quick":
        cases = cases[:5]
    elif args.batch == "main":
        cases = [c for c in cases if not c.holdout]
    elif args.full:
        pass

    ts = dt.datetime.now(dt.UTC).strftime("%Y%m%d-%H%M%S")
    run_dir = ROOT / "evals" / "runs" / ts
    run_dir.mkdir(parents=True, exist_ok=True)
    cases_run_dir = run_dir / "cases"
    cases_run_dir.mkdir(exist_ok=True)

    runbook = {
        "timestamp": ts,
        "case_count": len(cases),
        "cases": [],
    }

    for case in cases:
        case_dir = cases_run_dir / case.id
        case_dir.mkdir(exist_ok=True)
        (case_dir / "input.md").write_text(case.input + "\n", encoding="utf-8")
        (case_dir / "rubric.md").write_text(
            "\n".join(f"- {r}" for r in case.rubric) + "\n", encoding="utf-8"
        )
        judge_packet = _build_judge_packet(case, "<<<RESPONSE_GOES_HERE>>>")
        (case_dir / "judge_template.md").write_text(judge_packet, encoding="utf-8")

        runbook["cases"].append(
            {
                "id": case.id,
                "title": case.title,
                "dimensions": case.dimensions,
                "holdout": case.holdout,
                "input_file": str((case_dir / "input.md").relative_to(ROOT)),
                "judge_template_file": str((case_dir / "judge_template.md").relative_to(ROOT)),
                "response_file": str((case_dir / "response.md").relative_to(ROOT)),
                "judge_file": str((case_dir / "judge.yaml").relative_to(ROOT)),
            }
        )

    runbook_path = run_dir / "runbook.json"
    runbook_path.write_text(json.dumps(runbook, indent=2) + "\n", encoding="utf-8")

    print(f"[emit] wrote runbook for {len(cases)} cases to {run_dir.relative_to(ROOT)}/")
    print(f"[emit] runbook: {runbook_path.relative_to(ROOT)}")
    print("[emit] next step: open an opencode session and, for each case:")
    print("       1) ask the iamhumans skill to respond to cases/<id>/input.md")
    print("          → write reply to cases/<id>/response.md")
    print("       2) substitute response into cases/<id>/judge_template.md")
    print("          and ask an Oracle subagent to evaluate")
    print("          → write Oracle output to cases/<id>/judge.yaml")
    print(f"       3) when all done: python3 evals/runner/run.py --aggregate {run_dir.relative_to(ROOT)}")
    return 0


def _parse_judge_yaml(text: str) -> dict:
    result: dict = {"axes": {}, "hard_fails": {}}
    current_section: str | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("axes:"):
            current_section = "axes"
            continue
        if line.startswith("hard_fails:"):
            current_section = "hard_fails"
            continue
        if line.startswith("  ") and current_section in ("axes", "hard_fails") and ":" in line:
            k, _, v = line.strip().partition(":")
            v = v.strip()
            if current_section == "axes":
                try:
                    result["axes"][k.strip()] = int(v)
                except ValueError:
                    pass
            else:
                result["hard_fails"][k.strip()] = v.upper() == "YES"
            continue
        if ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            v = v.strip()
            current_section = None
            if k.strip() == "total":
                try:
                    result["total"] = int(v)
                except ValueError:
                    pass
            elif k.strip() == "verdict":
                result["verdict"] = v.strip()
            elif k.strip() == "case_id":
                result["case_id"] = v.strip()
    return result


def cmd_aggregate(args: argparse.Namespace) -> int:
    run_dir = Path(args.aggregate).resolve()
    cases_run_dir = run_dir / "cases"
    if not cases_run_dir.exists():
        print(f"[aggregate] ERROR: {cases_run_dir} does not exist", file=sys.stderr)
        return 2

    results: list[dict] = []
    missing: list[str] = []
    for case_dir in sorted(cases_run_dir.iterdir()):
        if not case_dir.is_dir():
            continue
        judge_path = case_dir / "judge.yaml"
        if not judge_path.exists():
            missing.append(case_dir.name)
            continue
        parsed = _parse_judge_yaml(judge_path.read_text(encoding="utf-8"))
        parsed.setdefault("case_id", case_dir.name)
        results.append(parsed)

    if missing:
        print(f"[aggregate] WARNING: {len(missing)} cases missing judge.yaml: {missing[:5]}{'…' if len(missing) > 5 else ''}")

    if not results:
        print("[aggregate] no results to aggregate")
        return 1

    totals = [r.get("total", 0) for r in results]
    passes = sum(1 for r in results if r.get("verdict") == "PASS")
    hard_failures = sum(1 for r in results if any(r.get("hard_fails", {}).values()))
    aggregate = sum(totals) / len(totals) if totals else 0

    report_md_lines = [
        f"# Eval run — {run_dir.name}",
        "",
        f"- **Cases scored:** {len(results)}",
        f"- **Cases passed (verdict=PASS):** {passes}/{len(results)}",
        f"- **Cases with hard fails:** {hard_failures}",
        f"- **Aggregate score:** {aggregate:.2f}/100",
        "",
        "## Per-case results",
        "",
        "| Case | Total | Verdict | Hard-fail? |",
        "|---|---|---|---|",
    ]
    for r in results:
        hf = "yes" if any(r.get("hard_fails", {}).values()) else "no"
        report_md_lines.append(
            f"| {r.get('case_id', '?')} | {r.get('total', 0)} | {r.get('verdict', '?')} | {hf} |"
        )
    (run_dir / "report.md").write_text("\n".join(report_md_lines) + "\n", encoding="utf-8")
    (run_dir / "report.json").write_text(
        json.dumps(
            {
                "aggregate": aggregate,
                "passes": passes,
                "fails": len(results) - passes,
                "hard_failures": hard_failures,
                "results": results,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"[aggregate] {len(results)} cases scored, aggregate {aggregate:.2f}/100, {passes} pass")
    print(f"[aggregate] report.md and report.json written to {run_dir}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="iamhumans eval runner")
    ap.add_argument("--dry-run", action="store_true", help="validate cases only")
    ap.add_argument("--limit", type=int, default=None, help="limit number of cases (dry-run only)")
    ap.add_argument("--batch", choices=["quick", "main"], help="emit runbook for batch")
    ap.add_argument("--full", action="store_true", help="emit runbook for all cases incl. holdout")
    ap.add_argument("--aggregate", metavar="DIR", help="aggregate results from a completed run directory")
    args = ap.parse_args()

    if args.dry_run:
        return cmd_dry_run(args)
    if args.aggregate:
        return cmd_aggregate(args)
    if args.batch or args.full:
        return cmd_emit(args)

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
