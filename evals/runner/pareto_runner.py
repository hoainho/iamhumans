#!/usr/bin/env python3
"""Pareto-sample driver: emit packets for a list of case IDs.

Unlike run.py's --batch quick/main, this runner takes an explicit sample
manifest (built by stratified_sample.py) and emits the per-case packets
that an opencode session will fill in with skill responses and oracle
judgments.

Usage:
    python3 evals/runner/pareto_runner.py emit <sample-dir>
        # Reads sample.json from <sample-dir>, creates cases/<id>/ packets
        # with input.md, rubric.md, judge_template.md

    python3 evals/runner/pareto_runner.py aggregate <sample-dir>
        # After response.md and judge.yaml are filled in for each case,
        # produces report.md and report.json.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "evals" / "runner"))

from schema import parse_case
from run import _build_judge_packet, _parse_judge_yaml


def cmd_emit(args: argparse.Namespace) -> int:
    sample_dir = Path(args.sample_dir).resolve()
    sample_json = sample_dir / "sample.json"
    if not sample_json.exists():
        print(f"[pareto] ERROR: {sample_json} does not exist", file=sys.stderr)
        return 2

    manifest = json.loads(sample_json.read_text(encoding="utf-8"))
    case_ids = [c["id"] for c in manifest["cases"]]

    cases_dir = sample_dir / "cases"
    cases_dir.mkdir(exist_ok=True)

    for cid in case_ids:
        src = ROOT / "evals" / "cases" / f"{cid}.md"
        if not src.exists():
            print(f"[pareto] WARNING: {src.relative_to(ROOT)} not found, skipping", file=sys.stderr)
            continue
        case = parse_case(src)
        case_pkt = cases_dir / cid
        case_pkt.mkdir(exist_ok=True)
        (case_pkt / "input.md").write_text(case.input + "\n", encoding="utf-8")
        (case_pkt / "rubric.md").write_text(
            "\n".join(f"- {r}" for r in case.rubric) + "\n", encoding="utf-8"
        )
        judge_packet = _build_judge_packet(case, "<<<RESPONSE_GOES_HERE>>>")
        (case_pkt / "judge_template.md").write_text(judge_packet, encoding="utf-8")

    print(f"[pareto emit] wrote {len(case_ids)} case packets under {cases_dir.relative_to(ROOT)}/")
    print(f"[pareto emit] next steps for the operator:")
    print(f"  1. For each case, ask iamhumans-loaded subagent to respond to")
    print(f"     cases/<id>/input.md → write reply to cases/<id>/response.md")
    print(f"  2. Re-run `emit` to re-build judge_template.md with responses substituted,")
    print(f"     OR substitute response into judge_template.md directly.")
    print(f"  3. Ask a fresh oracle subagent to evaluate using judge_template.md")
    print(f"     → write YAML output to cases/<id>/judge.yaml")
    print(f"  4. `python3 evals/runner/pareto_runner.py aggregate {sample_dir.relative_to(ROOT)}`")
    return 0


def cmd_aggregate(args: argparse.Namespace) -> int:
    sample_dir = Path(args.sample_dir).resolve()
    cases_dir = sample_dir / "cases"
    if not cases_dir.exists():
        print(f"[pareto aggregate] ERROR: {cases_dir} does not exist", file=sys.stderr)
        return 2

    results: list[dict] = []
    missing: list[str] = []
    for case_pkt in sorted(cases_dir.iterdir()):
        if not case_pkt.is_dir():
            continue
        judge_path = case_pkt / "judge.yaml"
        if not judge_path.exists():
            missing.append(case_pkt.name)
            continue
        parsed = _parse_judge_yaml(judge_path.read_text(encoding="utf-8"))
        parsed.setdefault("case_id", case_pkt.name)
        results.append(parsed)

    if missing:
        print(f"[pareto aggregate] WARNING: {len(missing)} cases missing judge.yaml: {missing}")

    if not results:
        print("[pareto aggregate] no results to aggregate")
        return 1

    totals = [r.get("total", 0) for r in results]
    passes = sum(1 for r in results if r.get("verdict") == "PASS")
    hard_failures = sum(1 for r in results if any(r.get("hard_fails", {}).values()))
    aggregate = sum(totals) / len(totals) if totals else 0

    report_lines = [
        f"# Pareto sample run — {sample_dir.name}",
        "",
        f"- **Cases scored:** {len(results)}/{len(results) + len(missing)}",
        f"- **PASS:** {passes}/{len(results)} ({100*passes/len(results):.1f}%)",
        f"- **Hard fails:** {hard_failures}",
        f"- **Aggregate:** {aggregate:.2f}/100",
        "",
        "## Per-case results",
        "",
        "| Case | Total | Verdict | Hard-fail? | Notes |",
        "|---|---|---|---|---|",
    ]
    for r in sorted(results, key=lambda x: x.get("case_id", "")):
        hf = "yes" if any(r.get("hard_fails", {}).values()) else "no"
        cid = r.get("case_id", "?")
        total = r.get("total", 0)
        verdict = r.get("verdict", "?")
        report_lines.append(f"| {cid} | {total} | {verdict} | {hf} | see cases/{cid}/judge.yaml |")

    (sample_dir / "report.md").write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    (sample_dir / "report.json").write_text(
        json.dumps(
            {
                "aggregate": aggregate,
                "passes": passes,
                "fails": len(results) - passes,
                "hard_failures": hard_failures,
                "missing": missing,
                "results": results,
            },
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )

    print(f"[pareto aggregate] {len(results)} cases scored, aggregate {aggregate:.2f}/100, {passes} pass, {hard_failures} hard-fail")
    print(f"[pareto aggregate] report.md + report.json written to {sample_dir.relative_to(ROOT)}/")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="iamhumans Pareto-sample driver")
    sub = ap.add_subparsers(dest="cmd", required=True)

    emit = sub.add_parser("emit", help="emit case packets for a sample")
    emit.add_argument("sample_dir", help="sample directory containing sample.json")

    agg = sub.add_parser("aggregate", help="aggregate filled judgments into report")
    agg.add_argument("sample_dir", help="sample directory containing cases/<id>/judge.yaml")

    args = ap.parse_args()
    if args.cmd == "emit":
        return cmd_emit(args)
    if args.cmd == "aggregate":
        return cmd_aggregate(args)
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
