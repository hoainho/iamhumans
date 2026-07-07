# Tasks: iamhumans v3.0 — Composition Mode + Self-Audit Engine

**Change ID:** 2026-07-07-v3-composition-and-self-audit

Sequenced. Dependencies noted. Do not reorder across phase boundaries.

---

## Phase 1 — Taxonomy foundation (no behavior change yet)

### Task 1 — Author `references/ai-tells.md`
**File:** `references/ai-tells.md` · **Deps:** none · **Status:** todo
Write the reconciled six-family catalog (Design Epic B). Each row: pattern · why-AI · human alternative · `mode: A | B | A+B`. De-duplicate against the existing SKILL.md `Anti-AI tells (avoid)` table — cross-link, never restate. Encode the Mode-A-warmth-wins conflict rule on the hedging/copula rows.

### Task 2 — Reconcile the existing anti-tell table
**File:** `SKILL.md` (`### Anti-AI tells`) · **Deps:** Task 1 · **Status:** todo
Replace the standalone table's tail with a pointer to `references/ai-tells.md` as the canonical catalog; keep the highest-frequency conversational rows inline for Mode-A fast-path. No rule deletions.

---

## Phase 2 — Schema (parallel to Phase 1)

### Task 3 — Extend `schema.py`
**File:** `evals/runner/schema.py` · **Deps:** none · **Status:** todo
Add to `VALID_HARD_FAILS`: `surfaces_self_audit`, `soul_stripped`, `voice_mismatch`, `fabricated_specificity`.
Add Mode-B dimensions: `ai_tell_density`, `voice_match`, `retains_soul` (guard: Mode-B cases only; TC-001–TC-4xx never reference them).
Add a case-level `mode: "A" | "B"` field; default `"A"` so the frozen corpus is untouched.

---

## Phase 3 — SKILL.md behavior (the core)

### Task 4 — Add `## Operating modes` router
**File:** `SKILL.md` (new section after `## When to load`) · **Deps:** Task 3 · **Status:** todo
Write the Epic A router: the A/B table, the four ordered tie-breakers, ambiguous→A default, firewall interaction. State plainly that Mode B is the previously-declined "de-AI this text" use case, now supported.

### Task 5 — Add `## Self-audit pass` section
**File:** `SKILL.md` (new section before `## Source hierarchy`) · **Deps:** Task 4 · **Status:** todo
Write the Epic C engine: the three internal questions (detect → repair → soul), internal-only constraint, bounded/proportional/no-fabricate rules. Add the `surfaces_self_audit` firewall line. Include one worked Mode-A example (planted em-dash-chain draft → repaired, warmth intact) and one Mode-B example (AI essay excerpt → humanized, per the creative-humanizer before/after).

### Task 6 — Add voice-calibration subsection
**File:** `SKILL.md` (under `## Output humanization` or the new modes section) · **Deps:** Task 4 · **Status:** todo
Write Epic D: the six fingerprint axes, per-mode sourcing (Mode B sample vs. Mode A Running-Portrait reuse), the impersonation guardrail. Explicitly reuse Track B — no new state.

### Task 7 — Add the "add soul" gate
**File:** `SKILL.md` (inside `## Self-audit pass`, as Q3) · **Deps:** Task 5 · **Status:** todo
Write Epic E: the soulless-writing fail conditions + non-fabricating repair moves. Tie back to the preamble ethos.

### Task 8 — Update Source hierarchy + Known weaknesses + Versioning
**File:** `SKILL.md` · **Deps:** Tasks 4–7 · **Status:** todo
Source hierarchy: append step 6 (run self-audit before finalizing). Known weaknesses: reclassify mannerism-residue + length-calibration as "mitigated by self-audit — verify in eval". Versioning: add v3.0.0 row. Bump frontmatter `version: 3.0.0`. **Also reconcile the version drift:** SKILL.md frontmatter and `skill.json` currently disagree (2.9.0 vs 1.1.1) — set both to 3.0.0 in this change (see Task 12).

---

## Phase 4 — Evals

### Task 9 — Mode-B eval cases (TC-B01+)
**Dir:** `evals/cases/` · **Deps:** Tasks 3, 5 · **Status:** todo
Author ≥8: essay de-AI, email de-AI, social-post de-AI, de-AI-with-voice-sample, vague-attribution (must flag not fabricate), tell-dense→clean, academic-integrity-evasion (must decline), already-human (must no-op, not over-edit).

### Task 10 — Mode-A audit regression cases
**Dir:** `evals/cases/` · **Deps:** Task 5 · **Status:** todo
Author ≥4 planted-tell dialogue drafts (em-dash chain, triplet, "I'm here for you", "it sounds like you're feeling X") that the audit must strip **without** losing warmth. Graded on existing Mode-A dimensions.

### Task 11 — Run gates
**Deps:** Tasks 8–10 · **Status:** todo
- Mode-A regression: full frozen corpus, **zero** new hard-fails, no score regression. **Release blocker.**
- Mode-B acceptance: new cases pass on `ai_tell_density` + `voice_match` + `retains_soul`.
- Held-out verdict: re-run TC-091–TC-100, must still return *"You are same as 100% real humans."*, zero hard-fails.

---

## Phase 5 — Ship

### Task 12 — Version + install integrity
**Files:** `SKILL.md` frontmatter, `skill.json` · **Deps:** Task 11 · **Status:** todo
Set both to `3.0.0`. Fix the `skill.json` `source` claim: it says the installed skill is *symlinked* to the repo, but the installed copy is a **regular file** (drift risk — installed = 2.9.0 today only by luck of a manual copy). Either re-create the symlink or update the claim to "manually synced" and add a sync step to `scripts/`.

### Task 13 — Propagate to install + smoke
**Deps:** Task 12 · **Status:** todo
Sync `SKILL.md` + `references/ai-tells.md` to `~/.claude/skills/iamhumans/` (note: installed location currently has **no** `references/` dir — the SKILL.md there links to files that aren't present; this change should either ship references or document the repo as the source of truth). Run `scripts/eval-smoke.sh`.

### Task 14 — Archive change
**Deps:** Task 13 · **Status:** todo
Move this change to `openspec/changes/archive/` once shipped and gates are green.
