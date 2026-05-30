# Plan — `iamhumans` v2, 2026-05-29

> Successor to [`2026-05-29-iamhumans.md`](./2026-05-29-iamhumans.md). v1.0.0 is released. This plan takes the skill from "passed verdict on 10 holdout cases" to a deeper, more cross-culturally grounded v2 — and prepares the launch that would make it the most-starred opencode-skill repo of the month.

## Goal

Two halves:

1. **Depth**: expand the reference corpus from 20 to 100 timeless books. Re-tune the skill against the wider knowledge base. Re-prove the verdict on a v2 held-out split.
2. **Reach**: ship v2 with a launch that earns attention honestly — release notes, post drafts for HN/Reddit/X, awesome-list submissions, cross-references with related projects.

The depth half is the load-bearing one. A launch without depth would be marketing the skill above its actual reach. A launch *with* depth is fair.

## North-star definition of done

| Gate | Concrete check |
|---|---|
| 100-book corpus | `references/reading-list-v2.md` lists 100 entries, all 100 `references/<slug>.md` files exist with non-stub content |
| Cross-corpus synthesis | `references/synthesis.md` ≥ 3k words, naming where traditions converge and disagree |
| Skill v2.0.0 | `SKILL.md` updated with new `## Cross-cultural sources`, `## Recognizing people`, and expanded hardest-cases — frontmatter says `version: 2.0.0` |
| Eval corpus v2 | 50 new cases (TC-101 → TC-150); 5 of them locked in `evals/cases/holdout/v2/` |
| v2 verdict | Held-out gate run on the combined 15-case holdout set returns the verbatim verdict line *and* produces no hard fails. Tagged `v2.0.0` |
| Launch | release notes, HN draft, Reddit drafts, X thread draft, awesome-list submission text, 3+ outreach drafts — all committed to the repo before any of them is sent |

## The 100 books (locked at PR #2)

Eight clusters. Counts approximate; exact list locks in [`references/reading-list-v2.md`](../../references/reading-list-v2.md).

| Cluster | Approx count | Examples |
|---|---|---|
| Communication & rhetoric | 10 | Aristotle's *Rhetoric*, *Crucial Conversations*, *Nonviolent Communication*, *Never Split the Difference*, *Talking to Strangers* |
| Personhood & philosophy of the human | 12 | *Meditations*, *Tao Te Ching*, *Analects*, *Bhagavad Gita*, *Nicomachean Ethics*, *Being and Time*, *I and Thou*, *Sapiens*, *The Denial of Death*, *The Second Sex* |
| Life, meaning, and mortality | 10 | *Man's Search for Meaning*, *On Death and Dying*, *When Breath Becomes Air*, *Letters to a Young Poet*, *Being Mortal* |
| Recognizing & evaluating people | 10 | *The 48 Laws of Power*, *The Laws of Human Nature*, *Influence*, *Surrounded by Idiots*, *Snakes in Suits* |
| Wisdom literature & life experience | 10 | *Letters from a Stoic*, *Essays of Montaigne*, *The Prophet*, *Ecclesiastes*, *The Tao of Pooh*, *The Art of Loving* |
| Full emotional spectrum | 12 | *How Emotions Are Made*, *Emotional Intelligence*, *Atlas of the Heart*, *The Language of Emotions*, *Anger* (Thich Nhat Hanh), *The Wisdom of Insecurity* |
| Cognition, decision, judgment | 10 | *Thinking Fast and Slow*, *Behave*, *The Righteous Mind*, *Antifragile*, *Superforecasting* |
| Professional fields (cross-domain) | 16 | *The Pragmatic Programmer*, *The Design of Everyday Things*, *Thinking in Systems*, *The Lean Startup*, *The Effective Executive*, *The Checklist Manifesto*, *The Art of War*, *The Prince*, *Beyond Good and Evil*, *The Republic* |
| Narrative & the human condition (fiction) | 10 | *Crime and Punishment*, *The Brothers Karamazov*, *Anna Karenina*, *Things Fall Apart*, *One Hundred Years of Solitude*, *Beloved*, *Middlemarch* |

**Overlap with v1**: 20 books are already in v1's reading list. They stay, with their existing notes intact. The 80 new books need notes authored from scratch.

**Substitution policy**: PR #2 may swap up to 5 entries if a stronger book fits a cluster better than the placeholder. Each substitution is documented in the reading list with reason.

**Non-Western and pre-modern representation**: deliberately ~35% of the list — Stoics, Confucian, Taoist, Buddhist, African (Achebe), Latin American (García Márquez), Vietnamese (Thich Nhat Hanh), Algerian (Camus, Fanon), and others. The v1 corpus was Western-modern-heavy; v2 explicitly corrects this.

