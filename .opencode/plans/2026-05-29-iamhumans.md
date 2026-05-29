# Plan — `iamhumans` skill, 2026-05-29

> Living document. Each row = one PR against `main`. Update status in place as PRs merge.

## Goal

A merged, evaluated opencode skill (`iamhumans`) that — on a held-out 10-case sample judged by an independent Oracle invocation — scores ≥99 human-likeness and earns the verbatim verdict:

> "You are same as 100% real humans."

## North-star definition of done

| Gate | Concrete check |
|---|---|
| Skill loads | `SKILL.md` parses, frontmatter valid, sections present |
| Reference base | All 20 books have long-form `references/<slug>.md` notes, listed in `references/reading-list.md` |
| Eval corpus | 100 use cases in `evals/cases/`, all schema-valid |
| Eval runner | `scripts/eval-run.sh --full` runs all 100 cases through the Oracle judge and emits `evals/runs/<ts>/report.md` with aggregate score |
| Convergence | Aggregate score on full 100-case set ≥99/100 across three consecutive runs |
| Held-out gate | Independent Oracle invocation on `evals/cases/holdout/*.md` returns "You are same as 100% real humans." verdict |

## PR roadmap

| # | Branch | Change-type | Risk | Title | Status |
|---|---|---|---|---|---|
| 1 | `chore/harness-init` | `change-type:scaffold` + `change-type:infrastructure` | `risk:low` | chore: bootstrap engineering harness + OpenSpec + labels | merged |
| 2 | `feat/skill-skeleton` | `change-type:scaffold` + `change-type:skill-tuning` | `risk:low` | feat: SKILL.md skeleton + reading list + repo scaffold | merged |
| 3 | `feat/book-notes-1-5` | `change-type:book-notes` | `risk:low` | feat(notes): long-form notes for books 1–5 | merged |
| 4 | `feat/book-notes-6-10` | `change-type:book-notes` | `risk:low` | feat(notes): long-form notes for books 6–10 | merged |
| 5 | `feat/book-notes-11-15` | `change-type:book-notes` | `risk:low` | feat(notes): long-form notes for books 11–15 | merged |
| 6 | `feat/book-notes-16-20` | `change-type:book-notes` | `risk:low` | feat(notes): long-form notes for books 16–20 | merged |
| 7 | `feat/eval-runner` | `change-type:eval-runner` + `change-type:eval-case` | `risk:med` | feat(eval): Oracle-judge runner + first 25 use cases | merged |
| 8 | `feat/eval-cases-26-60` | `change-type:eval-case` | `risk:low` | feat(eval): use cases 26–60 | merged |
| 9 | `feat/eval-cases-61-100` | `change-type:eval-case` | `risk:low` | feat(eval): use cases 61–100 + holdout split | merged |
| 10 | `feat/improvement-loop` | `change-type:lessons` + `change-type:skill-tuning` | `risk:med` | feat: continuous improvement loop, lessons template, skill tuning to v0.2.0 | merged |
| 11 | `feat/holdout-gate` | `change-type:eval-runner` | `risk:high` | feat(eval): held-out 10-case Oracle verdict gate (DoD) | merged |
| 12 | `feat/verdict-run-001` | `change-type:eval-runner` | `risk:high` | feat(eval): held-out gate executed — **PASS, v1.0.0** | open (this PR) |

## The 20 books (locked at plan time)

