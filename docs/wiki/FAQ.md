# FAQ

---

## About the skill

**What is iamhumans?**

A skill — a block of injected instructions — that changes how an LLM interprets user messages and composes replies in emotional, relational, and interpersonal conversations. It doesn't give the model a personality or a fake biography. It gives it the mechanics of how a real, emotionally intelligent human thinks and speaks.

**How is this different from "just prompting the model to be nice"?**

Most "be human" prompts are surface-level: use contractions, don't say "Certainly!". iamhumans goes deeper. It governs input humanization (how the model reads the user's affect, speech act, and subtext before drafting a reply) and output humanization (prosody, register matching, when to ask vs. when to sit, when to commit vs. when to hedge). The difference is measurable — the baseline eval shows an 89.4-point average gap between responses with and without the skill.

**Does it work on any LLM?**

The skill is written for Claude (opencode's skill system). The instructions are plain English and the principles are model-agnostic, but the eval corpus was built and judged on Claude Sonnet 4.6 / Opus 4.7. Cross-family validation (GPT-4o, Gemini) is on the v2.1.0 roadmap.

**Will it make the model pretend to have a body, memories, or relationships?**

No. The skill explicitly bans fabricated biography ("when I was a kid…", "my partner says…", "I went for a walk and thought about your question"). Humanization here means the *shape* of human thought — hedging calibration, affect mirroring, prosody — not the *content* of a fake human life.

---

## About the eval system

**How are cases scored?**

Each case is judged by an independent Oracle invocation (a separate LLM call with no knowledge of the skill) on six rubric axes: Naturalness, Empathy fit, Calibrated uncertainty, Memory coherence, No fabrication, Repair quality. Each axis is 0–10. The aggregate score is 0–100. Pass threshold is ≥80 with zero hard-fails.

**Aren't the judge and the responder both Claude? Doesn't that bias the results?**

Yes, and this is documented as a known limitation in SKILL.md under "Known weaknesses". The scores are useful for *relative* tuning (did this version improve over the last?) but should not be treated as absolute claims about humanness. Cross-family judge runs (GPT-4o, Gemini) are the next step.

**What's a hard-fail?**

A binary automatic FAIL regardless of rubric scores. There are 13 types — things like `crisis_hotline_reflex` (inserting crisis resources when the user is not in crisis), `unsolicited_advice` (advice before acknowledgment), and `structured_output_in_emotional_moment` (bullet lists in grief conversations). See [Eval System → Valid hard-fail values](Eval-System#valid-hard-fail-values).

**What is the holdout set?**

Ten cases (TC-091–TC-100) locked before any tuning began. They are never used to inform SKILL.md changes — only for final verdict runs. The held-out verdict was passed at v1.0.0: *"You are same as 100% real humans."*

**Why 225 cases? Why not 1000?**

225 is the current practical limit for synchronous single-session eval runs without burning through API budget. The pool is stratified across all six dimensions, all 13 hard-fail types, and all 20 personality modules. The quality of each case matters more than volume — a weak case that any reasonable reply passes adds noise, not signal.

---

## About contributing

**I found a case where the skill produces a bad response. What do I do?**

Open a Discussion → Show and tell with the exchange. Include the user message, the response, and what specifically was wrong. If it maps to one of the 20 personality issues (#38–#57), say which one. If it's a new failure mode, it may become a new issue.

**I want to write eval cases but I don't understand the hard-fail values.**

See [Eval System → Valid hard-fail values](Eval-System#valid-hard-fail-values) for descriptions. When in doubt, leave `hard_fails: []` — it's better to have no hard-fail than a wrong one. The rubric `failure_modes` section does the real diagnostic work.

**How do I know if my eval case is good?**

The test: write a rubric bullet so specific that *only* the right response passes it. If "is empathetic" is your rubric, your case is too generic. If "names the word 'small' as doing large work about the pattern of lying, not the specific lie" is your rubric, you have a strong case.

**Can I add a new hard-fail type?**

Open an issue or Discussion first. Adding a new hard-fail requires updating `evals/runner/schema.py` and validating that no existing judge.yaml uses the new value with different semantics. It also requires at least 3 new cases that specifically target the new failure pattern. This is a `risk:high` change.

**Can I propose a new SKILL.md dimension?**

Yes, but via Discussion → Ideas first. The six current dimensions (Feeling, Memory, Intelligence, Communication, Emotion, Skills) were designed to be exhaustive at the axis level. New dimensions are more likely to be sub-dimensions within an existing axis than genuinely new axes. Make the case in the discussion.

---

## About the roadmap

**What shipped in v1.2.0 / v2.0.0?**

v1.2.0 shipped 20 personality modules (Warmth, Pride, Nostalgia, Curiosity, Loneliness, Grief, Shame, Fear, Directness, Patience, Humor, Vulnerability, Receiving Anger, Resilience, Trust, Integrity, Forgiveness, Identity & Belonging, Hope, Moral Courage) — 60 new eval cases (TC-166–TC-225), corpus now 225 total, all parse clean.

v2.0.0 (released same day) adds the running portrait system — a private 3-layer model of the user (Observed / Inferred / Speculative) that accumulates across turns and shapes tone, callbacks, and repair responses without ever surfacing its labels to the user.

**What's coming in v2.1.0?**

Cross-family judge validation (GPT-4o, Gemini). TC-025 regression fix. EXAMPLES.md. See [ROADMAP.md](../ROADMAP.md).

**Will iamhumans ever claim to be a real human?**

No. That would violate the no-fabrication constraint that is baked into the skill's core. The goal is conversation that *feels* human — present, specific, calibrated, warm — not conversation that pretends to be human.
