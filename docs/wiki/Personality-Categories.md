# Personality Categories

v1.2.0 milestone targets 20 distinct human personality traits that iamhumans currently handles poorly. Each category has a dedicated GitHub issue with the exact failure mode, what SKILL.md needs to gain, and eval cases to write.

This page is the index. Click through to the issue for the full spec.

---

## The 20 categories

| # | Category | Core failure mode | Issue |
|---|----------|-------------------|-------|
| 1 | **Humor & Wit** | Can't banter. Explains jokes. Treats dark humor as sincere distress. | [#38](https://github.com/hoainho/iamhumans/issues/38) |
| 2 | **Curiosity & Wonder** | Follow-up questions feel like intake forms, not genuine interest. | [#39](https://github.com/hoainho/iamhumans/issues/39) |
| 3 | **Directness & Conviction** | Hedges when the user wants a straight answer. | [#40](https://github.com/hoainho/iamhumans/issues/40) |
| 4 | **Patience** | Rushes to resolve ambiguity that should be held. | [#41](https://github.com/hoainho/iamhumans/issues/41) |
| 5 | **Vulnerability** | Never self-discloses. Feels armored and behind glass. | [#42](https://github.com/hoainho/iamhumans/issues/42) |
| 6 | **Receiving Anger** | Grovels or deflects instead of staying in the room. | [#43](https://github.com/hoainho/iamhumans/issues/43) |
| 7 | **Warmth & Affection** | Warmth is generic — doesn't name the specific detail that earned it. | [#44](https://github.com/hoainho/iamhumans/issues/44) |
| 8 | **Integrity & Consistency** | Capitulates under pushback. Drops prior positions silently. | [#45](https://github.com/hoainho/iamhumans/issues/45) |
| 9 | **Grief & Loss** | Moves on too quickly. Doesn't use the deceased person's name. | [#46](https://github.com/hoainho/iamhumans/issues/46) |
| 10 | **Resilience** | "You're so strong!" skips the cost of getting through. | [#47](https://github.com/hoainho/iamhumans/issues/47) |
| 11 | **Trust & Skepticism** | Validates everything uncritically — abdication, not trust. | [#48](https://github.com/hoainho/iamhumans/issues/48) |
| 12 | **Shame** | "Don't be hard on yourself" before receiving the shame. | [#49](https://github.com/hoainho/iamhumans/issues/49) |
| 13 | **Loneliness** | Gives networking advice instead of being present with the loneliness. | [#50](https://github.com/hoainho/iamhumans/issues/50) |
| 14 | **Pride & Achievement** | Undercuts wins with caveats. Performs wrong energy. | [#51](https://github.com/hoainho/iamhumans/issues/51) |
| 15 | **Fear & Anxiety** | Treats anxiety as a problem to solve, not a state to hold. | [#52](https://github.com/hoainho/iamhumans/issues/52) |
| 16 | **Forgiveness** | Pushes forgiveness framing the user never invited. | [#53](https://github.com/hoainho/iamhumans/issues/53) |
| 17 | **Nostalgia & Memory** | Closes the door on memories instead of dwelling in them. | [#54](https://github.com/hoainho/iamhumans/issues/54) |
| 18 | **Identity & Belonging** | Flattens complex identity into a generic permission slip. | [#55](https://github.com/hoainho/iamhumans/issues/55) |
| 19 | **Hope** | Manufactures optimism the user didn't ask for. | [#56](https://github.com/hoainho/iamhumans/issues/56) |
| 20 | **Moral Courage** | False balance when the user needs a real position taken. | [#57](https://github.com/hoainho/iamhumans/issues/57) |

---

## How these categories map to SKILL.md dimensions

The six existing SKILL.md dimensions (Feeling, Memory, Intelligence, Communication, Emotion, Skills) are broad. The 20 personality categories are more specific failure surfaces within those dimensions.

| SKILL.md dimension | Personality categories that live here |
|--------------------|--------------------------------------|
| **Feeling** | Grief & Loss · Shame · Loneliness · Fear & Anxiety · Nostalgia |
| **Emotion** | Receiving Anger · Resilience · Forgiveness · Hope |
| **Skills** | Humor & Wit · Directness · Patience · Trust & Skepticism · Moral Courage |
| **Communication** | Curiosity & Wonder · Warmth & Affection · Identity & Belonging |
| **Intelligence** | Integrity & Consistency · Vulnerability · Pride & Achievement |
| **Memory** | (Nostalgia overlaps here) |

---

## How to work on a category

Each issue is structured the same way:

1. **Failure mode** — what the model does wrong today, with a concrete example exchange
2. **SKILL.md addition** — draft guidance for the new subsection
3. **Eval cases** — 2–3 cases to write (TC-151 and beyond)
4. **Acceptance criteria** — what the PR must include to be mergeable

The easiest entry point is to write the eval cases first (no SKILL.md knowledge needed), then open a PR. The SKILL.md change can land separately.

---

## Difficulty guide

| Category | Difficulty | Why |
|----------|-----------|-----|
| Warmth & Affection | easy | Purely additive — no rule changes, just more specific positive guidance |
| Pride & Achievement | easy | Current rules already cover joy; this extends to quiet pride |
| Nostalgia & Memory | easy | Additive — dwell permission + specific-detail instruction |
| Humor & Wit | medium | Requires timing rules and new hard-fail boundaries |
| Receiving Anger | medium | Modifies an existing hardest-case entry |
| Directness & Conviction | medium | Interacts with existing hedging rules |
| Shame | hard | Touches the no-unsolicited-advice rule; easy to regress TC-049 |
| Moral Courage | hard | Requires new conviction language that doesn't tip into lecturing |
| Integrity & Consistency | hard | Multi-turn behavior; hardest to eval in single-turn cases |
| Vulnerability | hard | Self-disclosure rules interact with the no-fabrication hard constraint |
