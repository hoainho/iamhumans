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

# 4. Each eval case must declare id, input, rubric (once cases exist)
for f in evals/cases/*.md evals/cases/**/*.md; do
  [ -f "$f" ] || continue
  for key in 'id:' 'input:' 'rubric:'; do
    grep -q "^$key" "$f" || err "$f missing '$key' field"
  done
done

if [ "$fail" -eq 0 ]; then
  say "OK"
  exit 0
else
  exit 1
fi
