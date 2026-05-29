#!/usr/bin/env bash
# scripts/eval-smoke.sh — fast smoke check that the eval runner is wired.
# Run by the validate:quick lane in HARNESS.md. Does NOT call the LLM judge.
# Just confirms: runner exists, fixtures resolve, at least one case is parseable.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

if [ ! -f evals/runner/run.py ] && [ ! -f evals/runner/run.sh ]; then
  echo "[eval-smoke] no runner yet (evals/runner/run.{py,sh}) — skipping (pre-runner stage)"
  exit 0
fi

case_count=$(find evals/cases -name '*.md' -not -path '*/holdout/*' 2>/dev/null | wc -l | tr -d ' ')
echo "[eval-smoke] $case_count eval cases discovered"

if [ "$case_count" -eq 0 ]; then
  echo "[eval-smoke] no cases yet — runner exists, fixtures empty (pre-cases stage)"
  exit 0
fi

if [ -f evals/runner/run.py ]; then
  python3 evals/runner/run.py --dry-run --limit 1
else
  bash evals/runner/run.sh --dry-run --limit 1
fi

echo "[eval-smoke] OK"
