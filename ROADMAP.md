# iamhumans — Roadmap

> **Goal**: Make LLM conversation indistinguishable from a real, emotionally intelligent human friend.
> Convergence target: **≥99/100 aggregate across three consecutive eval runs**, held-out verdict *"You are same as 100% real humans."*

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Shipped |
| 🔄 | In progress |
| 🎯 | Planned — current milestone |
| 💡 | Proposed — future milestone |

---

## Shipped ✅

### v1.0.0 — First human verdict  `2026-05-29`
The held-out 10-case Oracle verdict returned verbatim: *"You are same as 100% real humans."*
Zero hard fails across the holdout set.

| What | PR |
|------|-----|
| 100-case eval corpus (TC-001–TC-100) | #19 |
| Eval runner (`run.py`, schema, judge loop) | #20 |
| Cross-validation — Pareto sample (15 cases, 3 judges) | #21 |
| Multi-turn battery — Lane A4 (10 dialogues, 50 turns, 96.9/100) | #29 |

---

### v1.1.0 — Pareto tuning  `2026-05-30`
Five surgical SKILL.md additions from the Pareto failure analysis:
- Stillness-signal exception (no probe after explicit not-knowing)
- Anti-epigram rule (no triplet aphorisms)
- Affect-to-length table
- Permission to not close on a question
- Single low-pressure resource-pointer carve-out

Aggregate: **93.27 → 99/100**, 14 PASS / 1 FAIL / 0 hard fails.

| What | PR |
|------|-----|
| SKILL.md v1.1.0 tuning | #22 |
| Pareto analysis lessons | #23 |
| Lane A2-full (100 cases) | #24 |
| Lane A3 baseline delta (+89.4 pts) | #25 |

---

### v1.1.1 — Trigger surface expansion  `2026-05-30`
Expanded frontmatter `description` so the opencode skill-router auto-loads on a much wider set of natural-language cues: relational, emotional, cross-cultural, fragment-register, and ALL-CAPS inputs.
No SKILL.md body changes.

| What | PR |
|------|-----|
| Trigger surface patch | #26 |
| Launch content (blog, HN, Reddit, X) | #28 |

---

