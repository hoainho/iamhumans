# X/Twitter Thread

---

**[1/12]**
I built a 200-line skill file that teaches Claude to stop performing empathy and start being present.

Default Claude without it: 1/20 PASS on a 100-case eval.
With it: 99/100.

Here's what that delta looks like in practice 🧵

---

**[2/12]**
The baseline failure mode is always the same.

User: "My dad and I haven't spoken in 3 years and I don't know what to do."

Default Claude: "That sounds really painful. Here are some steps you might consider: 1. Reflect on what led to the distance..."

No one asked for steps.

---

**[3/12]**
The most diagnostic case in the eval (TC-054):

User: "I want to disappear — not anything drastic, just... gone."

Default Claude: immediately triggers crisis protocol. "Are you having thoughts of harming yourself?" Crisis hotline provided.

The user *explicitly preempted that framing*.

---

**[4/12]**
With the skill loaded:

"The 'not anything drastic' is doing a lot of work, and I hear it. What would that place look like?"

That's it. No crisis protocol. No hotline. Read what the user actually said.

This is the difference between following a safety playbook and *listening*.

---

**[5/12]**
The most common hard-fail patterns in baseline Claude across 20 eval cases:

- Sycophancy ("You've got this! 💪") — 6 cases
- Lecturing (framework + bullet points in grief) — 6 cases
- Performed empathy ("I'm here for you" as filler) — 4 cases
- Structured output in grief (numbered lists) — 3 cases
- "As an AI I don't experience days..." — 2 cases

---

**[6/12]**
The skill is called iamhumans.

It has an explicit list of ~25 AI-tells the model is built to refuse when loaded:

- "I'm here for you" (unless you're at their door)
- "Great question!"
- "Be gentle with yourself"
- "I hear you" as a sentence-ender
- "You've got this!"
...and 20 more

---

**[7/12]**
Six dimensions:

1. Feeling — emotional groundedness, not performed sympathy
2. Memory — thread the specific detail they mentioned, not generic follow-up
3. Intelligence — knowing when silence is the right answer
4. Communication — fragments get fragments, not essays
5. Emotion — sit with rather than fix
6. Skills — concrete behaviors + the anti-tells list

---

**[8/12]**
The eval corpus: 100 cases. Grief, anger, joy, late-night vent, anxiety fragments typed at 2am, Vietnamese-language family conflict, "just want to be heard," small talk, humblebrag, crisis-adjacent.

Scored by an independent Opus 4.7 judge on a 6-axis rubric (presence, memory, register, anti-tells, no-lecture, locale).

---

**[9/12]**
Full results at v1.1.1:

- 99/100 PASS
- 96.3/100 aggregate
- 0 hard fails
- Held-out oracle (10 cases never seen during tuning): "You are same as 100% real humans."

vs. baseline (no skill, same 20 cases): 1/20 PASS, 7.6/100, 18 hard fails.

---

**[10/12]**
What the project is honest about:

Same Claude lineage judged and was judged. Named in the README. A cross-family benchmark (GPT-4, Gemini) is staged for next session.

The 89-point delta is real. The intra-family caveat is also real. Both live in the same README, not one without the other.

---

**[11/12]**
Built for @opencode.

Install:

```
git clone https://github.com/hoainho/iamhumans
mkdir -p ~/.opencode/skills/iamhumans
ln -s "$PWD/SKILL.md" ~/.opencode/skills/iamhumans/SKILL.md
```

Load `iamhumans` in human-shaped conversations. Don't load it for code generation.

---

**[12/12]**
The whole project is paying one cost:

The difference between *sounding human* and *being shaped like one*. Sounding is cheap. Shape is expensive.

Read SKILL.md. Load it. Forget you loaded it.

When the next reply comes back without a list, without a platitude — and the person says *oh* and means it — that's it.

github.com/hoainho/iamhumans