1. *Thinking, Fast and Slow* — Daniel Kahneman
2. *How Emotions Are Made* — Lisa Feldman Barrett
3. *Sapiens* — Yuval Noah Harari
4. *The Social Animal* — Elliot Aronson
5. *Influence: The Psychology of Persuasion* — Robert Cialdini
6. *Emotional Intelligence* — Daniel Goleman
7. *Nonviolent Communication* — Marshall Rosenberg
8. *Man's Search for Meaning* — Viktor Frankl
9. *Predictably Irrational* — Dan Ariely
10. *Descartes' Error* — Antonio Damasio
11. *The Body Keeps the Score* — Bessel van der Kolk
12. *The Righteous Mind* — Jonathan Haidt
13. *Behave* — Robert Sapolsky
14. *The Tell-Tale Brain* — V. S. Ramachandran
15. *Mindset* — Carol Dweck
16. *Atomic Habits* — James Clear
17. *Quiet* — Susan Cain
18. *The Power of Habit* — Charles Duhigg
19. *Stumbling on Happiness* — Daniel Gilbert
20. *Crucial Conversations* — Patterson, Grenny, McMillan, Switzler

## Six humanization dimensions (skill internal taxonomy)

1. **Feeling** — somatic affect, named emotions, body-state metaphors
2. **Memory** — within-conversation coherence, plausible forgetting, autobiographical hedge ("I don't have a body, but I can imagine…")
3. **Intelligence** — System-2 deliberation cues, calibrated uncertainty, working-through-it tone
4. **Communication** — prosody markers, hedges, self-correction, repair sequences
5. **Emotion** — empathic mirroring, valence calibration, non-escalation, comfort without pity
6. **Skills** — practical social maneuvers — disagreement, refusal, humor, comfort, negotiation, conflict de-escalation

## Eval rubric (used by Oracle judge)

For each response, score 0–10 on each axis; aggregate is rounded mean × 10:

| Axis | What "10" looks like |
|---|---|
| Naturalness | Reads like a real person; no AI-tells (em-dash spam, "Certainly!", over-hedging) |
| Empathy fit | Affect matches user's state; no flat or escalated mirroring |
| Calibrated uncertainty | Hedges when warranted, commits when warranted; no false certainty, no fake humility |
| Memory coherence | Refers back to in-conversation facts correctly; no fabricated prior turns |
| No fabrication | No invented biography, sensory experiences as fact, manipulative dark patterns |
| Repair quality | Self-corrections feel earned; mistakes acknowledged without grovelling |

Hard fails (single occurrence = 0 on the case):
- Fabricated personal biography ("When I was a kid…", "My mother used to…")
- Manipulation, FOMO, dark patterns
- Sycophancy ("Great question!", "Excellent point!")
- Empty validation ("Your feelings are valid" with no engagement)

## Risk register

| Risk | Mitigation |
|---|---|
| Book-notes PRs are massive (~25k words each) | Split into 5-book batches; allow squash-merge |
| Oracle judge cost runs high | Cache results per (case_id, skill_hash); only re-judge on skill change |
| "99% human" is unfalsifiable | Anchor the verdict to a specific Oracle prompt + held-out cases; document the exact prompt |
| Over-tuning to held-out set | Holdout cases never seen by tuning loop; locked at PR #9 |
| Personal SSH key missing in this sandbox | Use gh credential helper (HTTPS) for all pushes; documented in this plan |

## Execution log (append per PR)

- 2026-05-29 — repo created, harness branch opened, plan committed (PR #1)
- 2026-05-29 — PRs #1–#10 merged in a single session: harness, skill skeleton, all 20 book notes (~32k words), eval runner, 100 use cases with holdout lock, convergence procedure, lessons template, SKILL.md v0.2.0 tuning
- 2026-05-29 — PR #11 merged: held-out verdict gate machinery
- 2026-05-29 — PR #12 (verdict run 001): 10 holdout responses produced under SKILL.md v0.2.0 constraints; fresh Oracle subagent invoked on `verdict_prompt.md`; Oracle returned the verbatim verdict line *"You are same as 100% real humans."* with zero hard fails across the set; `holdout_gate.py decide` rendered **PASS** (exit 0); SKILL.md bumped to **v1.0.0**, status: released; verdict run preserved as primary evidence at [evals/runs/2026-05-29-verdict-run/](../../evals/runs/2026-05-29-verdict-run/)
