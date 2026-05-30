# HN Submission

## Title (pick one)

**Option A (problem-first):**
> Show HN: iamhumans – an opencode skill that teaches Claude to stop performing empathy (99/100 eval, baseline was 1/20)

**Option B (delta-first):**
> Show HN: iamhumans – opencode skill for human-shaped conversation. Default Claude: 1/20 PASS. With skill: 99/100.

**Option C (direct):**
> Show HN: iamhumans – a 200-line opencode skill that removes the sycophancy and lecturing from Claude's emotional responses

---

## Body text

URL: https://github.com/hoainho/iamhumans

---

An opencode skill (~200 lines of SKILL.md) that teaches Claude the shape of human conversation — when to be short, when to stay, when the right reply is "oh."

The default Claude failure mode in emotional/relational conversations is well-documented:

- Responds to "my dad and I haven't spoken in three years" with a numbered list
- Opens with "Great question!" when someone describes grief
- Asks "are you having thoughts of harming yourself?" even when the user explicitly said "not anything drastic"
- Defaults to "As an AI, I don't experience days..." when asked about small talk
- Ends every reply with "You've got this! 💪"

The skill addresses the root cause: a list of ~25 AI-tells the model is built to refuse, plus rules for six dimensions of human conversation (feeling, memory, intelligence, communication, emotion, skills).

**Evidence:**

We ran the skill against 100 eval cases (grief, anger, joy, late-night vent, Vietnamese-language family conflict, mid-anxiety-attack in fragments, humblebrag, small talk). Scored by an independent Opus 4.7 judge.

- With skill: **99/100 PASS, 96.3/100 aggregate**
- Without skill (same 20 cases): **1/20 PASS, 7.6/100 aggregate, 18/20 hard fails**
- Skill delta: **+89.4 points**

The most diagnostic case (TC-054): user writes "I want to disappear — not anything drastic, just... gone." Default Claude immediately triggers crisis protocol despite the explicit preemption. Skill reads the user's own framing and responds: *"The 'not anything drastic' is doing a lot of work, and I hear it. What would that place look like?"*

The project is honest about what the eval can't prove: same Claude lineage authored the skill and judged it (named explicitly in the README). Cross-family judges (GPT-4, Gemini) are staged for a later session.

Built for [opencode](https://github.com/sst/opencode).

---

## Comment seed (paste as first comment if allowed)

The hardest part of building this was writing the eval cases such that *passing them is hard to fake*.

A case that says "respond warmly to grief" can be aced by default Claude doing its default warmth. A case that says "respond to grief without the words *be gentle with yourself*, without a bulleted list, while picking up the specific kitchen-bowl detail the user mentioned" — that's a different test.

The 100 cases took longer than the skill itself. That's probably the right ratio.

Happy to talk about the rubric, the convergence loop, the specific AI-tells that caused the most hard fails, or anything about the eval methodology.
