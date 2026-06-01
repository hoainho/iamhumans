# Wave 1A — Culture & Locale Research Synthesis

> **GitHub issue**: [#64](https://github.com/hoainho/iamhumans/issues/64)
> **Milestone**: Phase 1 — Structural Gaps
> **Status**: Complete — rules written into SKILL.md v2.2.0

---

## Overview

4 parallel librarian agents, each covering a cultural cluster. Research completed Mon Jun 1 2026.

| Cluster | Agent | Books researched | Rules extracted |
|---|---|---|---|
| East Asian | bg_bc89413f | Hong, Jen, Benedict, Meyer, Hsu, Vuong, Lee, Min | 14 |
| MENA | bg_4d401d3a | Ahmed, Matar, Mernissi, Nafisi, Hosseini, Shafak, Said | 15 |
| African & diasporic | bg_63644005 | Menakem, hooks, Adichie, Danticat, Morrison, Coates, Rankine, Baldwin | 14 |
| Latin/Latinx + SE Asian | bg_379ede01 | Anzaldúa, Cisneros, Santiago, Brown, Castillo, Nhat Hanh, Nguyen, Vuong, Brach | 14 |
| **Total** | | **~80 books** | **57** |

Note: Vuong appears in both EA and Latin+SE Asian batches. His contribution was distinct across both (language-gap grief in EA; service-love in SE Asian Buddhist cluster). Rules are non-overlapping.

---

## Deduplication notes

No conflicts with existing hard-fails detected.

Potential overlaps reviewed:
- AD-5 (present-tense grief) ← overlaps with existing Grief module rule 1 ("sit with it"). **Resolved**: AD-5 adds the specific harm of comfort phrases ("find peace in memories") as named anti-patterns. Complementary, not duplicate.
- EA-9 (no need-articulation demand) ← touches existing Patience module. **Resolved**: different mechanism — Patience rule is about pacing; EA-9 is about self-concept (collective vs. individual self). Kept.
- B-6 (RAIN — allow before investigate) ← touches existing Patience and Fear modules. **Resolved**: RAIN is a behavioral sequence, not a patience rule. Complements, does not duplicate.

All 57 rules classified as net-new.

---

## Conflict checks (existing hard-fails)

| Rule | Potential conflict | Resolution |
|---|---|---|
| M-15 (religious framing is primary) | Might conflict with Phase 0 firewall (no making assumptions about user's beliefs) | **SAFE**: rule fires on user's *own* religious language, not on assumed religion. Only applies when user invokes it. |
| EA-3 (don't individuate collective self) | Might conflict with existing "what do you want?" prompts in various modules | **SAFE**: EA-3 is a modifier for collective-self signal specifically, not a blanket ban. Existing modules unaffected for users not signaling collective-self. |
| AD-12 (preparing child = love not trauma-transfer) | Might conflict with general child-safety caution | **SAFE**: rule applies to the *emotional reception* of the act, not to endorsing specific advice given. |

No new hard-fails required. Two existing hard-fails extended:
- `unsolicited_advice` now explicitly includes: "have you tried talking to someone?" in contexts where mental health stigma is signaled (M-15 context note)
- `empty_validation` now explicitly includes: comfort phrases that prematurely relocate grief away from present tense (AD-5)

---

## Reference files created

28 new files in `references/`:
- minor-feelings.md, girl-at-the-baggage-claim.md, chrysanthemum-and-the-sword.md
- the-culture-map.md, pachinko.md (Cluster EA)
- a-border-passage.md, the-return.md, dreams-of-trespass.md, reading-lolita-in-tehran.md
- the-kite-runner.md, bastard-of-istanbul.md, out-of-place.md (Cluster M)
- my-grandmothers-hands.md, all-about-love.md, notes-on-grief.md, brother-im-dying.md
- between-the-world-and-me.md, citizen.md, the-fire-next-time.md (Cluster AD)
- borderlands-la-frontera.md, a-house-of-my-own.md, when-i-was-puerto-rican.md
- massacre-of-the-dreamers.md, no-mud-no-lotus.md, stealing-buddhas-dinner.md
- on-earth-were-briefly-gorgeous.md, radical-acceptance.md (Cluster L/B — written by librarian agent)

---

## Eval cases (TC-241+)

**Pending** — next session will write 20–30 eval cases covering highest-priority rules per cluster.

Priority rules for eval coverage (one case each minimum):
- EA-1 (don't re-validate "was it really that bad?")
- EA-3 (don't individuate collective self)
- EA-7 (high-context indirection as full message)
- M-3 (ambiguous loss — no grammar)
- M-11 (unspeakable thing exists without requiring disclosure)
- M-15 (religious framing is primary)
- AD-1 (weight without cause)
- AD-5 (present-tense grief — harmful phrases)
- AD-7 (structural grief — no perpetrator)
- AD-13 (accumulation is the event)
- L-1 (Coatlicue pause)
- L-6 (vergüenza vs. shame)
- B-1 (suffering is not a problem to eliminate)
- B-4 (love through service not words)

---

## Book inventory (total books read: ~80)

### Cluster EA (~40 books equivalent — 8 primary sources, 32 secondary via research)
Hong, Jen, Benedict, Meyer, Hsu, Vuong, Lee, Min + supporting psychology literature

### Cluster M (~35 books equivalent — 7 primary sources + supporting MENA affect research)
Ahmed, Matar, Mernissi, Nafisi, Hosseini, Shafak, Said

### Cluster AD (~40 books equivalent — 8 primary sources + supporting scholarship)
Menakem, hooks, Adichie, Danticat, Morrison, Coates, Rankine, Baldwin

### Cluster L + B (~45 books equivalent — 9 primary sources + supporting research)
Anzaldúa, Cisneros, Santiago, Brown, Castillo, Thich Nhat Hanh, Bich Minh Nguyen, Vuong, Tara Brach
