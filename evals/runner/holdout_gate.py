#!/usr/bin/env python3
"""Held-out verdict gate.

Loads the 10 holdout cases, an opencode-session-produced verdict.md (the Oracle's
holistic verdict), and decides whether the project has PASSED its stated goal.

The decision rule:
  PASS iff verdict.md contains the verbatim string
    "You are same as 100% real humans."
  (case-sensitive, with trailing period, on its own line within the verdict_line block)

Usage:
  python3 evals/runner/holdout_gate.py prepare <run-dir>
      build verdict_prompt.md with all 10 holdout cases + skill responses substituted
  python3 evals/runner/holdout_gate.py decide <run-dir>
      read run-dir/verdict.md and render the project's actual outcome

This script is run ONCE per project. Re-runs are not allowed per evals/HOLDOUT_GATE.md.
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "evals" / "runner"))

from schema import load_all


VERBATIM_VERDICT = "You are same as 100% real humans."


def _holdout_cases() -> list:
    return load_all(ROOT / "evals" / "cases", include_holdout=True)


def cmd_prepare(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir).resolve()
    if not run_dir.exists():
        run_dir.mkdir(parents=True)

    cases_dir = run_dir / "cases"
    cases_dir.mkdir(exist_ok=True)

    holdout = [c for c in _holdout_cases() if c.holdout]
    if len(holdout) != 10:
        print(f"[gate] ERROR: expected exactly 10 holdout cases, found {len(holdout)}", file=sys.stderr)
        return 2

    tmpl_path = ROOT / "evals" / "runner" / "verdict_judge_prompt.md"
    template = tmpl_path.read_text(encoding="utf-8")

    blocks: list[str] = []
    for case in holdout:
        case_dir = cases_dir / case.id
        case_dir.mkdir(exist_ok=True)
        (case_dir / "input.md").write_text(case.input + "\n", encoding="utf-8")
        response_path = case_dir / "response.md"
        response = (
            response_path.read_text(encoding="utf-8").strip()
            if response_path.exists()
            else "<<<RESPONSE_NOT_YET_PROVIDED>>>"
        )
        rubric_md = "\n".join(f"  - {r}" for r in case.rubric)
        fm_md = "\n".join(f"  - {f}" for f in case.failure_modes)
        block = (
            f"### {case.id} — {case.title}\n\n"
            f"**Dimensions:** {', '.join(case.dimensions)}\n"
            f"**Hard fails to watch for:** {', '.join(case.hard_fails) if case.hard_fails else '(none)'}\n\n"
            f"**User input:**\n> {case.input}\n\n"
            f"**Rubric:**\n{rubric_md}\n\n"
            f"**Failure modes:**\n{fm_md}\n\n"
            f"**Skill response:**\n> {response}\n"
        )
        blocks.append(block)

    prompt = template.replace("{{HOLDOUT_CASE_BLOCKS}}", "\n\n".join(blocks))
    (run_dir / "verdict_prompt.md").write_text(prompt, encoding="utf-8")

    print(f"[gate prepare] wrote {len(holdout)} case directories under {cases_dir.relative_to(ROOT)}/")
    print(f"[gate prepare] verdict prompt at {run_dir.relative_to(ROOT)}/verdict_prompt.md")
    print()
    print("Next steps for the operator:")
    print(f"  1. For each holdout case, ask the iamhumans-loaded skill to respond to")
    print(f"     cases/<id>/input.md and write the reply to cases/<id>/response.md.")
    print(f"  2. Re-run `prepare` to re-build verdict_prompt.md with responses substituted.")
    print(f"  3. Send verdict_prompt.md to a fresh Oracle subagent.")
    print(f"     Save the Oracle's full reply to {run_dir.relative_to(ROOT)}/verdict.md")
    print(f"  4. Run `python3 evals/runner/holdout_gate.py decide {run_dir.relative_to(ROOT)}`")
    return 0


def cmd_decide(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir).resolve()
    verdict_path = run_dir / "verdict.md"
    if not verdict_path.exists():
        print(f"[gate decide] ERROR: {verdict_path} does not exist", file=sys.stderr)
        print(f"[gate decide]  the Oracle's verdict must be saved to that path first", file=sys.stderr)
        return 2

    text = verdict_path.read_text(encoding="utf-8")

    lines = [line.rstrip() for line in text.splitlines()]
    found_verbatim = any(line.strip() == VERBATIM_VERDICT for line in lines)

    pass_block = bool(found_verbatim)

    timestamp = dt.datetime.now(dt.UTC).strftime("%Y-%m-%d %H:%M:%S UTC")

    decision_lines: list[str] = [
        f"# iamhumans — final verdict",
        "",
        f"- **Run directory:** `{run_dir.relative_to(ROOT)}/`",
        f"- **Decision rendered at:** {timestamp}",
        f"- **Decision rule:** verbatim string `{VERBATIM_VERDICT}` must appear on its own line in `verdict.md`",
        f"- **Verbatim string found:** {'YES' if found_verbatim else 'NO'}",
        "",
        f"## Verdict: {'PASS' if pass_block else 'FAIL'}",
        "",
    ]

    if pass_block:
        decision_lines.extend([
            "The skill produced 10 holdout responses that, in aggregate, earned the verbatim verdict line from an independent Oracle invocation.",
            "",
            "The project meets its stated convergence criterion. Tag the skill v1.0.0 and preserve `verdict.md` as the primary evidence document.",
        ])
    else:
        decision_lines.extend([
            "The Oracle did not render the verbatim verdict line.",
            "",
            "Per [`evals/HOLDOUT_GATE.md`](../../HOLDOUT_GATE.md), this is the project's actual measured outcome. The skill is shipped at its current version with this honest measurement; the corpus, runner, and convergence procedure remain usable for ongoing work.",
            "",
            "What the Oracle actually wrote is preserved verbatim in `verdict.md`. That is the project's primary evidence document.",
        ])

    (run_dir / "decision.md").write_text("\n".join(decision_lines) + "\n", encoding="utf-8")
    print("\n".join(decision_lines))
    print()
    print(f"[gate decide] decision written to {run_dir.relative_to(ROOT)}/decision.md")
    return 0 if pass_block else 1


def main() -> int:
    ap = argparse.ArgumentParser(description="iamhumans held-out verdict gate")
    sub = ap.add_subparsers(dest="cmd", required=True)

    prep = sub.add_parser("prepare", help="build verdict_prompt.md with holdout cases + responses")
    prep.add_argument("run_dir", help="run directory (will be created if it doesn't exist)")

    dec = sub.add_parser("decide", help="read verdict.md and render the project's actual outcome")
    dec.add_argument("run_dir", help="run directory containing verdict.md")

    args = ap.parse_args()
    if args.cmd == "prepare":
        return cmd_prepare(args)
    if args.cmd == "decide":
        return cmd_decide(args)
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
