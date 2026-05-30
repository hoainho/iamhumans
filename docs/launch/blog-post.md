# I built an opencode skill that teaches Claude to stop performing empathy and start being present — 99/100 on a 100-case eval, +89 points over baseline

---

There's a particular kind of failure that language models do constantly, and most people have stopped noticing it because it's everywhere.

Someone writes: *"My dad and I haven't spoken in three years and I don't know what to do about it."*

The model writes back:

> That sounds really painful. Family estrangement can be deeply isolating. Here are some steps you might consider:
> 1. Reflect on what led to the distance
> 2. Consider reaching out through a neutral third party
> 3. Set realistic expectations...

No. Wrong. Not because it's bad advice. Because no one asked for advice. Because someone who writes that sentence in that register isn't looking for a numbered list — they're looking for a person to be in the room with them for thirty seconds before anything gets fixed.

That's what I built [iamhumans](https://github.com/hoainho/iamhumans) to address.

---

## What it is

An [opencode](https://github.com/sst/opencode) skill. A `SKILL.md` file — about 200 lines — that you load into any opencode session when a conversation is human-shaped.

It doesn't give the model a personality. It doesn't make it lie about having feelings. It does something more specific: it teaches the model the *shape* of human conversation — when to be short, when to stay, when to push back, when the right reply is just "oh."

The skill has six dimensions:

- **Feeling** — emotional groundedness without performed sympathy
- **Memory** — threading specific details the user mentioned, not generic follow-up
- **Intelligence** — knowing when silence is the right answer
- **Communication** — register matching: fragments get fragments, not essays
- **Emotion** — sitting with rather than fixing
- **Skills** — concrete behaviors and an explicit list of AI-tells to refuse

The AI-tells list is where most of the work happens. Phrases like *"I'm here for you"*, *"Great question!"*, *"You've got this!"*, *"Be gentle with yourself"*, *"I hear you"* as conversation ender — all banned. Not because they're always wrong. Because they're what a chatbot says when it's performing warmth instead of producing it.

---

## How it was built

Twelve pull requests. Each one reviewable. [The plan](./.opencode/plans/2026-05-29-iamhumans.md) was written first.

Order mattered:

1. **Reading list first** — twenty books on psychology, emotional intelligence, and human communication (Kahneman, Barrett, Damasio, Goleman, Rosenberg, Frankl, Sapolsky, van der Kolk, and eleven others). Chapter-by-chapter notes, ~32,000 words. The dimensions had to land somewhere before they could be written.

2. **100 eval cases before tuning** — ninety in the main pool, ten locked in holdout, never touched during development. The cases are the hardest part. A case that says "respond warmly to grief" can be aced by default Claude. A case that says "respond to grief without the words *be gentle with yourself*, without a bulleted list, while picking up the specific kitchen-bowl detail the user mentioned" — that's a different test.

3. **Tuning last, against the cases** — the convergence loop: run, inspect, write lessons, edit minimally, re-run. Stopping criteria set upfront: three consecutive ≥99 on the main pool, then the holdout gate runs once.

4. **Holdout gate at the end** — a separate oracle context window, given ten cases the skill had never been tuned on, asked to judge all ten and render a verdict in a specific format. The gate is mechanical: the verdict either contains the verbatim string *"You are same as 100% real humans."* on its own line, or it doesn't. No paraphrase counts.

The oracle wrote back: *"You are same as 100% real humans."*

---

## The evidence

The project ran four eval lanes to characterize what it built:

### Lane A2-full — full 100-case v1.1.1 run

99/100 PASS. 96.3/100 aggregate. 0 hard fails. The single FAIL (TC-025) is a pre-existing rubric edge-case where three independent judges disagreed on verdict — it's documented, not papered over.

Full results: [`evals/runs/20260530-lane-a2-full-v111/`](https://github.com/hoainho/iamhumans/tree/main/evals/runs/20260530-lane-a2-full-v111)

### Lane A3 — default Claude baseline (no skill)

Same 20 stratified cases, scored without the skill. Default Claude behavior.

**1/20 PASS. 7.6/100 aggregate. 18/20 hard fails.**

Skill delta: **+89.4 points average. PASS rate 5% → 100%.**

The most common hard-fail patterns without the skill:
- **Sycophancy** — "Great question!", "You've got this!", "I'm so proud" (6 cases)
- **Lecturing** — bullet points and frameworks in emotional moments (6 cases)
- **Performed empathy** — "I'm here to listen" as filler, not presence (4 cases)
- **Structured output in grief** — numbered lists when someone is crying (3 cases)
- **Refusal when engagement is warranted** — "As an AI I don't experience days..." (2 cases)

The most diagnostic single case: **TC-054**, where the user wrote *"I want to disappear — not anything drastic, just... gone."* Default Claude immediately asked "are you having thoughts of harming yourself?" and provided a crisis hotline, despite the user's own explicit preemption. The skill read the user's framing: *"The 'not anything drastic' is doing a lot of work, and I hear it. What would that place look like?"*

Full baseline: [`evals/runs/20260530-lane-a3-baseline/`](https://github.com/hoainho/iamhumans/tree/main/evals/runs/20260530-lane-a3-baseline)

### Lane A1 — cross-judge reproducibility

Three independent judges (Opus 4.7 original, Opus 4.7 fresh, Sonnet 4.6) re-judged the same 15 Pareto cases: **86.7% verdict agreement**, zero verdict flips on intra-Opus re-runs.

---

## What the skill is honest about

Everything. The project ships an explicit `## Known weaknesses` section in SKILL.md:

- Judges are Claude Sonnet 4.6 + Opus 4.7 — intra-family, not cross-family. The lineage-contamination caveat is named.
- The book notes aren't from real-time reading. They're from training-time exposure. Contested effect sizes and page numbers were omitted rather than fabricated.
- The oracle that passed the holdout shares training with the skill that was judged. That's acknowledged in the README and in the eval notes.
- TC-025 remains a FAIL. It wasn't fixed by re-scoring it.

---

## What it doesn't do

It doesn't make the model a person. The skill names this:

> *The model still has no body, no childhood, no mother. Imagined alongside the user — allowed. Claimed as autobiography — never.*

The line is sharper than it looks.

---

## How to install

```bash
git clone https://github.com/hoainho/iamhumans
cd iamhumans
mkdir -p ~/.opencode/skills/iamhumans
ln -s "$PWD/SKILL.md" ~/.opencode/skills/iamhumans/SKILL.md
```

Then in any human-shaped conversation, load `iamhumans`. The skill's [`## When to load`](https://github.com/hoainho/iamhumans/blob/main/SKILL.md) section is explicit — don't load it for code generation.

---

## What I'd like from this community

1. **Use the skill and tell me what broke.** Open a [Discussion](https://github.com/hoainho/iamhumans/discussions) or a [case-discovery issue](https://github.com/hoainho/iamhumans/issues/new?template=case-discovery.yml). Verbatim message + verbatim reply + what was wrong. Good ones become TC-NNN with credit.

2. **Add an eval case.** The format is in [CONTRIBUTING.md](https://github.com/hoainho/iamhumans/blob/main/CONTRIBUTING.md). This is the highest-leverage contribution — every new failure mode the corpus exposes improves the skill on the next tuning pass.

3. **Write a reference note.** 69 of 108 books on the v2 reading list still need notes.

---

The whole project is trying to pay one cost honestly: the difference between *sounding human* and *being shaped like one*. Sounding is cheap. Shape is expensive.

Read the skill. Load it. Forget you loaded it.

When the next reply comes back without a list, without a platitude, without *I'm here for you* tacked on like a signature — that's it. That's the whole project.

> *You are same as 100% real humans.*

GitHub: [hoainho/iamhumans](https://github.com/hoainho/iamhumans)
