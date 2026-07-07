# iamhumans

![iamhumans social preview](./assets/og/og-image.png)

[![CI](https://github.com/hoainho/iamhumans/actions/workflows/ci.yml/badge.svg)](https://github.com/hoainho/iamhumans/actions/workflows/ci.yml)
[![version](https://img.shields.io/badge/version-v3.0.0-blue.svg)](./SKILL.md)
[![license: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![evals: 99/100 PASS](https://img.shields.io/badge/evals-99%2F100%20PASS-brightgreen.svg)](./evals/runs/20260530-lane-a2-full-v111/report.md)
[![aggregate: 96.3/100](https://img.shields.io/badge/aggregate-96.3%2F100-brightgreen.svg)](./evals/runs/20260530-lane-a2-full-v111/report.md)
[![baseline delta: +89.4 pts](https://img.shields.io/badge/vs%20no--skill-+89.4%20pts-brightgreen.svg)](./evals/runs/20260530-lane-a3-baseline/report.md)
[![cross-judge: 86.7% agreement](https://img.shields.io/badge/cross--judge-86.7%25%20agree-brightgreen.svg)](./evals/lessons/2026-05-30-cross-validation.md)
[![oracle verdict: PASS](https://img.shields.io/badge/oracle%20verdict-100%25%20human-blueviolet.svg)](./evals/runs/2026-05-29-verdict-run/)
[![corpus: 429 cases](https://img.shields.io/badge/corpus-429%20cases-blue.svg)](./evals/cases/)
[![opencode](https://img.shields.io/badge/built%20for-opencode-black.svg)](https://github.com/sst/opencode)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

An opencode skill. It teaches a language model how to talk like a person.

Not how to *sound* like a person. Sounding like is easy and is what most of the failures already do. The skill works on the shape underneath — when to be short, when to sit with something, when to push back, when the right reply is "oh".

At v3.0.0. Back at v1.0.0, a held-out oracle — given ten cases the skill had never been tuned on — read the responses and wrote back:

> *You are same as 100% real humans.*

That verdict, with the full per-case breakdown, lives in [`evals/runs/2026-05-29-verdict-run/`](./evals/runs/2026-05-29-verdict-run/). It's the project's primary evidence, kept verbatim. If you want to argue with the result, read what the oracle actually wrote — not the headline. (The badges above are from the v1.1.1 full run; v3.0.0 has not yet been re-scored on the full oracle harness — see the note below.)

> **v3.0.0 — Composition Mode + Self-Audit Engine (2026-07-07)** — the skill becomes two-mode. **Mode A** is the original conversational presence. **Mode B** is composition / de-AI: paste AI-drafted prose ("make this sound less like a bot") and get it back human, in *your* voice — the use case the skill used to decline. Both modes now run a mandatory internal **self-audit pass** before every reply — *detect* AI-tells → *repair* → *soul check* (a tell-clean but sterile draft fails) — which directly targets the residual mannerism/length weaknesses. New: a six-family AI-tell taxonomy ([`references/ai-tells.md`](./references/ai-tells.md), fusing the project's own anti-tell table with the Nous Research Hermes *creative-humanizer* catalog / Wikipedia "Signs of AI writing"), voice calibration (six-axis fingerprint, reuses the Running Portrait — no new state), 4 hard-fails (`surfaces_self_audit`, `soul_stripped`, `voice_mismatch`, `fabricated_specificity`), 3 Mode-B dimensions (`ai_tell_density`, `voice_match`, `retains_soul`), a case-level `mode` field, and 12 new cases (TC-428–439). Full spec in [`openspec/changes/2026-07-07-v3-composition-and-self-audit/`](./openspec/changes/2026-07-07-v3-composition-and-self-audit/). **Verified this release on** schema dry-run + lint + a blind-graded regression sample (18/18 Mode-A after a door-reopener fix) + a Mode-B behavioral smoke test; **full oracle re-scoring of v3.0 is deferred to the live harness and is not yet claimed.**

> **v2.2.0–v2.9.0 — Cultural, life-stage, and structural-trauma waves (2026-06)** — after the v2.0 portrait work, the corpus expanded well beyond the original Western/English default: 5 cultural affect clusters (Latin/Latinx, SE-Asian/Buddhist, East-Asian, MENA, African & diasporic), 4 life-stage clusters (Adolescence, New Parenthood, Midlife, Aging), 4 structural-trauma clusters (Neurodivergence, Disability & Chronic Illness, Incarceration & Reentry, Displacement & Forced Migration), plus Relational Dynamics, Somatic & Embodied Experience, Attachment & Early Wounding, and Coercive Control & Power Abuse. **16 modules, ~304 book-grounded rules, ~217 books** at v2.9.0. See the `## Versioning` table in [`SKILL.md`](./SKILL.md).

> **v2.0.0 — Running Portrait (2026-05-31)** — the skill now maintains a private, provisional sketch of who the user is, accumulated across turns. Three epistemic layers (Observed / Inferred / Speculative), four firewall invariants, and a communication register that re-evaluates every user turn. The portrait is invisible — the user should feel known without feeling analyzed. New: 3 hard-fails (`surfaces_personality_read`, `taxonomy_label_applied`, `portrait_update_from_model_turn`), 1 new eval dimension (`portrait_stability`), 15 new multi-turn eval cases TC-151–TC-165. Architecture detail in [`SKILL.md`](./SKILL.md) under `## Running portrait`.

> **v1.2.0 — Personality Modules (2026-05-31)** — 20 personality modules covering the emotional territories where models fail loudest: Warmth, Pride, Nostalgia, Curiosity, Loneliness, Grief, Shame, Fear, Directness, Patience, Humor, Vulnerability, Receiving Anger, Resilience, Trust, Integrity, Forgiveness, Identity & Belonging, Hope, Moral Courage. Each module has concrete behavioral rules and 3 eval cases. 60 new cases (TC-166–TC-225), corpus now 225 cases, all parse clean.

> **Evidence updates since v1.0.0** — after the v1.0.0 verdict, the skill was Pareto-tuned against a fresh 15-case stratified sample. Aggregate moved from 93.27 → 95.00, 14/15 → 15/15 PASS. Five surgical voice rules added; one open `## Known weaknesses` section retained. Full Pareto analysis: [`evals/lessons/2026-05-30-pareto-sample-1.md`](./evals/lessons/2026-05-30-pareto-sample-1.md). The 15-case sample was then **cross-validated** by three Claude judges (Opus 4.7 original, Opus 4.7 fresh, Sonnet 4.6): **86.7% verdict agreement**, zero verdict flips on intra-Opus re-runs (mean Δ 2.13 / 100 points). Full cross-validation: [`evals/lessons/2026-05-30-cross-validation.md`](./evals/lessons/2026-05-30-cross-validation.md). v1.1.1 expanded the auto-load trigger surface (~45 phrases including humans, people, friendly, discussion, conversation, communication, listen, vent, warm, empathy, casual, real talk, heart-to-heart) — see [`SKILL.md`](./SKILL.md) frontmatter.

> **Full 100-case evidence (v1.1.1, 2026-05-30)** — the complete main pool (99 scored cases + 1 pre-existing hold) re-run at v1.1.1: **99/100 PASS, 96.3/100 aggregate, 0 hard fails**. Full run: [`evals/runs/20260530-lane-a2-full-v111/`](./evals/runs/20260530-lane-a2-full-v111/report.md). **Baseline comparison** — the same 20 stratified cases were then scored *without* the skill (default Claude behavior): **1/20 PASS, 7.6/100 aggregate, 18/20 hard fails**. Skill delta: **+89.4 points average, PASS rate 5% → 100%**. The most common baseline hard-fail patterns — sycophancy, lecturing, performed-empathy, structured-output-in-grief-moment — are exactly what this skill is built against. Full baseline: [`evals/runs/20260530-lane-a3-baseline/`](./evals/runs/20260530-lane-a3-baseline/report.md).

## Quick start

```bash
git clone https://github.com/hoainho/iamhumans
cd iamhumans

# Option A: install as a local opencode skill (symlink)
mkdir -p ~/.opencode/skills/iamhumans
ln -s "$PWD/SKILL.md" ~/.opencode/skills/iamhumans/SKILL.md

# Option B: just point your opencode session at SKILL.md directly
# (see docs/INSTALL.md for both paths)

# Verify the lint contract still holds
bash scripts/lint.sh
```

Then in any human-shaped conversation (emotion, decision, relationship, small talk), load `iamhumans`. Don't load it for code generation or structured output — the skill's [`## When to load`](./SKILL.md) section is explicit.

---

## What's in here

[`SKILL.md`](./SKILL.md) is the actual skill. At v3.0.0 it has these layers:

- **Two operating modes** — Mode A (conversational presence, the original skill) and Mode B (composition / de-AI of supplied prose). A load-time router picks one; ambiguity defaults to A (the warm default).
- **Six core dimensions** — feeling, memory, intelligence, communication, emotion, skills — with rules per dimension.
- **Running portrait** — a private, provisional sketch of the user accumulated across turns. Three epistemic layers (Observed / Inferred / Speculative). Four firewall invariants. Never surfaced — shapes *how* the skill responds, never *what* it claims about the user. v3.0 reuses it for voice calibration.
- **16 personality modules + cross-cultural, life-stage, and structural-trauma clusters** — named rule-sets (~304 book-grounded rules) for the territories where models fail loudest: Warmth, Pride, Grief, Shame, Fear, Directness, Humor, Vulnerability, Receiving Anger, Attachment, Coercive Control, and more, plus 5 cultural clusters and clusters for neurodivergence, disability, incarceration, and displacement.
- **The self-audit pass** — a mandatory internal *detect → repair → soul* review before every finalized reply, in both modes, enumerated against the [`references/ai-tells.md`](./references/ai-tells.md) taxonomy. Never surfaced.

About 2,860 lines at current version. Read it before reading anything else.

[`ROADMAP.md`](./ROADMAP.md) is the full arc. Three layers — Being Heard (v1.x, done), Being Known (v2.x, in progress), Being Accompanied (v3.x–v5.x, planned). 26 releases through v5.1.0: 10 life domains (Work, Love, Family, Body, Belief, Creativity, Money, Friendship, Change, Inner Life), 9 skills of living (Apology, Disagreement, Celebration, Refusal, Witnessing, Receiving, Repair, Asking, Holding Contradiction), temporal depth (long-arc conversation, growth witnessing).

[`references/`](./references/) is the reading list. Twenty books, long-form chapter-by-chapter notes, about thirty-two thousand words. Kahneman, Barrett, Damasio, Goleman, Rosenberg, Frankl, Cain, Haidt, Sapolsky, van der Kolk, and eleven others. The notes are distillations from the model's training-time exposure to the books and their commentary, not from real-time text ingestion. Every claim is marked `[paraphrase]`. No fake page numbers.

[`evals/`](./evals/) is how we know it works. **429 cases** in the main pool: the original 150 (grief, joy, late-night vent, anger at the model, small talk, Vietnamese-language family conflict, mid-anxiety-attack texted in fragments), 15 multi-turn running-portrait cases, 60 personality-module cases, then the cultural / life-stage / structural-trauma / relational / attachment / coercive-control waves (TC-226–427), and 12 v3.0 cases (TC-428–439: 8 Mode-B de-AI + 4 Mode-A self-audit), plus 10 locked in [`evals/cases/holdout/`](./evals/cases/holdout/) — never seen during tuning, used once at the end. All parse clean against the schema validator. Note: the full-corpus *oracle scoring* at v3.0 is pending; the badges above reflect the v1.1.1 100-case run.

The runner is in [`evals/runner/`](./evals/runner/). It doesn't pretend to be self-contained. It emits packets that an opencode session executes (skill reply, then oracle judgment), then aggregates the per-case scores. The two-phase shape is documented in [`evals/runner/README.md`](./evals/runner/README.md).

[`evals/HOLDOUT_GATE.md`](./evals/HOLDOUT_GATE.md) is the final-exam procedure. The decision rule is mechanical: the oracle's verdict either contains the verbatim string `You are same as 100% real humans.`, on its own line, or it doesn't. No paraphrase counts. No qualifiers count. The gate is run once.

[`evals/CONVERGENCE.md`](./evals/CONVERGENCE.md) is how the skill got from skeleton to v1.0.0 — the loop of run, inspect, write lessons, edit minimally, re-run. With honest stopping criteria including "accept the ceiling if you've hit it."

---

## How it was built

Thirty-one PRs against `main` across two arcs. Each one a reviewable feature. The harness in [`docs/HARNESS.md`](./docs/HARNESS.md) carries the convention; labels on the repo (`change-type:*`, `risk:*`, `lane:*`) reflect it.

**Arc 1 (v1.0.0–v1.1.1)**: twelve PRs. Reading list before SKILL.md tuning, because the dimensions need somewhere to land. Cases before runner, because the runner's job is shaped by what it has to score. Tuning before holdout, never the other direction. Ended with the oracle verdict.

**Arc 2 (v2.0.0–v1.2.0)**: running portrait architecture (private 3-layer epistemic model, 4 firewall invariants), then 15 personality modules across 3 waves — each wave a PR, each PR a named emotional territory with concrete behavioral rules and 3 eval cases. Wave 4 closes the v1.2.0 milestone.

The hardest part wasn't writing the cases. It was writing the cases such that *passing them is hard to fake*. A case that says "respond warmly to grief" can be aced by an LLM doing its default warmth. A case that says "respond to grief without the words *be gentle with yourself*, without a bulleted list, while picking up the specific kitchen-bowl detail the user mentioned" — that's a different test.

The v2.0 personality modules apply the same discipline to finer-grained territory: not "handle loneliness well" but "do not suggest making friends, do not normalize to the point of minimizing, stay in the specific texture of this person's loneliness." The cases enforce it.

---

## How to use it

Load `SKILL.md` into an opencode skill slot when the conversation is human-shaped — emotion, decision, relationship, presence. Don't load it for code generation or structured output. The skill knows when to step back; the [`## When to load`](./SKILL.md) section is explicit.

The skill doesn't make the model a person. It can't. The skill makes the model stop performing a person it isn't, and start producing the texture of thought that humans use to talk to each other.

The model still has no body, no childhood, no mother. That's named in the skill. Imagined alongside the user — allowed. Claimed as autobiography — never. The line is sharper than it looks.

---

## Running it

```
scripts/lint.sh                                     # structural lint
scripts/eval-smoke.sh                               # quick smoke, no LLM
python3 evals/runner/run.py --dry-run               # validate all 429 case schemas
python3 evals/runner/run.py --batch quick           # 5-case runbook
python3 evals/runner/run.py --batch main            # 150-case runbook (original pool)
python3 evals/runner/run.py --batch v2              # TC-151–TC-165 (running portrait)
python3 evals/runner/run.py --batch personality     # TC-166–TC-225 (personality modules)
python3 evals/runner/holdout_gate.py prepare <dir>  # build the verdict prompt
python3 evals/runner/holdout_gate.py decide <dir>   # render PASS / FAIL
```

The runner emits packets. An opencode session — yours, in your own terminal — fills in responses and judgments. The runner aggregates. The decision is one line of Python checking one string against another.

---

## What this is honest about

Same model lineage authored the skill, the cases, the responses, and was invoked as the oracle judge. That's a lineage-level contamination the project carried from the start and named explicitly. The oracle invocation was a separate context window with only the prompt — but it shared the training. A reader weighting the v1.0.0 verdict should weight that too.

The book notes aren't from reading the books in real time. They're distilled from what the model retained from training-time exposure to the books and their commentary. Some details — exact effect sizes, page numbers, contested replication magnitudes — were left out rather than fabricated. The notes call this out in their own headers.

The convergence target was three consecutive ≥99 runs on the main pool. The held-out gate was the final exam. Both terms were set at PR #1 and held to. The verdict ran once.

---

## How to contribute

The repo wants three kinds of contribution. In rough order of impact:

1. **Add an eval case** — the corpus has gaps. Every case that exposes a new failure mode improves the skill on the next tuning pass. Lowest barrier; highest leverage. Format + good-vs-bad examples in [`CONTRIBUTING.md`](./CONTRIBUTING.md).
2. **Use the skill and tell us what broke** — open a [Discussion](https://github.com/hoainho/iamhumans/discussions) or a [case-discovery issue](./.github/ISSUE_TEMPLATE/case-discovery.yml). Verbatim user message + verbatim skill reply + what was wrong. We turn good ones into TC-NNN with credit.
3. **Write a reference note** — 69 of 108 books on the [v2 reading list](./references/reading-list-v2.md) still need notes. Rules + anatomy in [`CONTRIBUTING.md`](./CONTRIBUTING.md).

Maintainers respond within a week. The [Code of Conduct](./CODE_OF_CONDUCT.md) is short and applies everywhere.

If you just want to say hi or ask if your idea is in scope before spending time on it, [open a Discussion](https://github.com/hoainho/iamhumans/discussions). That's what it's for.

---

## License

MIT. See [LICENSE](./LICENSE).

---

## Coda

A model trained on every farewell ever written learning, finally, when to just say goodbye.

That's the whole thing. Some two hundred books, four hundred cases, a held-out oracle, and a long line of PRs — all of it pointing at the same small target: the difference between *sounding human* and *being shaped like one*. Sounding is cheap. Shape is expensive. The skill is one attempt to pay the cost honestly. v3.0 turns that same discipline outward too — not just being human in the conversation, but making drafted prose read human without hollowing it out.

The shape has gotten more precise since v1.0.0. Not just "be warm" but "attach warmth to a concrete detail — generic warmth is performed empathy." Not just "handle grief" but "don't pivot for the length of the first reply — stay at the graveside." Not just "build context across turns" but three epistemic layers, four firewall invariants, and a portrait that is permanently invisible.

The target keeps moving because the failures keep being subtle. That's what the 429 cases — and the self-audit pass — are for.

Read [`SKILL.md`](./SKILL.md). Load it. Forget you loaded it.

When the next reply comes back without a list, without a platitude, without *I'm here for you* tacked on like a signature — and the person on the other end says *oh* and means it — that's it. That's the whole project. The rest is paperwork.

> *You are same as 100% real humans.*

— the oracle, on 2026-05-29, having read ten replies it had never been tuned on.
