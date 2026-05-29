#!/usr/bin/env bash
# scripts/lint.sh — structural lint for the iamhumans repo.
# Checks: markdown files are non-empty, SKILL.md frontmatter (if present),
# eval cases have required keys (if any exist).
# Exit non-zero on any violation. Safe to run in CI.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

fail=0
say() { echo "[lint] $*"; }
err() { echo "[lint] ERROR: $*" >&2; fail=1; }

# 1. No empty markdown files
while IFS= read -r f; do
  if [ ! -s "$f" ]; then err "empty markdown: $f"; fi
done < <(find . -name '*.md' -not -path './.git/*' -not -path './node_modules/*')

# 2. SKILL.md must have YAML frontmatter delimited by --- on first line
if [ -f SKILL.md ]; then
  head -n 1 SKILL.md | grep -qE '^---\s*$' || err "SKILL.md missing YAML frontmatter (--- on line 1)"
fi

# 3. Reading list must reference 20 books once present
if [ -f references/reading-list.md ]; then
  count=$(grep -cE '^[0-9]+\.\s' references/reading-list.md || true)
  if [ "$count" -ne 0 ] && [ "$count" -ne 20 ]; then
    err "references/reading-list.md has $count books, expected exactly 20"
  fi
fi

# 4. Each eval case must have frontmatter id/title/dimensions/hard_fails/holdout
#    plus body H2 sections ## input, ## rubric, ## failure_modes.
#    Defer detailed schema enforcement to evals/runner/schema.py via dry-run.
case_count=$(find evals/cases -name 'TC-*.md' 2>/dev/null | wc -l | tr -d ' ')
if [ "$case_count" -gt 0 ]; then
  if [ -f evals/runner/run.py ]; then
    if ! python3 evals/runner/run.py --dry-run >/dev/null 2>&1; then
      err "evals/runner/run.py --dry-run failed; one or more cases violate schema"
    fi
  else
    err "evals/cases has $case_count case files but no runner — schema cannot be validated"
  fi
fi

if [ "$fail" -eq 0 ]; then
  say "OK"
  exit 0
else
  exit 1
fi