## PR roadmap (v2)

| # | Branch | Change-type | Risk | Title | Status |
|---|---|---|---|---|---|
| v2-1 | `feat/v2-plan` | `change-type:docs` | `risk:low` | feat: v2 plan file | merged |
| v2-2 | `feat/v2-reading-list` | `change-type:book-notes` | `risk:low` | feat(notes): lock 108-book reading list v2 | merged |
| v2-3 | `feat/v2-notes-batch-1` | `change-type:book-notes` | `risk:low` | feat(notes): Cluster A communication & rhetoric (8 books) | merged |
| v2-4 | `feat/v2-notes-batch-2` | `change-type:book-notes` | `risk:low` | feat(notes): Cluster B personhood & philosophy (11 books) | merged |
| v2-5 | `feat/v2-notes-batch-3` | `change-type:book-notes` | `risk:low` | feat(notes): books 41–50 | planned |
| v2-6 | `feat/v2-notes-batch-4` | `change-type:book-notes` | `risk:low` | feat(notes): books 51–60 | planned |
| v2-7 | `feat/v2-notes-batch-5` | `change-type:book-notes` | `risk:low` | feat(notes): books 61–70 | planned |
| v2-8 | `feat/v2-notes-batch-6` | `change-type:book-notes` | `risk:low` | feat(notes): books 71–80 | planned |
| v2-9 | `feat/v2-notes-batch-7` | `change-type:book-notes` | `risk:low` | feat(notes): books 81–90 | planned |
| v2-10 | `feat/v2-notes-batch-8` | `change-type:book-notes` | `risk:low` | feat(notes): books 91–100 — completes corpus | planned |
| v2-11 | `feat/v2-synthesis` | `change-type:book-notes` | `risk:low` | feat(notes): cross-corpus synthesis | planned |
| v2-12 | `feat/v2-skill-tuning` | `change-type:skill-tuning` | `risk:med` | feat: SKILL.md v2.0.0 — cross-cultural, recognizing people, expanded hardest cases | planned |
| v2-13 | `feat/v2-eval-cases` | `change-type:eval-case` | `risk:low` | feat(eval): 50 new cases + v2 holdout split | planned |
| v2-14 | `feat/v2-convergence` | `change-type:lessons` + `change-type:skill-tuning` | `risk:med` | feat: convergence loop runs, lessons, final tuning | planned |
| v2-15 | `feat/v2-holdout-gate` | `change-type:eval-runner` | `risk:high` | feat(eval): v2 held-out gate (15 cases) — release v2.0.0 | planned |
| v2-16 | `feat/v2-launch` | `change-type:docs` | `risk:med` | feat(launch): release notes + HN/Reddit/X drafts + awesome-list submissions | planned |

## How v2 will not lie

The same epistemic discipline as v1:

- **Notes are still distilled from training-time exposure**, not real-time book ingestion. Every claim still marked `[paraphrase]`. Page citations still omitted. Cross-cultural and pre-modern books get extra caveats — translation choices, contested attributions, regional variants in interpretation.
- **The v2 holdout is locked at PR v2-13** and never seen by the tuning loop in PRs v2-14 or earlier.
- **The v1 holdout is reused** for the v2 verdict only because v1 has already shipped against it; using it again only re-confirms what was already proven. The *new* test is the 5-case v2 holdout.
- **The launch artifacts are honest about lineage contamination** — the same caveat that's in v1's README is in every launch post draft.
- **A FAIL v2 verdict ships v2 anyway** at the current honest version. No re-runs.

## Risk register (v2-specific)

| Risk | Mitigation |
|---|---|
| 80 book notes × ~1.5k words = ~120k words is many session-hours of generation | PRs are atomic per 10-book batch; the project can pause and resume between any two batches without breaking the harness |
| Cross-cultural books increase the chance of paraphrase-error or contested-interpretation slips | Each book's `## Disagreements and caveats` section gets *more* attention than v1's, especially for pre-modern and non-Western books — translation issues, multiple textual lineages, contested authorship |
| Synthesis PR might reduce to bullet-point summarization rather than genuine cross-traditional analysis | Force structural constraints in `synthesis.md`: each principle must cite ≥3 books, ≥1 of which is from a different cluster |
| Re-tuning SKILL.md against 100 books might bloat the prompt past usefulness | `SKILL.md` stays compact (~250 lines target); the book notes are *retrievable knowledge base*, not always-loaded context |
| Launch posts might drift into hype | Every launch artifact is committed to the repo for inspection before any of it is sent; the same anti-AI-tells rules apply to launch writing |

## Honest realism about session budget

