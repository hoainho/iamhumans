# iamhumans

![iamhumans social preview](./assets/og/og-image.png)

[![CI](https://github.com/hoainho/iamhumans/actions/workflows/ci.yml/badge.svg)](https://github.com/hoainho/iamhumans/actions/workflows/ci.yml)
[![version](https://img.shields.io/badge/version-v3.0.0-blue.svg)](./SKILL.md)
[![license: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![measured: 82.7/100 (sample)](https://img.shields.io/badge/measured-82.7%2F100%20sample-brightgreen.svg)](https://hoainho.github.io/iamhumans/)
[![hard-fails: 0](https://img.shields.io/badge/hard--fails-0-brightgreen.svg)](https://hoainho.github.io/iamhumans/)
[![corpus: 429 cases](https://img.shields.io/badge/corpus-429%20cases-blue.svg)](./evals/cases/)
[![modes: 2](https://img.shields.io/badge/modes-A%20presence%20%2B%20B%20de--AI-blue.svg)](./SKILL.md)
[![platforms](https://img.shields.io/badge/runs%20on-Claude%20Code%20·%20opencode%20·%20any%20agent-black.svg)](#install-anywhere)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

A portable skill for **Claude Code, opencode, and any agent**. It teaches a language model how to talk like a person.

Not how to *sound* like a person — sounding like is easy, and it's what most failures already do. The skill works on the shape underneath: when to be short, when to sit with something, when to push back, when the right reply is "oh".

**Live site:** [hoainho.github.io/iamhumans](https://hoainho.github.io/iamhumans/)

---

## What v3.0 is

**Two operating modes**, one shared self-audit pass:

- **Mode A — conversational presence.** You *are* the friend, replying in real time: matching register, leading with acknowledgment, honoring silence, pushing back when a real friend would.
- **Mode B — composition / de-AI.** Paste AI-drafted prose ("make this sound less like a bot") and get it back human, in *your* voice. Strips the tells without hollowing the writing out.

**The self-audit pass** runs before *every* finalized reply, in both modes — an internal *detect → repair → soul* review:

1. **Detect** — read the draft as a skeptic; enumerate AI-tells against the taxonomy in [`references/ai-tells.md`](./references/ai-tells.md).
2. **Repair** — cut the specific tells; never invent facts to fill a gap.
3. **Soul** — a tell-clean but sterile draft *fails*. Stripping is necessary; soul is the point.

Plus: a six-family **AI-tell taxonomy**, **voice calibration** (a six-axis fingerprint that reuses the private running portrait — no new state), a **running portrait** (a provisional, never-surfaced read of the user that shapes *how* the skill responds, never *what* it claims), and **16 modules** (~304 book-grounded rules) covering the emotional territories where models fail loudest — Warmth, Grief, Shame, Fear, Directness, Humor, Vulnerability, Receiving Anger, Attachment, Coercive Control, and more — alongside cross-cultural, life-stage, and structural-trauma clusters.

---

## Measured, not asserted

A blind, independent oracle scored a stratified 30-case sample of replies produced under v3.0:

| | |
|---|---|
| **Aggregate** | **82.7 / 100** |
| **PASS rate** | **27 / 30 (90%)** |
| **Hard-fails** | **0** |
| Mode A (presence) | 83.6 / 100 · 21/22 |
| Mode B (de-AI) | 80.0 / 100 · 6/8 |

Real numbers, mixed edges and all — three misses sit in de-AI polish and one register pivot; none of it is hidden. **This is a sample (30 of 429), not the full-corpus harness** (see [What this is honest about](#what-this-is-honest-about)).

---

## Install anywhere

iamhumans is a single portable `SKILL.md` (plus `references/`) — no runtime, no dependency.

```bash
git clone https://github.com/hoainho/iamhumans
cd iamhumans
```

**Claude Code** — drop it into your skills directory:
```bash
mkdir -p ~/.claude/skills/iamhumans
cp -R SKILL.md references ~/.claude/skills/iamhumans/
```

**opencode** — symlink so it stays in sync with the repo:
```bash
mkdir -p ~/.opencode/skills/iamhumans
ln -s "$PWD/SKILL.md" ~/.opencode/skills/iamhumans/SKILL.md
```

**Any other agent** (Cursor, Windsurf, a raw API loop, your own harness) — iamhumans is prose, so any model can use it: open `SKILL.md`, paste it into the system prompt / instructions, and load it when the conversation is human-shaped.

> **MCP (roadmap)** — a thin MCP server that serves the skill to any MCP-capable provider is planned. Today the skill *is* the product; an MCP wrapper is a distribution convenience, not a dependency.

```bash
# verify the contracts still hold
bash scripts/lint.sh
python3 evals/runner/run.py --dry-run   # validates all 429 case schemas
```

Then in any human-shaped conversation (emotion, decision, relationship, small talk), load `iamhumans` — or hand it a draft and say "make this sound less like a bot" (Mode B). Don't load it for code generation or machine-readable output — the skill's [`## When to load`](./SKILL.md) section is explicit.

---

## What's in here

[`SKILL.md`](./SKILL.md) is the actual skill. Its layers:

- **Two operating modes** — a load-time router picks Mode A (presence) or Mode B (composition / de-AI); ambiguity defaults to A, the warm default.
- **Six core dimensions** — feeling, memory, intelligence, communication, emotion, skills.
- **Running portrait** — a private, provisional, never-surfaced sketch of the user (Observed / Inferred / Speculative), behind four firewall invariants; also the source for voice calibration.
- **16 modules + clusters** — named rule-sets (~304 book-grounded rules) for high-failure emotional territory, plus cross-cultural, life-stage, and structural-trauma clusters.
- **The self-audit pass** — the *detect → repair → soul* review before every reply, both modes, enumerated against [`references/ai-tells.md`](./references/ai-tells.md).

[`references/`](./references/) is the reading corpus the rules are grounded in — long-form, chapter-by-chapter notes. The notes are distilled from the model's training-time exposure to the books and their commentary, not real-time ingestion. Every claim is marked `[paraphrase]`; no fabricated page numbers.

[`evals/`](./evals/) is how it's checked. **429 cases** in the main pool (grief, joy, late-night vent, anger at the model, small talk, cross-cultural family conflict, mid-anxiety-attack in fragments, and the composition / de-AI cases), plus 10 locked in [`evals/cases/holdout/`](./evals/cases/holdout/). All parse clean against the schema validator. The runner ([`evals/runner/`](./evals/runner/)) emits packets an agent session executes (skill reply, then oracle judgment), then aggregates the scores.

[`openspec/changes/2026-07-07-v3-composition-and-self-audit/`](./openspec/changes/2026-07-07-v3-composition-and-self-audit/) is the full v3.0 design — proposal, design, and tasks.

---

## How to use it

Load `SKILL.md` when the conversation is human-shaped — emotion, decision, relationship, presence — or hand the skill a draft to de-AI. Don't load it for code generation or structured output; the skill knows when to step back, and the [`## When to load`](./SKILL.md) section is explicit.

The skill doesn't make the model a person. It can't. It makes the model stop performing a person it isn't, and start producing the texture of thought humans use to talk to each other. The model still has no body, no childhood, no mother — that's named in the skill. Imagined alongside the user: allowed. Claimed as autobiography: never.

---

## What this is honest about

v3.0 is measured on a **blind-graded 30-case sample — aggregate 82.7/100, 27/30 PASS, 0 hard-fails** (above), plus schema dry-run, lint, and a Mode-A regression pass in which the one miss was a door-reopener that has since been fixed. It has **not** yet been re-scored on the full 429-case oracle harness, and the sample keeps its mixed edges — two de-AI replies and one register pivot scored below the bar, and none of it is hidden.

The same model lineage authored the skill, the cases, the replies, and served as oracle judge — a lineage-level contamination named from the start. The oracle runs in a separate context with only the prompt, but it shares the training; weight the numbers accordingly.

Book notes are distilled from training-time exposure, not real-time reading; every claim is marked as paraphrase, with no fabricated page numbers.

---

## How to contribute

In rough order of impact:

1. **Add an eval case** — the corpus has gaps. Every case that exposes a new failure mode improves the skill on the next tuning pass. Format + examples in [`CONTRIBUTING.md`](./CONTRIBUTING.md).
2. **Use the skill and tell us what broke** — open a [Discussion](https://github.com/hoainho/iamhumans/discussions) or a case-discovery issue: verbatim user message + verbatim skill reply + what was wrong.
3. **Write a reference note** — several books in the reading corpus still need notes. Rules + anatomy in [`CONTRIBUTING.md`](./CONTRIBUTING.md).

The [Code of Conduct](./CODE_OF_CONDUCT.md) is short and applies everywhere.

---

## License

MIT. See [LICENSE](./LICENSE).

---

## Coda

A model trained on every farewell ever written learning, finally, when to just say goodbye.

That's the whole target: the difference between *sounding human* and *being shaped like one*. Sounding is cheap. Shape is expensive. v3.0 turns that discipline both ways — being human in the conversation, and making drafted prose read human without hollowing it out.

Read [`SKILL.md`](./SKILL.md). Load it. Forget you loaded it. When the next reply comes back without a list, without a platitude, without *I'm here for you* tacked on like a signature — and the person on the other end says *oh* and means it — that's the whole project. The rest is paperwork.
