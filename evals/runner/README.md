# `iamhumans` eval runner

## What this is

A script that turns the 100 use cases into a structured runbook, drives an opencode session to (a) invoke the `iamhumans` skill on each case input and (b) invoke an Oracle subagent to judge each response against the case's rubric, then aggregates the per-case scores into a report.

## What this is not

A standalone test runner. The Oracle judge is an opencode subagent — not callable from a plain Python script over HTTP. The runner produces a **runbook** that an opencode-driven session executes; the session writes responses and judge verdicts back into `evals/runs/<ts>/`, and the runner aggregates them.

## Two invocation modes

### `--dry-run`

Loads all cases, validates the schema, prints a summary. Does *not* invoke the skill or the judge. Used by `scripts/eval-smoke.sh` as the validation lane in CI.

```bash
python3 evals/runner/run.py --dry-run
python3 evals/runner/run.py --dry-run --limit 5
```

### Full run

Emits a runbook JSON to `evals/runs/<ts>/runbook.json` and a per-case packet under `evals/runs/<ts>/cases/<id>/`. Each packet contains the prompt the skill should be asked, and the prompt the Oracle judge should be asked once a response exists.

```bash
python3 evals/runner/run.py --batch quick     # 5 cases, smoke
python3 evals/runner/run.py --batch main      # 90 main-pool cases
python3 evals/runner/run.py --full            # 100 cases incl. holdout
```

After emitting, the runner *prints* the opencode invocation commands the operator (or wrapping skill) should execute to fill in responses and judgments. Once all responses and judgments exist in the run directory, run:

```bash
python3 evals/runner/run.py --aggregate evals/runs/<ts>/
```

…which produces `report.md` and `report.json`.

## Why this two-phase shape

Three reasons.

1. **Honesty about the medium.** The judge is an LLM. Invoking it requires running an LLM. The runner does not pretend to be self-contained — it is explicit about needing an opencode harness around it.
2. **Reproducibility.** The runbook captures the exact prompts at a given commit hash. Re-running with the same runbook on the same skill version should produce equivalent results modulo LLM stochasticity.
3. **Auditability.** Per-case packets are inspectable. A maintainer can read `cases/TC-007/response.md` and `cases/TC-007/judge.md` and see exactly what happened.

## Files

- `run.py` — the orchestrator
- `schema.py` — case parsing and validation
- `judge_prompt.md` — the prompt template for the Oracle judge
- `aggregate.py` — score aggregation (imported by `run.py --aggregate`)

## When you've changed the skill, what to re-run

- Edited `SKILL.md` or a dimension card → re-run `main` and compare against the previous aggregate. Any regression on a previously-passing case is a lesson-worthy event (write a `lessons/<batch-id>.md`).
- Edited a single case's rubric → re-run that case only (`--limit 1 --case <id>`).
- Added a new case → run it once and confirm pass before considering it part of the main pool.
- *Never* edit holdout cases between PR #9 and PR #11. The holdout is locked.
