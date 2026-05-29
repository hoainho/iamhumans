# Lessons learned — `<batch-id>`

> Written after a batch run where one or more cases failed (or where a previously-passing case regressed). Each entry feeds back into SKILL.md / dimension cards / new eval cases.

## Run summary

- **Run directory:** `evals/runs/<ts>/`
- **Aggregate score:** `<N>/100`
- **Cases failed:** `<N>` of `<total>`
- **Hard-fail cases:** `<list of case IDs>`
- **Regressions vs. last run:** `<list>` (cases that previously passed and now don't)

## Per-failure analysis

For each failed case:

### `<TC-XXX>` — `<short title>`

- **What the case asked for:** one-sentence summary of the rubric intent.
- **What the skill produced:** one paragraph, or a quote.
- **Failure mode:** which of the case's `failure_modes`, or which hard-fail pattern, or which axis fell below threshold.
- **Root cause:** which line/rule in `SKILL.md` or a dimension card was missing, ambiguous, or wrong. Specific file:line.
- **Fix:** the concrete edit being made.
- **New case (optional):** if this failure suggests a pattern not yet covered, the new case ID and short description.

## Pattern across failures

If two or more failures share a root cause, name the pattern here:

- **Pattern:** _e.g., "skill defaults to bulleted advice in grief contexts even after acknowledging"_
- **Affected cases:** _e.g., TC-007, TC-019, TC-024_
- **Skill-level fix:** _the SKILL.md edit that addresses the pattern, not just the individual cases._

## What converged

If this batch's aggregate improved over the previous run, name what worked:

- _e.g., "the new `## Anti-AI tells` table caught TC-003 and TC-011 that previously failed on `naturalness`."_

## Next-batch focus

What to watch for in the next run:

- _Cases at risk of regression._
- _Dimensions where the aggregate is lowest._
- _Hard fails that nearly fired but stayed under the line._

## Sign-off

- Run completed: `<date>`
- Skill version: `<commit hash>`
- Reviewer: `<name or 'self'>`
