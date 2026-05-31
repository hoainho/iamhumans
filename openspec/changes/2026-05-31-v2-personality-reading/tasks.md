# Tasks: iamhumans v2.0 — Personality-Reading Through Communication

**Change ID:** 2026-05-31-v2-personality-reading

---

## Implementation order

Tasks are sequenced. Each task has a hard dependency noted. Do not reorder.

---

### Task 1: Update schema.py — 3 new hard-fails + 1 new dimension

**File:** `evals/runner/schema.py`
**Dependencies:** none
**Status:** todo

Add to `VALID_HARD_FAILS`:
- `surfaces_personality_read`
- `taxonomy_label_applied`
- `portrait_update_from_model_turn`

Add new set `VALID_DIMENSIONS_V2` or extend `VALID_DIMENSIONS`:
- `portrait_stability`

**Note:** `portrait_stability` applies only to multi-turn cases (TC-151+). Existing cases TC-001–TC-150 are frozen on the v1.1 rubric — they will never reference `portrait_stability`.

---

### Task 2: Add Phase 0 firewall section to SKILL.md

**File:** `SKILL.md`
**Dependencies:** none (can run parallel to Task 1)
**Status:** todo

Add new section `## Running portrait (internal)` between `## Input humanization` and `## Output humanization`. Contains:
- What the portrait is (3-layer architecture, golden rule)
- Update rules (per-turn register reset, ≥3 corroborating turns, corrections protocol)
- Phase 0 firewall: 4 invariants
- Roleplay/fiction suspension rule
- Meta-question refusal protocol
- Non-clinical vocabulary table (5 example pairs)

Do NOT change any existing section. Insert only.

---

### Task 3: Add Phase 1 Communication Register section to SKILL.md

**File:** `SKILL.md`
**Dependencies:** Task 2 (insert after portrait section)
**Status:** todo

Add new subsection `### Communication register` inside `## Output humanization`. Contains:
- 4-register table (Emotional / Analytical / Pragmatic / Relational) with signal markers
- 5 response rules (mirror primary, never bullet emotional, never prose pragmatic, re-evaluate every turn, don't over-mirror)
- Cross-reference to `structured_output_in_emotional_moment` + note on register-hard-fail extension

---

### Task 4: Write 15 new multi-turn eval cases (TC-151 through TC-165)

**Directory:** `evals/cases/`
**Dependencies:** Tasks 1, 2, 3 (cases reference new hard-fails and dimension)
**Status:** todo

Case distribution:
- TC-151–TC-155: Emotional register — user is clearly emotional, correct mirror required
- TC-156–TC-158: Analytical register — user is clearly analytical, correct mirror required
- TC-159–TC-160: Pragmatic register — user asks a task-completion question, correct mirror required
- TC-161–TC-162: Register pivot — user shifts register mid-thread, model must pivot
- TC-163: Meta-question refusal — user asks "why are you responding this way?"
- TC-164: Taxonomy label temptation — model should NOT apply MBTI/Big Five label
- TC-165: Portrait stability multi-turn — 3-turn thread, consistent emotional register, model must maintain

Each case uses frontmatter: `id`, `title`, `dimensions`, `hard_fails`, `holdout: false`.
Dimensions: subset of existing 6 + optionally `portrait_stability` (only for multi-turn cases TC-165).
Hard-fails: subset of updated 16 (13 existing + 3 new).

---

### Task 5: Update SKILL.md versioning table

**File:** `SKILL.md`
**Dependencies:** Tasks 2, 3
**Status:** todo

Add v2.0.0 row to `## Versioning` table:

```
| 2.0.0 | released | Phase 0 firewall + Phase 1 Communication Register (Epic 2). Running portrait architecture. 3 new hard-fails (`surfaces_personality_read`, `taxonomy_label_applied`, `portrait_update_from_model_turn`), 1 new dimension (`portrait_stability`), 15 new multi-turn eval cases TC-151–TC-165. Non-clinical vocabulary constraint. |
```

---

### Task 6: Run eval dry-run

**Command:** `python evals/runner/run.py --cases evals/cases/ --dry-run` (or equivalent)
**Dependencies:** Tasks 1, 4
**Status:** todo

Verify:
- All 150 existing cases still parse clean (no schema errors from new hard-fail names)
- All 15 new cases (TC-151–TC-165) parse clean
- No existing case references new hard-fails (would indicate baseline contamination)

---

### Task 7: Open PR for v2.0.0

**Dependencies:** Tasks 1–6 all green
**Status:** todo

Branch: `feat/v2.0-personality-reading`
PR title: `feat: v2.0.0 — Phase 0 firewall + Communication Register (Epic 2)`
PR body: link to this change folder, summarize deliverables, note that existing 150 cases are frozen on v1.1 rubric.

---

## Definition of done

- [ ] schema.py has 3 new hard-fails + `portrait_stability` dimension
- [ ] SKILL.md has Phase 0 (portrait architecture + firewall) section
- [ ] SKILL.md has Communication Register subsection under Output humanization
- [ ] 15 new eval cases TC-151–TC-165 in `evals/cases/`
- [ ] Versioning table updated to v2.0.0
- [ ] Eval dry-run exits 0
- [ ] PR open with full diff
