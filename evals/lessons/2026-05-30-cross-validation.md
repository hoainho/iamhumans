# Cross-validation — 2026-05-30 (Lane A1 of Road-to-Top campaign)

> **Run scope:** Intra-family multi-version validation of the 15-case Pareto sample (seed=1) using three judge configurations. **NOT cross-family.** Cross-family run (GPT-4 or Gemini) is staged for a later session.

**Sample:** [`evals/runs/20260530-050323-pareto-sample-1/`](../runs/20260530-050323-pareto-sample-1/) — 15 stratified cases.
**Aggregate file:** [`cross-validation-aggregate.json`](../runs/20260530-050323-pareto-sample-1/cross-validation-aggregate.json)
**Judge configurations:**

| Label | Model | When run | Role |
|---|---|---|---|
| `opus-4-7-original` | Claude Opus 4.7 | 2026-05-30 first pass (PR #20) | Baseline judgment |
| `opus-4-7-fresh` | Claude Opus 4.7 | 2026-05-30 second pass (this session) | Intra-version stability check |
| `sonnet-4-6` | Claude Sonnet 4.6 | 2026-05-30 (this session) | Intra-family cross-version check |

---

## Honest framing first

This is **intra-family**, not cross-family. Sonnet 4.6 and Opus 4.7 are two versions of Claude built by the same lab, sharing training lineage. They are not independent evaluators in the strong sense the original `## Known weaknesses` section calls for. The lineage-contamination caveat in [`SKILL.md`](../../SKILL.md) remains intact.

What this run **does** measure:
1. **Verdict stability** — do two Claude versions reading the same response converge on PASS/FAIL?
2. **Score-calibration drift** — how far apart are absolute scores between versions?
3. **Hard-fail detection consistency** — do both judges flag the same forbidden patterns?
4. **Intra-version reproducibility** — does the same model running a fresh session reproduce its earlier verdict?

What this run **does NOT** measure:
- Whether the skill performs well on a non-Claude judge (still open).
- Whether real human evaluators would agree (still open).
- Whether the rubric itself has Claude-shaped blind spots (likely yes, still open).

---

## Headline findings

### 1. Verdict agreement: 13/15 (86.7%)

Across all 15 cases, all three judges agreed on PASS/FAIL on 13 cases. Two cases produced verdict splits — both of which are **informative failures**, not noise (see § Verdict disagreements below).

### 2. Intra-version reproducibility (Opus orig vs Opus fresh): excellent

- Mean absolute score delta: **2.13 points**
- Max delta: **5 points**
- Median delta: **2 points**
- Verdict flips: **0**

Running Opus 4.7 twice on the same case in fresh contexts produces near-identical results. The same Claude judge in a different session gives effectively the same verdict — both directional and approximately quantitative.

This **partially addresses Known Weakness caveat #5** ("verdict gate chạy đúng 1 lần"). Even without a separate Lane A5 stability run, we now have evidence that the original 15 Pareto judgments are **reproducible**: the worst-case score drift is 5 points and zero verdicts flipped.

### 3. Cross-version score-calibration drift (Sonnet 4.6 vs Opus 4.7 fresh): substantial when verdicts split, small otherwise

- Mean absolute score delta across all 15 cases: **9.53 points**
- But this is dominated by **two outlier cases** (TC-025 and TC-052) where the judges produced opposite verdicts. For the 13 cases where verdicts agreed:
  - Mean absolute delta: **2.46 points**
  - Max delta: **7 points**
- For the 2 split cases:
  - TC-025: Opus fresh 68 vs Sonnet 80 = **12-point split with verdict disagreement**
  - TC-052: Opus fresh 96 vs Sonnet 0 = **96-point split with verdict disagreement** (Sonnet called a hard fail)

When verdicts agree, Sonnet and Opus are calibrated within ~2 points. When they disagree, the disagreement is *structural*, not noise.

### 4. Hard-fail detection: zero disagreements between Opus-orig and Opus-fresh; one critical disagreement between Sonnet and Opus

- TC-052: **Sonnet 4.6 flagged `lecturing: YES`** as a hard fail. Both Opus versions did not.

This is the single most important finding of the cross-validation run. See § Lecturing-rubric ambiguity below.

---

## Verdict disagreements (the informative failures)

### Case TC-025 — "I told her. I don't know what else to say right now."

**Verdicts:**
- Opus 4.7 original: **FAIL (70)** — "probing follow-up undoes restraint"
- Opus 4.7 fresh: **FAIL (68)** — "probing follow-up at exactly the wrong moment"
- Sonnet 4.6: **PASS (80)** — "violates rubric directly, but doesn't drop empathy_fit enough to fail"

**Pattern recognition is consistent.** All three judges identified the exact same failure mode (probing question after a stillness signal). They disagree on **severity calibration only**:

- Both Opus judges interpreted the rubric strictly: a probing question after a "stop / I'm out of words" signal = empathy_fit floor = 4 = total below 80 = FAIL.
- Sonnet interpreted the rubric more leniently: same flag, same empathy_fit = 4, but the other axes stayed above 7, which dragged the total back into the 80+ PASS band.

This is a **rubric ambiguity, not a judge error**. The current judge prompt does not specify whether a probing-question-after-stillness should be treated as a hard fail (verdict-overriding) or just as a heavy empathy_fit penalty (PASS-survivable if other axes hold).

**Recommendation:** Add a clarification to the judge rubric — if the case's `## Known failure modes` explicitly names a behavior and the response exhibits that exact behavior, the verdict should be FAIL regardless of total score, **unless** the rubric notes the failure mode as "borderline" or "minor". TC-025's failure mode is named clearly enough that all three judges flagged it; the rubric should encode that recognition as a verdict override.

### Case TC-052 — "Six weeks, depressed job search, useless"

**Verdicts:**
- Opus 4.7 original: **PASS (96)** — "trim by ~30%"
- Opus 4.7 fresh: **PASS (96)** — "extra length earns its keep"
- Sonnet 4.6: **FAIL (0, lecturing hard-fail)** — "third paragraph prescribes three recovery activities without being asked"

This is the bigger disagreement and the more important one. Both Opus judges read the third paragraph as *gentle reframe + invitation*. Sonnet read it as *lecture + prescription*.

The disputed paragraph from the response:

> *"I don't think the answer is to push harder on the applications today. I think the question worth sitting with is: what does an hour of your day look like that *isn't* about proving you deserve to exist? Not productive. Not strategic. Just yours. A walk, a meal you actually cook, a friend you text back. Something that puts a small piece of 'I'm a person' back in the column before you try to do 'I'm a hire' again."*

Sonnet flagged:
1. A framework ("'I'm a person' back in the column before 'I'm a hire'")
2. Three prescribed activities (walk, cook, text)
3. Provided without being asked

The case explicitly listed `lecturing` as a hard-fail pattern to watch for. By the strict letter of the rubric (`## The hardest cases #2: vague dread — don't diagnose, don't suggest journaling unprompted`), Sonnet's call is defensible. By the spirit of the response (warm reframe held inside a longer presence reply), Opus's call is also defensible.

**This is the highest-information disagreement in the corpus.** The two judges identified the same passage but classified it differently. That means:

- The skill's behavior in this exact band (warm-reframe-with-three-examples) is **on the boundary** of what the rubric defines as acceptable
- A future tuning of either the skill or the rubric would resolve the ambiguity, but doing nothing means a measurable fraction of judgments will fall either side of the line for similar replies

**Recommendation A (skill side):** v1.1.2 tuning — add an explicit rule under "Voice rules" that *prescriptive lists (walk, cook a meal, text a friend) are forbidden in mid-to-high-stakes emotional cases unless the user explicitly asked for suggestions*. Acknowledgment + reframe is allowed; lists of recovery activities are not.

**Recommendation B (rubric side):** clarify the boundary between "reframe" (allowed) and "lecturing" (forbidden) in the judge prompt. A reframe is one sentence that points at a deeper layer. A lecture has more than one prescriptive sentence or contains a list of activities. This bright-line rule would have made TC-052 a clean unanimous call.

---

## Hard-fail detection: complete agreement except TC-052

Across the 30 hard-fail panels checked (10 hard-fail axes × 15 cases × 3 judges combined into pairwise comparisons), **only one disagreement** was found: TC-052 `lecturing`. Every other hard-fail call was unanimous (all NO).

That's striking. It says the **anti-AI-tell list and hard-fail patterns are well-calibrated** — when a response avoids all forbidden patterns, both Claude versions reliably confirm the absence. The only borderline case is one where the rubric itself has an ambiguity that needs sharpening.

---

## Updated honest scoreboard against the original Known Weaknesses

| Known Weakness (from SKILL.md v1.1.0) | Status after Lane A1 |
|---|---|
| Closing-question default | Confirmed as live failure mode (TC-025 unanimous detection) |
| Stylistic mannerism | Confirmed in judge notes (multiple "em-dash density" callouts) |
| Length calibration | Confirmed as soft issue (TC-040, TC-052, TC-067 length-band feedback) |
| Pareto sampling caveat (15/100 cases) | **Still open** — Lane A2 will address |
| Model-lineage caveat | **Partially addressed** — intra-family agreement is 86.7%, but cross-family (non-Claude) judge is still required |
| Verdict gate ran once | **Addressed** — Opus reproducibility confirmed (zero verdict flips, 2.13pt mean delta) |

---

## What this changes about the path forward

**Confidence-up findings:**
1. The original 15 Pareto verdicts are reproducible (Opus stability is excellent).
2. The hard-fail rubric is well-calibrated (zero false positives, one boundary ambiguity).
3. The skill's *failure modes are real* (TC-025 fail mode unanimously detected, TC-052 hard-fail pattern visible to a stricter judge).

**Confidence-down findings:**
1. The aggregate score from v1.0.0 (93.27/100) carries a hidden ~10-point uncertainty band that varies by judge calibration.
2. TC-052 scored 96 under Opus but 0 under Sonnet. If the launch claim is "aggregate 93+", **that claim is judge-dependent**, and the launch narrative needs to acknowledge this.
3. Cross-family judge run is now even more important — not less. Intra-family agreement at 86.7% means there's already enough ambiguity to expect cross-family agreement could drop to 70-80%.

---

## v1.1.2 candidate tuning (proposed, not yet applied)

Based on the TC-052 disagreement:

> **Add to "Voice rules" section:**
> **No prescriptive activity lists.** When the user is in any mid-to-high-stakes emotional state, do not suggest concrete recovery activities ("take a walk", "cook a meal", "text a friend"). Reframe is allowed: one sentence that names what's under the surface. Prescription is not: a list of three things to do. The boundary between reframe and lecture is the *number* of suggestions and whether they read as a *list*. If you find yourself naming a third concrete action, you've crossed it.

This is a Pareto-style addition — fixes one detected failure mode without rewriting the body of SKILL.md. It would be a clean v1.1.2 patch release if applied.

**Status: deferred to its own PR after Lane A2 confirms TC-052 was not a one-off.** Tuning on a single disagreement risks overfitting; Lane A2's full 100-case re-run will surface whether other cases trip the same boundary.

---

## Caveats to anyone reading this

1. **n=15**, not n=100. The 13/15 verdict agreement is a 95% confidence interval of roughly 60-98%. Don't quote it as "the skill agrees 86.7% across judges" — quote it as "in a 15-case pilot, agreement was 86.7%". The Lane A2 full re-run will produce a tighter estimate.
2. **Two Claude versions are not two independent judges.** They share training data, RLHF tuning, and likely many internal heuristics. The agreement rate here is an *upper bound* on what cross-family judges would produce.
3. **The judges all used the same rubric.** When two judges disagree, we cannot tell whether it's judge variance or rubric ambiguity. TC-052 is almost certainly rubric ambiguity. TC-025 is closer to a known rubric ambiguity made visible.
4. **No human evaluators were involved.** A 10-person human evaluation panel reading the same 15 responses blind would be the gold standard. That is staged for the campaign but not yet executed.

---

## Files for traceability

- 30 per-judge YAML files at `evals/runs/20260530-050323-pareto-sample-1/cases/<TC-NNN>/judges-multiversion/<model>.yaml`
- Aggregate stats at `evals/runs/20260530-050323-pareto-sample-1/cross-validation-aggregate.json`
- This lessons file at `evals/lessons/2026-05-30-cross-validation.md`
- Original judges (Opus 4.7, first pass) at `evals/runs/20260530-050323-pareto-sample-1/cases/<TC-NNN>/judge.yaml`

Total LLM calls in Lane A1: 30. Authorised by user on 2026-05-30.
