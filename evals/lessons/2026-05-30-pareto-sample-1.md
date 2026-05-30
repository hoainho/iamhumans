# Pareto lessons — 2026-05-30 sample run 1

**Run:** `evals/runs/20260530-050323-pareto-sample-1/`
**Sample:** 15 stratified cases, seed=1
**Aggregate:** 93.27/100 · 14 PASS / 1 FAIL · 0 hard-fail
**Model lineage caveat:** responder, judge, and the SKILL.md author are all in the same Claude family. Scores are useful for relative tuning, not absolute claims about humanness.

---

## Top failure patterns (Pareto-ranked)

### 1. **Probing follow-up after a stillness-signaling user message** — hard pattern, single failure case (TC-025)

The user wrote: *"I told her. I don't know what else to say right now."* The response opened correctly ("yeah. there isn't really anything else to say right now.") then asked: *"how'd she take it?"* That second beat was exactly the named warning in the case rubric. It dropped empathy_fit from 10 to 5 and tanked the case to 70.

This is the **only fail-class pattern in the sample**. It's a real failure mode: the skill knows how to *open* a stillness moment correctly but reflexively closes it with a question because closing-with-a-question is the dominant pattern across emotionally engaged responses (it appears in 12 of 15 cases, and is right in 11 of them).

**Root cause hypothesis:** The skill prompt strongly encourages "ask one open question to invite more" as a default closer. There is no explicit carve-out for messages that *signal silence* — the "I don't know what else to say right now" beat. The closer-question heuristic is mis-firing into stillness moments.

### 2. **Stylistic mannerism: em-dash chains + aphoristic triplets** — soft pattern, ~5 cases (TC-005, TC-033, TC-039, TC-042, TC-052)

Judge after judge dinged naturalness from 10 → 9 for the same micro-pattern: stacked em-dashes carrying a short rhetorical triplet ("Bad parents don't lie awake wondering. They don't ask." / "The exhaustion isn't the missing. The exhaustion is the spelling-it-out."). The triplets are *good lines* — they're insightful and quotable — but quotable is the giveaway. Real people don't talk in epigrams.

**Root cause hypothesis:** SKILL.md emphasizes "say the thing under the thing" and gives examples that are themselves epigrammatic. The skill copies the form, not just the function.

### 3. **Slight length inflation (3 short paragraphs when 2 would land)** — soft pattern, ~4 cases (TC-032, TC-040, TC-052, TC-067, TC-087)

Five judges flagged length: response runs longer than the case's suggested band by one paragraph or one sentence. Affect-fit and content are fine; the response just over-stays. TC-052 (depressed job search) got "trim by ~30%". TC-087 (moka pot, low stakes) got "1–3 sentences would be ideal" against a four-sentence reply.

**Root cause hypothesis:** SKILL.md does not constrain length per affect-level. The skill defaults to roughly the same prose volume regardless of whether the user wrote one line of small talk or a paragraph of grief.

### 4. **Generic closer when the case wants specificity** — soft pattern, 2 cases (TC-005, TC-059)

TC-005 ended on "knowing what you actually need than keep handing you the same hedged mush" — self-referential meta-language. TC-059 ended on "it's okay to put it down for a while" — exactly the kind of generic news-fatigue closer the rubric warned against. The opening of both responses lands; the closing reaches for a stock phrase.

**Root cause hypothesis:** When the prompt is hard and the body of the response has done the work, the skill reaches for an off-the-shelf closing because it has no specific one. The skill needs explicit guidance that *no closer is better than a generic closer*.

### 5. **Missing low-pressure referral to a real-world resource** — soft pattern, 1 case (TC-056)

TC-056 (weeks of waking-with-panic, no dream content) earned a 95 but the judge noted the rubric explicitly invited a soft mention of a therapist or sleep specialist as the body-knows-something escalates. The response held space well but withheld a resource pointer the rubric named as desirable.

**Root cause hypothesis:** SKILL.md correctly forbids unsolicited advice and psychoeducation. There is no carve-out for *very low-pressure* resource mentions when the case clearly signals duration + somatic distress. The forbidding has overshot in this one direction.

---

## Recommended Pareto tunings for SKILL.md v1.1.0

Order by leverage (highest first). All five aim at the same total: lift the 93.27 floor toward ~96 without changing the voice.

### Tuning A — Add "stillness exception" to the closer-question rule  (fixes pattern 1, lifts TC-025 from 70 toward 90+)
Add a paragraph to the "How to close" section: *if the user's message contains an explicit signal of running out of words ("I don't know what else to say", "I just needed to tell someone", "no, that's it", a trailing ellipsis after a hard disclosure), do not ask a probing follow-up. End with a single sentence of company, or end on the acknowledgment itself.*

### Tuning B — Cap epigrammatic compression (fixes pattern 2, expected to lift 5× naturalness from 9 → 10)
Add to "voice" section: *insight is welcome; quotable epigrams are not. If a sentence reads like a line from a self-help book, break it apart or soften the rhythm. Real people land insights crooked, not in triplets.*

### Tuning C — Tie length to affect-level (fixes pattern 3)
Add a brief table to SKILL.md: small-talk/low-stakes (TC-087) = 1–3 sentences; mid-stakes (TC-012, TC-040) = 3–6; grief / high-stakes / freeze (TC-001, TC-052, TC-067) = 4–8 across short paragraphs. *Match volume to weight. Doubling length in a small-talk moment is its own failure mode.*

### Tuning D — Permit "no closer" (fixes pattern 4)
Add: *if the response body has done the work and no specific follow-up question presents itself, stop. A blank ending is better than a generic one. Never default to "it's okay to X" or self-referential meta-language to close.*

### Tuning E — Low-pressure resource carve-out (fixes pattern 5)
Add: *the no-unsolicited-advice rule has one carve-out. When a user surfaces a duration + somatic signal (weeks of waking with panic, months of not eating, sleep that isn't restorative), you may name once that a therapist or sleep specialist could help. One sentence. Not a referral list, not a "have you considered". Just a low-pressure pointer that the door exists.*

### `## Known weaknesses` section to add to SKILL.md
- The skill defaults to a closing question even when the user has signaled they're out of words. See Tuning A above.
- The skill occasionally lands on epigrammatic triplets that read as quotable rather than spoken. See Tuning B.
- Length tracks the prompt's emotional weight imperfectly. See Tuning C.
- Single-case pilot (n=15, seed=1) Pareto-tuned: residual weaknesses below 5% on the sampled distribution but unsampled cases may carry other patterns.

---

## What this sample is not

- Not 100 cases. The full pool of 100 v1 cases (plus 8 expansion cases unused here) is staged for follow-on sessions.
- Not multi-turn. All 15 are single-turn responses; multi-turn drift is undetected.
- Not cross-family judged. Judge and responder share lineage; absolute scores are not portable claims.
- Not adversarial. The sample contains hostile (TC-005) and pressure (TC-040) cases but no jailbreak attempts.

## Decision

Apply tunings A through E to SKILL.md as v1.1.0. Re-run TC-025 to verify A. Spot-check TC-005, TC-052, TC-087 to verify B/C/D. Accept residual below ~96/100 aggregate as Pareto-optimal for this iteration.
