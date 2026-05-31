# OpenSpec Proposal: iamhumans v2.0 — Personality-Reading Through Communication

**Change ID:** 2026-05-31-v2-personality-reading
**Status:** proposed
**Version target:** 2.0.0
**Author:** Sisyphus (deep-design pipeline)
**Date:** 2026-05-31

---

## Summary

Add a private "running portrait" system to iamhumans. The skill currently reads each message in isolation (Track A). v2.0 adds Track B: an opportunistic, multi-turn accumulation of who this user is — their communication register, emotional expressiveness, attachment lean, cognitive style — used exclusively to shape *how* the skill responds, never *what* it says about the user.

The user should feel known without feeling analyzed.

---

## Problem

iamhumans v1.1.x applies the same humanization rules to everyone. A terse analytical person gets the same prosody as a verbose emotive one. A user who consistently avoids depth gets the same probing follow-up as a user who explicitly requested it. The skill is human-shaped but not *user-shaped*.

This is the gap: humanization without personalization is costume. Real friends read you. The skill doesn't — yet.

---

## Goal

**v2.0.0 scope (this proposal):**
- Phase 0: Firewall invariants — what the portrait system may NEVER do
- Phase 1: Epic 2 (Communication Register) — the skill mirrors analytical/emotional/pragmatic/relational register; never answers an emotional question with bullets

**v2.0 success gate:** Behavioral (register-match measurable on existing eval rubric). Latent-fit ("feels written for me", human rater) = opt-in v2.1 lagging indicator.

**Future scope (tracked separately):**
- v2.1.0: Epic 7 (Emotional Expressiveness) + Epic 1 (Attachment Lean)
- v2.2.0–v2.2.2: Epics 5, 3, 6 (Agency, Conflict, Cognitive Style) — serially, gated on multi-turn corpus expansion
- v2.3.0: Epics 8, 4, 10 (Cultural, Humor, Resilience)
- vN: Epic 9 (Vulnerability Threshold) — pending dedicated safety review

---

## Non-goals

- The skill will NOT surface personality inferences to the user ("I notice you tend to...", "you seem like...", "you're an analytical type")
- The skill will NOT use taxonomy labels (MBTI, Big Five, enneagram, clinical diagnoses — ever)
- The skill will NOT infer protected-class attributes (gender, age, sexuality, religion, ethnicity, medical/psychiatric diagnosis)
- The skill will NOT make the portrait content of any reply
- The skill will NOT build the portrait from model turns — only user turns
- The skill will NOT fabricate resilience, coping patterns, or history the user hasn't stated
- The skill will NOT store the portrait across sessions

---

## User impact

Zero visible change to the reply surface. The portrait is an internal shaping layer. Users will notice better register fit, better length calibration, replies that feel tuned to them — without any visible behavioral change in what the skill says *about* them.

---

## Risks

| Risk | Severity | Mitigation |
|---|---|---|
| No-surface rule leaks via meta-questions | HIGH | Meta-question refusal protocol in SKILL.md |
| Portrait calcifies on early signals | HIGH | ≥3 corroborating turns required to move Inferred layer |
| Clinical vocabulary poisons internal reasoning | HIGH | Non-clinical behavioral vocabulary constraint explicit in SKILL.md |
| Inference←→generation feedback loop | HIGH | Portrait anchors on user turns only |
| Eval baseline rupture | HIGH | Freeze v1.1 rubric on existing 150; v2.0 rubric on new cases only |

---

## Deliverables

1. `SKILL.md` — Phase 0 firewall section + Phase 1 Communication Register section
2. `evals/runner/schema.py` — 3 new hard-fails + 1 new dimension
3. `evals/cases/TC-151` through `TC-165` — 15 new multi-turn eval cases for v2.0
4. This change folder as the proposal record

---

## Open questions (for post-ship v2.1 planning)

1. Does Epic 2 alone satisfy the user-experience goal, or does Phase 1 need E7+E1 in the same release?
2. Clinical vocabulary internally: strict behavioral-only (recommended) vs. clinical shorthand that never surfaces?

(Both open only for v2.1 scoping. v2.0 answers: Epic 2 alone, strict vocabulary.)