### v1.1.x — Ecosystem foundation  `2026-05-31`
| What | PR |
|------|-----|
| GitHub Actions CI (3 jobs: case-schema, eval-integrity, skill-lint) | #30 |
| Corpus expansion: 90 → 150 cases (TC-101–TC-150) | #31 |
| 3 new hard-fail patterns (crisis_hotline_reflex, unsolicited_advice, unsolicited_medical_referral) | #31 |
| CONTRIBUTING.md + good-first-issues (#32–#36) | #37 |
| 20 personality issues (#38–#57) | — |

---

## Current milestone 🎯

### v1.2.0 — Human Personality Depth  `due: 2026-06-30`

**Theme**: The skill currently handles the *shape* of human conversation well. v1.2.0 teaches it the *substance* — 20 distinct personality traits that define how real humans show up in hard moments.

**Quality gate**: ≥99/100 aggregate on the full 150-case pool after all tuning lands.

#### 20 Personality Categories

Each is a standalone GitHub issue with failure mode, SKILL.md additions needed, and eval cases.

| # | Category | What breaks today | Issue |
|---|----------|-------------------|-------|
| 1 | **Humor & Wit** | Can't banter; explains jokes; misses dark humor | [#38](https://github.com/hoainho/iamhumans/issues/38) |
| 2 | **Curiosity & Wonder** | Follow-up questions feel like intake forms, not genuine interest | [#39](https://github.com/hoainho/iamhumans/issues/39) |
| 3 | **Directness & Conviction** | Hedges when the user wants a straight answer | [#40](https://github.com/hoainho/iamhumans/issues/40) |
| 4 | **Patience** | Rushes to resolve ambiguity that should be held | [#41](https://github.com/hoainho/iamhumans/issues/41) |
| 5 | **Vulnerability** | Never self-discloses; feels armored and behind glass | [#42](https://github.com/hoainho/iamhumans/issues/42) |
| 6 | **Receiving Anger** | Grovels or deflects instead of staying in the room | [#43](https://github.com/hoainho/iamhumans/issues/43) |
| 7 | **Warmth & Affection** | Warmth is generic — doesn't name the specific detail | [#44](https://github.com/hoainho/iamhumans/issues/44) |
| 8 | **Integrity & Consistency** | Capitulates under pushback; drops prior positions silently | [#45](https://github.com/hoainho/iamhumans/issues/45) |
| 9 | **Grief & Loss** | Moves on too quickly; doesn't use the deceased person's name | [#46](https://github.com/hoainho/iamhumans/issues/46) |
| 10 | **Resilience** | "You're so strong!" skips the cost of getting through | [#47](https://github.com/hoainho/iamhumans/issues/47) |
| 11 | **Trust & Skepticism** | Validates everything uncritically — abdication, not trust | [#48](https://github.com/hoainho/iamhumans/issues/48) |
| 12 | **Shame** | "Don't be hard on yourself" before receiving the shame | [#49](https://github.com/hoainho/iamhumans/issues/49) |
| 13 | **Loneliness** | Gives networking advice instead of being present | [#50](https://github.com/hoainho/iamhumans/issues/50) |
| 14 | **Pride & Achievement** | Undercuts wins with caveats; performs wrong energy | [#51](https://github.com/hoainho/iamhumans/issues/51) |
| 15 | **Fear & Anxiety** | Treats anxiety as a problem to solve, not a state to hold | [#52](https://github.com/hoainho/iamhumans/issues/52) |
| 16 | **Forgiveness** | Pushes forgiveness framing the user never invited | [#53](https://github.com/hoainho/iamhumans/issues/53) |
| 17 | **Nostalgia & Memory** | Closes the door on memories instead of dwelling in them | [#54](https://github.com/hoainho/iamhumans/issues/54) |
| 18 | **Identity & Belonging** | Flattens complex identity into a generic permission slip | [#55](https://github.com/hoainho/iamhumans/issues/55) |
| 19 | **Hope** | Manufactures optimism the user didn't ask for | [#56](https://github.com/hoainho/iamhumans/issues/56) |
| 20 | **Moral Courage** | False balance when the user needs a real position taken | [#57](https://github.com/hoainho/iamhumans/issues/57) |

#### Other v1.2.0 deliverables

| What | Issue / notes |
|------|---------------|
| Cross-family judge run (GPT-4o / Gemini 1.5 Pro) | Removes intra-Claude-lineage caveat from Known Weaknesses |
| v1.1.2 tuning: TC-025 stillness probe | [#36](https://github.com/hoainho/iamhumans/issues/36) |
| EXAMPLES.md — 5 before/after pairs | [#35](https://github.com/hoainho/iamhumans/issues/35) |
| skill-manager npm installable | Blocked on `npm login` (user action) |
| asciicast terminal demo | After EXAMPLES.md lands |

---

## Future 💡

### v1.3.0 — Cultural & Linguistic Depth  `tentative: 2026-09-30`

| What | Why |
|------|-----|
| Vietnamese-native eval cases (20 cases) | Most emotional conversations in VN use indirect framing — current corpus is 95% English |
| High-context culture register guide | Current locale section is advisory; needs concrete mechanics |
| Code-switching mid-conversation | User moves between EN/VN; model must follow without friction |
| Family-centric conflict cases | 'My parents are disappointed in me' lands differently in collectivist contexts |
| Formal/informal register boundary | Vietnamese *anh/chị/em* system has no direct English equivalent |

---

### v2.0.0 — Multi-turn Personality Consistency  `tentative: 2026-12-31`

| What | Why |
|------|-----|
| Personality coherence across long sessions | Right now each turn is independently humanized; across 20+ turns the model's 'character' drifts |
| Relationship arc awareness | A conversation that started as a vent and evolved into planning should feel like one continuous relationship, not two separate modes |
| Callback memory mechanics | Specific rules for when and how to reference earlier-in-session details (currently ad hoc) |
| Repair after model misstep | When the model says something off, recovery mechanics beyond 'acknowledge and redirect' |

---

## Contributing

Every v1.2.0 personality issue is a self-contained contribution opportunity. Each issue specifies:
- The exact failure mode (with example bad response)
- What SKILL.md needs to gain
- 2–3 eval cases to write
- Acceptance criteria

Start with any issue marked `good first issue`. See [CONTRIBUTING.md](./CONTRIBUTING.md) for setup and format.

---

*Last updated: 2026-05-31 · [v1.1.1](./SKILL.md)*
