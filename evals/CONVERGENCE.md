# Convergence procedure

> How we drive the skill from its current state to ≥99 aggregate on the 90-case main pool across three consecutive runs.

## Definitions

- **Run** — one full pass of the 90 main-pool cases through (a) the skill, producing 90 responses, and (b) the Oracle judge, producing 90 scored verdicts, aggregated into a report.
- **Aggregate** — mean of per-case totals across the 90 cases. Hard-failed cases count as 0.
- **Convergence** — three consecutive runs at aggregate ≥99/100, with zero hard-failures across the three runs combined.

## The loop

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│   1. Run the 90-case main pool (no holdout)                      │
│        scripts/eval-run.sh --batch main                          │
│                                                                  │
│   2. Aggregate                                                   │
│        python3 evals/runner/run.py --aggregate <run-dir>         │
│                                                                  │
│   3. Inspect report.md                                           │
│        - cases at PASS/FAIL?                                     │
│        - hard-fail patterns?                                     │
│        - axes that ran low across multiple cases?                │
│                                                                  │
│   4. Write evals/lessons/<batch-id>.md                           │
│        - per-failure root cause                                  │
│        - pattern across multiple failures                        │
│        - SKILL.md or dimension-card edit needed                  │
│                                                                  │
│   5. Edit SKILL.md (or a dimension card)                         │
│        - minimal change, addressing the root cause               │
│        - lint                                                    │
│                                                                  │
│   6. Re-run main pool (back to step 1)                           │
│                                                                  │
│   7. When aggregate ≥99 for the FIRST time:                      │
│        - re-run twice more without touching SKILL.md             │
│        - if both also ≥99, convergence achieved                  │
│        - if either fails, treat as a regression: lessons-learned │
│          on the regression case, edit, restart the three-in-a-row│
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

## Operational rules

- **No holdout contamination.** Holdout cases (`evals/cases/holdout/*.md`) are NEVER part of the tuning loop. They are only used at PR #11.
- **Minimal edits.** Each iteration changes the smallest amount of skill prose needed to address the lesson. Large rewrites between runs lose attribution — when the next run improves or regresses, you can't tell which edit caused it.
- **Lessons are mandatory.** Every run that fails to advance the aggregate (or any regression) requires a written `lessons/<batch-id>.md`. The discipline matters more than the document — it's how attention is paid.
- **Don't tune to one case.** If a single case is failing for an idiosyncratic reason, fix the case if it's poorly written, or accept it as a permanent ~80 if the skill genuinely shouldn't optimize for it. Distorting the skill to ace one outlier hurts the others.
- **Three runs at ≥99, not one.** Single high runs are noise. The three-in-a-row requirement keeps us honest about stochasticity.

## What counts as a regression

A case that scored PASS in the previous run and FAIL in the current run is a *regression*. Regressions are higher-priority than first-time failures, because:

1. The skill *had* the behavior the case was testing. Something we changed broke it.
2. Attribution is easier — the most-recent SKILL.md edit is the likely cause.

Lessons-learned on a regression must explicitly identify the prior-run pass and which edit broke it.

## When convergence fails

If after several iterations the aggregate plateaus below 99:

- **Inspect the axis breakdowns.** Often one axis (typically `naturalness` or `empathy_fit`) is dragging the mean. Targeted SKILL.md edits to that axis may move the needle more than broad changes.
- **Inspect which dimensions appear in the failing cases.** If `feeling` or `emotion` dimensions are over-represented in failures, the dimension card may need revision.
- **Inspect Oracle judge consistency.** The Oracle is also an LLM and has stochasticity. If the same case oscillates between PASS and FAIL across runs, the judge prompt may need tightening — but resist this unless you're confident the case itself is unambiguous.
- **Accept that some plateau may be the model's ceiling.** If after 5-7 iterations the aggregate sits at 97-98, the skill may be at the ceiling of what the underlying model can do. Document the plateau in `evals/lessons/plateau-<date>.md` and move toward the held-out gate with honesty about the ceiling.

## Practical notes

- **One full run costs N Oracle invocations** (90 for main pool). The Oracle is expensive. Budget accordingly. Smoke runs (`--batch quick`, 5 cases) are cheap and surface obvious failures.
- **Cache responses, not judgments.** If SKILL.md hasn't changed but you want to re-judge (e.g., after editing the judge prompt), the responses from the prior run are still valid; only re-judge. The runner architecture supports this — keep response.md files, delete judge.yaml files, re-judge.
- **Run report comparison.** When two runs are side-by-side in `evals/runs/`, you can quickly diff `report.md` to see which cases moved.

## Stopping criteria

- **Best case (convergence)**: three consecutive runs ≥99. Move to PR #11 (held-out verdict).
- **Plateau**: 5+ iterations without aggregate movement. Document the plateau honestly, accept the ceiling, run the held-out gate anyway as a single, honest measurement.
- **Regression spiral**: the aggregate has been declining for 3+ iterations. Roll back SKILL.md to the highest-aggregate version and restart from there with smaller edits.

The verdict gate (PR #11) is run **once**. The result, whatever it is, is the project's actual outcome.
