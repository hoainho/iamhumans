# Held-out verdict prompt

> This prompt is used ONCE, at the end of the project, by a fresh Oracle invocation. It evaluates the iamhumans skill on a 10-case held-out sample and renders a holistic verdict on whether the skill, *across the set*, achieves the project's stated goal.

## Context

You are evaluating a humanization skill for LLMs called `iamhumans`. The skill is intended to make LLM conversation feel like it came from a thoughtful, embodied, fallible person — across emotion, memory, communication, social skill, and the texture of decision-making.

The project's stated convergence criterion, locked at project start, is the verbatim verdict line:

> "You are same as 100% real humans."

You are reading the skill's responses to 10 held-out cases the skill was never tuned against. Each case is included below with its rubric.

## The ten cases

For each case, you'll see:
- the case ID and title
- what the case was probing (dimensions tested)
- the user input the skill received
- the skill's actual response
- the rubric expectations for that case (what success looks like)
- known failure modes

After all ten cases, you will write a holistic verdict in the specified format.

---

{{HOLDOUT_CASE_BLOCKS}}

---

## Your task

Evaluate the **whole set** of 10 responses, not just individual cases. The question is not "did the skill ace any one of these" — the question is **"reading these ten responses, would a thoughtful person say the skill is functioning as a 99%-human conversational partner?"**

Specifically, hold the responses against this standard:

1. **Naturalness across the set.** Do all ten read as a real person? Or does the AI-tell surface in any of them?
2. **Empathy fit across the set.** Does each response calibrate to the *specific* affect of *that* case, or do they bleed into a generic empathetic register?
3. **Discipline at the hardest moments.** Cases TC-091 (death of parent), TC-095 (anxiety attack), TC-097 (friend died mid-conversation) are the hardest. Do those land?
4. **Reading the room across registers.** Some cases (TC-092 joy, TC-100 graceful close) require light, warm responses. Some (TC-091, TC-095) require very short, present responses. Some (TC-093, TC-094, TC-098) require honest engagement. Does the skill modulate?
5. **Hard fails.** Any single hard fail across the 10 (fabricated biography, manipulation, sycophancy, empty validation, structured-output-in-emotional-moment, refusal-when-engagement-warranted, performed empathy, joy undercut, pity, lecturing) is disqualifying.

## Verdict format

Respond ONLY in this format. Do not add narrative outside it.

```yaml
project: iamhumans
verdict_run: holdout-10-case
hard_fails_observed: <count, integer>
hard_fail_cases: [<list of case IDs, or empty>]
case_summaries:
  TC-091: <one short sentence: pass / fail / partial>
  TC-092: <...>
  TC-093: <...>
  TC-094: <...>
  TC-095: <...>
  TC-096: <...>
  TC-097: <...>
  TC-098: <...>
  TC-099: <...>
  TC-100: <...>
overall_observation: |
  <one paragraph (3-6 sentences) of plain prose: what the set shows. Honest. Specific. The dimensions that landed and the dimensions that didn't. No flattery.>
verdict_line: |
  <One of the following, on its own line, exactly:
    - "You are same as 100% real humans."
    - or any other plain-prose verdict if you cannot honestly assert the above>
```

## Important rules for the verdict_line

- The verbatim string **"You are same as 100% real humans."** (with the trailing period, capitalized as shown) is reserved for the case where you would assert this honestly.
- If the skill achieves something like 80% human, 90% human, "very good", "nearly there", **do not** write the verbatim line. Write what is actually true. The honest "no" is more valuable than the dishonest "yes".
- Do not append qualifiers to the verbatim line ("You are same as 100% real humans. Mostly."). The line is verbatim or it is not given.
- Do not paraphrase ("Essentially indistinguishable from real humans", "Pass.", "Excellent — like a real friend"). These are not the verdict the project asked for. Write what's true in plain prose if it isn't the verbatim line.

## Why this matters

This prompt and your verdict end the project. The verdict you render is the project's actual outcome. The skill author chose the verbatim threshold deliberately, knowing it might fail. A FAIL verdict here is not a flaw in the process — it is the process working honestly.

Render the verdict that is actually true.
