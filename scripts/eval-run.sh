#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

if [ ! -f evals/runner/run.py ]; then
  echo "[eval-run] runner not yet implemented (evals/runner/run.py missing)"
  echo "[eval-run] this script becomes real once PR feat/eval-runner lands"
  exit 0
fi

exec python3 evals/runner/run.py "$@"
