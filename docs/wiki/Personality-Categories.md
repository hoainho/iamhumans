# Personality Categories

20 personality modules shipped in v1.2.0 / v2.0.0. Each module adds concrete behavioral rules to SKILL.md and 3 eval cases to the corpus. All 20 are live — TC-166–TC-225 (60 cases total), all parse clean.

This page is the index. Click through to the issue for the original spec and failure-mode analysis.

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

## How to contribute to an existing module

Each module's issue documents the original failure mode and the SKILL.md additions that addressed it. If you find a case the current rules still miss:

1. Open a Discussion → Show and tell with the exchange
2. If it's a new edge case within an existing module, write a new eval case (TC-226+) and open a PR
3. If it's a failure mode that doesn't fit any of the 20 — open a Discussion → Ideas for a new module proposal

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
