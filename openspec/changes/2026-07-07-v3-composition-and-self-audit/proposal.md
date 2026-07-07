# OpenSpec Proposal: iamhumans v3.0 — Composition Mode + Self-Audit Engine

**Change ID:** 2026-07-07-v3-composition-and-self-audit
**Status:** proposed
**Version target:** 3.0.0
**Date:** 2026-07-07
**Cross-reference:** Nous Research Hermes *creative-humanizer* skill (Wikipedia "Signs of AI writing" lineage)

---

## Summary

iamhumans today is a **conversational-presence** skill: it interprets a live human interlocutor (Running Portrait, affect read) and composes emotionally attuned dialogue (prosody, register, 16 modules, cultural clusters). It is excellent at *being* a human in conversation, and it explicitly **declines** to help when the task is "de-AI this essay / email / post."

The Hermes *creative-humanizer* skill occupies exactly that declined space: it takes AI-drafted **prose** and strips 29 statistical AI tells, then runs a **dual-phase self-audit** ("what makes this obviously AI-generated? → now fix it") and calibrates to a user's **voice sample**, all under one governing ethos: **add soul, don't just strip patterns.**

v3.0 fuses the two. It adds a second operating mode and — more importantly — lifts *creative-humanizer*'s self-audit loop into a **shared verification engine that runs before every reply in both modes.** This is the single biggest capability iamhumans is missing: it has ~250 rules but **no pre-send check that it followed them.**

---

## Problem

Three concrete gaps, in priority order:

1. **No verification pass.** iamhumans is a large ruleset applied in one forward pass. Nothing re-reads the drafted reply and asks "did I just do a thing on the avoid-list?" The Known Weaknesses section admits residual em-dash chains, epigrammatic triplets, and length miscalibration *persist despite explicit bans* — the classic signature of rules without a checking step.

2. **Incomplete AI-tell taxonomy.** The current `Anti-AI tells (avoid)` table (~22 rows) is conversation-specific (sycophancy, "I'm here for you", clinical labels). It does **not** cover the structural/lexical tells that dominate *written* output: copula avoidance ("serves as / stands as / boasts"), negative parallelism ("it's not just X, it's Y"), rule-of-three forcing, false ranges ("from X to Y"), significance inflation ("pivotal moment", "enduring testament"), signposting ("let's dive in"), em-dash/boldface/title-case/emoji density, filler ("in order to", "due to the fact that"), hedging stacks, generic uplift conclusions ("the future looks bright").

3. **No composition mode and no voice calibration.** iamhumans refuses text-editing tasks by design ("Do not load when the user wants … structured output"). But "make this sound less like AI" is one of the most common real humanization requests, and it is squarely on-brand. The skill also has no way to match a *specific person's* written voice from a sample — only per-turn typographic mirroring.

---

## Goal

Turn iamhumans from a **single-mode conversational skill** into a **two-mode humanization skill with a shared self-audit engine.**

### In scope (v3.0.0)

- **Epic A — Dual-mode router.** A load-time decision: Mode A (Conversational presence, existing) vs. Mode B (Composition / de-AI, new). Modes share the taxonomy and the audit engine; they differ in input (a live turn vs. a supplied draft) and output shape.
- **Epic B — AI-tell taxonomy.** A structured `references/ai-tells.md` importing and de-duplicating the 29-pattern catalog against the existing conversational table. Single source of truth both modes cite.
- **Epic C — Self-Audit Engine (the keystone).** A mandatory internal dual-phase pass before *every* finalized reply, both modes: (1) "What in this draft reads as AI?" → enumerate tells against the taxonomy; (2) "Rewrite so it doesn't." Internal only — never surfaced, consistent with the Phase 0 firewall.
- **Epic D — Voice calibration.** When a writing sample is supplied (Mode B) or a stable voice signal accrues across turns (Mode A, via the existing Running Portrait), extract a voice fingerprint (sentence-length rhythm, lexical level, paragraph openers, punctuation habits, recurring phrases, transitions) and match it — not just strip tells.
- **Epic E — "Add soul" gate.** A second audit question that fails pattern-clean-but-soulless output: uniform sentence length, zero opinion, zero acknowledged uncertainty, no first person where fitting, no humor/edge. Pattern-clean is necessary, not sufficient.
- **Epic F — Evals + schema.** New hard-fails, new dimensions, new Mode-B eval cases, source-hierarchy + versioning updates.

### Out of scope (tracked for later)

- Automated AI-tell *scoring* tooling (a linter that counts em-dashes/tells) — v3.1 candidate; v3.0 keeps the audit judgment-based to stay model-portable.
- Multi-document / batch de-AI over a folder — v3.1.
- Non-text media humanization — out of skill charter.

---

## Why now / why this fusion

- The two skills are **complementary, not redundant.** iamhumans owns *presence*; creative-humanizer owns *prose de-slop*. Neither covers the other's ground. Merging yields one skill that humanizes both what the model *says live* and what it *drafts on request*.
- The **self-audit loop is portable across both modes** and directly attacks iamhumans' three *Open* known weaknesses (mannerism residue, length calibration, unverified rule-following). This is the highest-leverage single addition available.
- It keeps iamhumans' distinctive strength — **soul over sterility** — as the governing constraint, so v3.0 does not regress into a mechanical de-tell filter.

---

## Success gate

- **Behavioral, measurable on the existing Oracle rubric.** Two new gates:
  - *Mode A regression gate:* the full frozen corpus (TC-001–TC-4xx) holds — no score regression, no new hard-fails introduced by the audit pass.
  - *Mode B acceptance gate:* new Mode-B cases (de-AI a supplied draft) pass on the new `ai_tell_density` + `voice_match` + `retains_soul` dimensions, with the before/after showing tell removal **without** soul loss.
- **Held-out verdict** re-run on the 10 locked cases must still return *"You are same as 100% real humans."* with zero hard-fails after the audit pass is wired in (proves the engine helps, never hurts, Mode A).

---

## Risks

| Risk | Mitigation |
|---|---|
| Self-audit over-sanitizes → sterile, soulless replies | Epic E "add soul" gate is part of the *same* pass; audit is two-sided by construction. |
| Audit adds latency / verbosity | Engine is internal and bounded; it revises the draft, it does not narrate. Firewall bans surfacing it. |
| Mode router misfires (treats a live vent as a de-AI task) | Router defaults to Mode A on any affective/relational signal; Mode B requires an explicit "edit this text" shape. Ambiguity → Mode A (the safe, warm default). |
| Taxonomy import drags in Wikipedia-register rules that clash with iamhumans' warmth | Epic B de-duplicates and reconciles; conversational table wins on any conflict in Mode A. |
| Corpus regression from the new pass | Mode A regression gate is a hard release blocker. |

---

## Deliverables

1. `SKILL.md` — new `## Operating modes` router; new `## Self-audit pass` section; taxonomy pointer; voice-calibration subsection; updated Source hierarchy + Versioning.
2. `references/ai-tells.md` — the reconciled 29-pattern catalog.
3. `evals/runner/schema.py` — new hard-fails + dimensions.
4. New Mode-B eval cases + a Mode-A regression run.
5. `design.md`, `tasks.md` (this change).
