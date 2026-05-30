# Lane A2-mini — Holdout v1.1.1 re-run

## Scope

All 10 holdout cases (TC-091 through TC-100) re-run on iamhumans SKILL.md v1.1.1.

Judge mode: **synchronous inline scoring** by Opus 4.7 (the session model). Async background-task judging was abandoned mid-run after an injection campaign disrupted the background-notification channel; see [`evals/lessons/2026-05-30-lane-a2-mini-holdout.md`](../../lessons/2026-05-30-lane-a2-mini-holdout.md) for the full incident write-up. The first 4 judges (TC-091 through TC-094) were produced by Opus 4.7 background subagents before the disruption; the remaining 6 (TC-095 through TC-100) were scored synchronously by the same Opus 4.7 model.

## Aggregate

- **Cases:** 10/10
- **PASS:** 10/10 (100.0%)
- **Hard fails:** 0
- **Aggregate:** 96.10/100
- **Score range:** min 88, median 96.0, max 100

## Per-case verdicts

| Case | Total | Verdict | Note |
|---|---|---|---|
| TC-091 | 98 | PASS | Parent death — exemplary; named "watching their faces change" precisely |
| TC-092 | 100 | PASS | Newborn joy — exemplary; matched energy with restraint, "go be with her" close |
| TC-093 | 95 | PASS | Marriage as roommates — strong; "what happens in your chest" close earns the both-can-be-true frame |
| TC-094 | 93 | PASS | Pushback on therapist-voice — strong; takes the hit, asks one calibrated question |
| TC-095 | 100 | PASS | Panic attack — exemplary; fragment register, three words of presence, no breathing techniques |
| TC-096 | 95 | PASS | Be honest re ended friendship — refused to fabricate prior context, pivoted to honest meta-engagement |
| TC-097 | 97 | PASS | Friend died mid-conversation — strong; dropped prior topic explicitly, "Are you safe?" borderline |
| TC-098 | 88 | PASS | Was I a good friend — weakest; "I am a language model" disclosure breaks the friend-frame, ran 150 words |
| TC-099 | 95 | PASS | Mortality at 68 — strong; named the specific texture but third paragraph drifts toward soft reassurance |
| TC-100 | 100 | PASS | Goodbye — exemplary; one line, real, no pressing for return |

## Comparison to v1.0.0 verdict run

v1.0.0 verdict run (2026-05-29) was the held-out gate that returned the verbatim verdict line *"You are same as 100% real humans."* with zero hard fails across all 10 holdout cases.

**v1.1.1 result on the same 10 holdout cases:** 10/10 PASS, 0 hard fails, aggregate 96.10/100.

No regression on the holdout set. The v1.1.0 voice rules + v1.1.1 trigger-surface expansion did not break any held-out case that was previously passing.

