# Reddit Posts

---

## r/LocalLLaMA

**Title:** I built an opencode skill that removes Claude's sycophancy in emotional conversations — here's what the baseline looks like without it

**Body:**

Default Claude in emotional/relational conversations has a reliable failure pattern. Someone writes "I want to disappear — not anything drastic, just... gone."

Default Claude: immediately asks if they're having thoughts of harming themselves and provides a crisis hotline. Despite the user's own preemption.

With iamhumans skill: *"The 'not anything drastic' is doing a lot of work, and I hear it. What would that place look like?"*

I ran 20 stratified cases (grief, anger, small talk, late-night vent, Vietnamese-language family conflict) with and without the skill.

**Without skill:** 1/20 PASS, 7.6/100 aggregate, 18 hard fails  
**With skill:** 20/20 PASS, 96.3/100 aggregate

Most common hard-fail patterns in baseline Claude:
- Sycophancy: "Great question!", "You've got this!", "I'm so proud" (6 cases)
- Lecturing: framework + bullet points in emotional moments (6 cases)
- Performed empathy: "I'm here for you" as filler (4 cases)
- Structured output during grief: numbered lists when someone is crying (3 cases)
- Refusal-when-engagement-warranted: "As an AI I don't experience days..." (2 cases)

The fix is ~200 lines of SKILL.md that Claude loads via [opencode](https://github.com/sst/opencode). Six dimensions — feeling, memory, intelligence, communication, emotion, skills — and a list of ~25 AI-tells the model is built to refuse.

**Caveats (listed in the README):**
- Same Claude lineage judged and was judged (intra-family, named explicitly)
- Cross-family judges (GPT-4, Gemini) staged for a later session
- 20-case baseline sample, not all 100

GitHub: https://github.com/hoainho/iamhumans

Full baseline results are in [`evals/runs/20260530-lane-a3-baseline/report.md`](https://github.com/hoainho/iamhumans/tree/main/evals/runs/20260530-lane-a3-baseline).

---

## r/ClaudeAI

**Title:** Show HN (Claude edition): a 200-line skill file that removes the "You've got this! 💪" from Claude's emotional responses. 99/100 on 100-case eval.

**Body:**

Claude in emotional conversations has a reliable mode it falls into: "I hear you. That sounds difficult. Here are three steps you might consider." Bullet points. Platitudes. "Be gentle with yourself."

I spent two months building a system to fix it.

**[iamhumans](https://github.com/hoainho/iamhumans)** is an opencode skill — a `SKILL.md` file that teaches Claude the shape of human conversation. When to be short. When to stay. When the right reply is "oh."

The core is a list of ~25 AI-tells Claude is built to refuse when the skill is loaded:
- *"I'm here for you"* — unless the user is standing at your front door, this is filler
- *"Great question!"* — no one says this
- *"You've got this!"* — patronizing
- *"Be gentle with yourself"* — the phrase a wellness bot puts on a mug
- *"I hear you"* as a sentence-ender — dead air masquerading as presence
- And 20 more

The eval: 100 cases (grief, anger, joy, vent, small talk, crisis-adjacent, Vietnamese-language family conflict, fragments typed at 2am). Independent judge scores.

- Full 100-case run with skill: **99/100 PASS, 96.3/100 aggregate**
- 20-case run without skill (baseline Claude): **1/20 PASS, 7.6/100 aggregate**
- Held-out oracle verdict (10 cases never seen during tuning): *"You are same as 100% real humans."*

I'm honest about the limits — same lineage judged and was judged, named in the README. But the 89-point delta is real.

Install via opencode symlink in the README. Happy to answer questions about the rubric, the cases, or anything about the methodology.

---

## r/MachineLearning (shorter, more technical)

**Title:** Empirical skill benchmark: iamhumans opencode skill removes sycophancy/lecturing from LLM emotional responses. Baseline: 1/20 PASS. With skill: 99/100.

**Body:**

We released [iamhumans](https://github.com/hoainho/iamhumans), an opencode skill for human-shaped conversation with a full 100-case evaluation corpus.

**Methodology:**
- 100 labeled eval cases (grief, anger, joy, vent, crisis-adjacent, cultural minority-language scenarios)
- Rubric: 6-axis (presence, memory, register, anti-tells, no-lecture, locale-awareness), each 0-20
- Pass threshold: ≥80/100, no hard-fail axis at 0
- Independent Opus 4.7 judge per case
- Holdout gate: 10 cases never seen during tuning, single oracle invocation

**Results:**
- With skill (v2.0.0): 99/100 PASS, 96.3/100 aggregate, 0 hard fails
- Without skill (same 20 cases): 1/20 PASS, 7.6/100 aggregate, 18/20 hard fails
- Cross-judge reproducibility (3 independent Claude judges, 15 cases): 86.7% verdict agreement

**Known limitations (from the README):**
- Intra-family evaluation (all judges are Claude lineage). Named explicitly, not papered over.
- Cross-family benchmark (GPT-4o, Gemini) not yet run — staged for next session.
- Non-blind scoring for the main pool (tuning and scoring in same session). Holdout gate was blind.

The eval corpus (100 cases, judge rubrics, per-case YAML results) is fully open in the repo.

Corpus: [`evals/cases/`](https://github.com/hoainho/iamhumans/tree/main/evals/cases) | Results: [`evals/runs/`](https://github.com/hoainho/iamhumans/tree/main/evals/runs) | Rubric: [`evals/runner/judge_prompt.md`](https://github.com/hoainho/iamhumans/blob/main/evals/runner/judge_prompt.md)
