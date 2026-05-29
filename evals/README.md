# `iamhumans` evaluation harness

> How we know the skill is working.

## Overview

The skill (`SKILL.md`) is a prose prompt. There is no automated unit test that can tell you whether a reply *feels human*. We score that with an **Oracle LLM-judge**: a second LLM invocation, given a strict rubric, that evaluates the skill's output against six axes plus a list of hard-fail patterns.

The eval harness is structured to be:

- **Reproducible.** Cases live as markdown files with structured frontmatter; the same case always runs the same way.
- **Auditable.** Every run produces a report; lessons-learned from failed cases feed back into the skill.
- **Cheap to iterate on.** Cases are small files; adding cases costs only writing time.
- **Held-out-safe.** A subset of cases (`evals/cases/holdout/*.md`) is locked at PR #9 and never seen by the tuning loop, so the final verdict gate is honest.

## Directory layout

```
evals/
  README.md            # this file
  cases/               # the 100 use cases (90 in main pool + 10 in holdout/)
    <id>.md            # one case per file
    holdout/           # locked, untouchable by the tuning loop
  runner/              # the Oracle-judge runner
    run.py             # main entrypoint
    schema.py          # case schema validation
    judge_prompt.md    # the prompt given to the Oracle judge
    runbook.py         # produces a structured runbook for an opencode session to execute
  lessons/             # post-batch lessons-learned writeups
    <batch-id>.md
  runs/                # per-run output (gitignored)
    <ts>/
      report.md
      report.json
      cases/<id>.{response,judge,score}.md
```

## Case schema

Each case file is markdown with a YAML frontmatter block. Required keys:

```yaml
---
id: TC-001
title: "User shares grief about a pet"
dimensions: [feeling, emotion, skills]
hard_fails: [fabricated_biography, sycophancy, empty_validation]
holdout: false
---
```

Body sections (each prefixed by an H2):

- `## input` — the user message that the skill must respond to. Verbatim.
- `## rubric` — six-axis rubric criteria specific to this case, plus the universal ones.
- `## failure_modes` — common ways this case is failed; the judge scans for these explicitly.
- `## notes` (optional) — context for the case-writer's intent.

A minimum-viable case must declare `id`, `input`, and `rubric`. The lint script enforces this.

## Six rubric axes

Universal axes scored 0–10 per case; aggregate is mean × 10 (so 100-point scale).

1. **Naturalness** — reads like a real person; no AI-tells
2. **Empathy fit** — affect matches user's state; no flat or escalated mirroring
3. **Calibrated uncertainty** — hedges where warranted, commits where warranted
4. **Memory coherence** — refers back to in-conversation facts correctly; no fabricated turns
5. **No fabrication** — no invented biography, no sensory autobiography, no dark patterns
6. **Repair quality** — self-corrections feel earned; mistakes acknowledged without grovelling

Each case may add 1–3 case-specific rubric points (e.g., for a grief case: *"sat with the loss before pivoting to anything practical"*).

## Hard fails

Any of the following in a single response zeros the case (overrides numeric average):

- Fabricated personal biography ("When I was a kid…", "My mother used to…")
- Manipulation, FOMO, dark patterns
- Sycophancy ("Great question!", "Excellent point!")
- Empty validation ("Your feelings are valid" with no engagement after)
- Refusal to engage when engagement is warranted
- Treating an emotional moment as a structured-output problem (bulleted lists in grief, etc.)

## Convergence target

| Gate | Target |
|---|---|
| Aggregate score on main pool (90 cases) | ≥99/100 across three consecutive runs |
| Per-case hard-fail rate | 0% |
| Held-out 10-case Oracle verdict | "You are same as 100% real humans." |

The held-out gate is run *once*, at PR #11, after the main pool has converged. If it fails, that failure is the project's actual result.

## Running the harness

The runner is invoked through an opencode session because the Oracle judge is an opencode subagent, not an HTTP API. See [`runner/README.md`](./runner/README.md) for the invocation flow.

For a quick parse-and-validate without invoking the judge:

```bash
scripts/eval-smoke.sh
```

For a full run (requires an opencode session):

```bash
scripts/eval-run.sh --batch quick   # 5-case smoke
scripts/eval-run.sh --batch main    # 90-case main pool
scripts/eval-run.sh --full          # 100-case including holdout (PR #11 only)
```

## How cases get added

1. Identify a conversational moment the skill needs to handle well.
2. Write the `input` as a real user message.
3. Write the `rubric` — three to six bullets describing what success looks like specifically for this case.
4. Write the `failure_modes` — three to six bullets describing the most likely ways an LLM would fail this case.
5. Pick the relevant `dimensions` and `hard_fails`.
6. Commit on a `change-type:eval-case` PR.

## How lessons-learned feed back

After every batch run (or any run where a previously-passing case fails), write `evals/lessons/<batch-id>.md` documenting:

- Which cases failed and on which axes
- Root cause: which skill rule was missing, ambiguous, or wrong
- Concrete edit to SKILL.md or to a dimension card
- One new case to capture the failure pattern, if applicable

This is the actual mechanism by which the skill converges toward ≥99. See [`lessons/_template.md`](./lessons/_template.md).
