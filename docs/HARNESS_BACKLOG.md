# Harness Backlog

<!-- generated-by: harness-init v0.1.0 -->

Use this file when an agent discovers a missing harness capability but should
not change the operating model immediately.

## Template

```md
## Missing Harness Capability

### Title

Short name.

### Discovered While

Task or story that exposed the gap.

### Current Pain

What was hard, repeated, ambiguous, or unsafe?

### Suggested Improvement

What should be added or changed?

### Risk

Tiny, normal, or high-risk.

### Status

proposed | accepted | implemented | rejected
```

## Items

## Missing Harness Capability

### Title

Regression test as an explicit step after PR-comment fixes.

### Discovered While

PR #20 (v1.1.0 Pareto tuning). Reviewer asked: how do we know a fix for a
PR comment doesn't break the cases that were already PASSing? The existing
PR + Bot Review Loop said "re-run validate + user-flow test" — that's
per-fix scope, not regression scope.

### Current Pain

The harness defined a Validation Ladder (lint, integration, e2e, release)
but had no explicit regression layer. After a PR-comment fix, agents would
re-run validate, see green, and push — with no requirement to re-run the
previously-failing case OR spot-check the previously-passing ones. A fix
that secretly broke a passing case could merge undetected.

### Suggested Improvement

Three coordinated edits to docs/HARNESS.md:

1. **Validation Ladder**: add `test:regression` as a named layer with a
   concrete command sequence (lint + smoke + aggregate + targeted re-run +
   spot-check) and a required column in the lane table.
2. **PR + Bot Review Loop**: insert the regression step into the diagram
   between "re-run Review Gate" and "wait for bot re-review", and require
   that regression output is pasted into the PR thread before re-review.
3. **Forbidden Practices**: add items 11 + 12 forbidding push without
   regression evidence and forbidding merge on green CI alone when a PR
   comment has been addressed.

### Risk

Normal. Process change. No code execution surface affected. Affects every
future PR-comment cycle from v1.1.0 onward.

### Status

implemented (in this PR — same commit as this backlog entry).
