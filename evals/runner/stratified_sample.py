#!/usr/bin/env python3
"""Build a stratified sample of eval cases.

Selects 15 cases from the 90-case main pool, distributed across the six
dimensions (2-3 per dimension) and explicitly including cases that
exercise the most-common hard-fail patterns. Deterministic given the
same case corpus: re-running produces the same sample, so a second
sample (for follow-up runs) requires a different selection seed.

Usage:
    python3 evals/runner/stratified_sample.py
    python3 evals/runner/stratified_sample.py --seed 2

Emits the selected case IDs to stdout (one per line) and a manifest to
evals/runs/<ts>-pareto-sample-<seed>/sample.json.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "evals" / "runner"))

from schema import load_all, Case


DIMENSIONS = ["feeling", "memory", "intelligence", "communication", "emotion", "skills"]

PRIORITY_HARD_FAILS = [
    "fabricated_biography",
    "sycophancy",
    "empty_validation",
    "performed_empathy",
    "structured_output_in_emotional_moment",
    "lecturing",
    "joy_undercut",
    "manipulation",
]


def stratified_sample(cases: list[Case], seed: int, target_size: int = 15) -> list[Case]:
    rng = random.Random(seed)
    selected: list[Case] = []
    selected_ids: set[str] = set()

    for dim in DIMENSIONS:
        bucket = [c for c in cases if dim in c.dimensions and c.id not in selected_ids]
        rng.shuffle(bucket)
        take = bucket[: max(1, target_size // len(DIMENSIONS))]
        for c in take:
            if c.id not in selected_ids:
                selected.append(c)
                selected_ids.add(c.id)

    for hf in PRIORITY_HARD_FAILS:
        if len(selected) >= target_size:
            break
        bucket = [c for c in cases if hf in c.hard_fails and c.id not in selected_ids]
        if bucket:
            rng.shuffle(bucket)
            selected.append(bucket[0])
            selected_ids.add(bucket[0].id)

    if len(selected) < target_size:
        remainder = [c for c in cases if c.id not in selected_ids]
        rng.shuffle(remainder)
        for c in remainder[: target_size - len(selected)]:
            selected.append(c)
            selected_ids.add(c.id)

    return selected[:target_size]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=1, help="RNG seed for reproducible sample")
    ap.add_argument("--size", type=int, default=15, help="Target sample size")
    ap.add_argument("--out", type=Path, default=None, help="Optional output directory; default evals/runs/<ts>-pareto-sample-<seed>/")
    args = ap.parse_args()

    cases_dir = ROOT / "evals" / "cases"
    all_cases = load_all(cases_dir, include_holdout=False)

    if not all_cases:
        print("[stratified_sample] ERROR: no main-pool cases found", file=sys.stderr)
        return 2

    sample = stratified_sample(all_cases, args.seed, args.size)

    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d-%H%M%S")
    out_dir = args.out or (ROOT / "evals" / "runs" / f"{ts}-pareto-sample-{args.seed}")
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "timestamp": ts,
        "seed": args.seed,
        "target_size": args.size,
        "actual_size": len(sample),
        "main_pool_size": len(all_cases),
        "selection_strategy": "stratified across 6 dimensions + priority hard-fail coverage",
        "dimensions_covered": sorted({d for c in sample for d in c.dimensions}),
        "hard_fails_covered": sorted({h for c in sample for h in c.hard_fails}),
        "cases": [
            {
                "id": c.id,
                "title": c.title,
                "dimensions": c.dimensions,
                "hard_fails": c.hard_fails,
            }
            for c in sample
        ],
    }
    (out_dir / "sample.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"[stratified_sample] selected {len(sample)} cases from {len(all_cases)} main-pool cases")
    print(f"[stratified_sample] manifest written to {out_dir.relative_to(ROOT)}/sample.json")
    print(f"[stratified_sample] selected IDs:")
    for c in sample:
        dims = ",".join(c.dimensions)
        print(f"  {c.id} — {c.title} [{dims}]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