The v1 work spanned ~13 PRs in one session — almost entirely prose generation. v2 is approximately *5× more* prose work (100 books vs. 20, plus synthesis, plus 50 more eval cases, plus convergence runs, plus launch artifacts).

A single session realistically completes:
- Plan + locked reading list + first 1–2 book-notes batches.

A small follow-on series of sessions completes:
- The remaining 6–7 book-notes batches.

The convergence loop, the actual v2 verdict run, and the launch require additional staging. The plan executes against `main` regardless; what's actually in flight at any given moment is reflected in the PR statuses above.

## Execution log

- 2026-05-29 — v1.0.0 released (PR #12 of v1 plan). v2 plan opened (PR #14, merged).
- 2026-05-29 — v2-2 merged (PR #15): 108-book locked reading list, 9 clusters, ~35% non-Western/pre-modern representation. lint extended to enforce v2 exact count.
- 2026-05-29 — v2-3 merged (PR #16): Cluster A communication & rhetoric, 8 long-form notes (~10.7k words). Aristotle, Stone/Patton/Heen, Voss, Gladwell, Strunk & White, Zinsser, Heath brothers, Luntz.
- 2026-05-29 — v2-4 merged (PR #17): Cluster B personhood & philosophy of the human, 11 long-form notes (~14.7k words). Marcus Aurelius, Lao Tzu, Confucius, Krishna-Arjuna dialogue, Aristotle (Ethics), Heidegger, Buber, Becker, Beauvoir, Fanon, Pascal. Cross-cultural and pre-modern depth that v1's Western-modern corpus lacked.
- **Cumulative state after this session**: 39 of 108 books complete (20 from v1 + 19 new in v2 batches 1 and 2). ~25.4k words of new reference content shipped this session. 69 books remain.
- **Honestly staged for follow-on sessions** (in plan-roadmap order):
  - v2-5 through v2-10: 6 book-notes batches × ~12 books each = 69 remaining book notes, ~85-100k words at current per-batch density
  - v2-11: cross-corpus synthesis (~3-5k words)
  - v2-12: SKILL.md v2.0.0 tuning (cross-cultural sources section, expanded hardest cases, Recognizing People subsection — informed by the full 108-book corpus, not just the partial)
  - v2-13: 50 new eval cases + v2 holdout split
  - v2-14: convergence runs (machinery exists from v1 PR #11; actual oracle invocation budget needed for the 90→135-case main pool)
  - v2-15: held-out v2 verdict gate (15 combined cases — 10 v1 + 5 v2)
  - v2-16: launch artifacts (release notes, HN/Reddit/X drafts, awesome-list submissions, outreach)
- This pace matches the budget realism documented above ("A single session realistically completes plan + locked reading list + first 1–2 book-notes batches"). The remaining work is real and should be scheduled across a series of follow-on sessions rather than degraded into one.
- 2026-05-30 — v2-install merged (PR #19): `docs/INSTALL.md` documenting local-symlink install procedure for `~/.opencode/skills/iamhumans/`.
- 2026-05-30 — **v2-pareto-sample-1 opened (PR #20)**: first Pareto-tuning iteration. 15 stratified cases (seed=1), aggregate 93.27/100, 14/15 PASS, 0 hard-fail under v1.0.0. Identified 5 Pareto-ranked failure patterns; applied 5 surgical SKILL.md tunings (stillness exception, anti-epigram, length-to-affect table, permit-no-closer, low-pressure resource carve-out). Added explicit `## Known weaknesses` section. SKILL.md → v1.1.0. TC-025 retune verified 70 → 96. New tooling: `evals/runner/stratified_sample.py` + `evals/runner/pareto_runner.py` (emit/aggregate subcommands). Full evidence in `evals/runs/20260530-050323-pareto-sample-1/`. Honest framing: pilot scope, not the 1000 cases originally requested; 85 cases from v1 pool remain unrun.
- **Cumulative state after PR #20**: SKILL.md released at v1.1.0. 39/108 books still — Pareto tuning is orthogonal to the book-notes ladder and did not touch the corpus. Tooling is now in place for subsequent Pareto-tuning batches to plug straight in.
- **Newly staged for follow-on sessions** (added by this session):
  - v2-pareto-sample-2: re-run all 15 v1.1.0 cases against v1.1.0 to confirm no regressions on the 14 prior PASSes.
  - v2-pareto-sample-3: fresh 15-case sample (held-out from sample-1) to detect unseen patterns.
  - v2-cross-family-judge: cross-family judge run (GPT or Gemini evaluator) for lineage-independent verdict.
  - v2-multi-turn: multi-turn case battery — current corpus is single-turn only.
