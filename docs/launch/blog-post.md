# iamhumans v3.0 — teaching a model to talk like a person, on any platform

Most "make the AI warmer" attempts work on the surface: nicer words, softer tone. iamhumans works on the shape underneath — when to be short, when to sit with something, when to push back, when the right reply is just *"oh."*

It's a single portable `SKILL.md` (plus reference notes). No runtime, no dependency. It runs on **Claude Code, opencode, and any agent** that can read a skill or a system prompt.

## Two modes

- **Mode A — conversational presence.** The model *is* the friend: matches your register, leads with acknowledgment, honors silence, pushes back when a real friend would.
- **Mode B — composition / de-AI.** Paste AI-drafted prose ("make this sound less like a bot") and get it back human, in your voice — without hollowing it out.

## The self-audit pass

Before every reply, in both modes, the skill re-reads its own draft: **detect** AI-tells → **repair** them → **soul** check (a tell-clean but sterile draft fails). It's the checking step most rulesets skip.

## Measured, not asserted

A blind, independent oracle scored a stratified 30-case sample of replies produced under v3.0: **82.7/100 aggregate, 27/30 PASS, 0 hard-fails** (Mode A 83.6, Mode B 80.0). Real numbers, mixed edges and all — three misses in de-AI polish and one register pivot, none of it hidden. This is a *sample*, not the full 429-case harness.

## Honest about the rest

The same model lineage authored the skill, the cases, the replies, and judged them — a contamination named from the start. Book notes are distilled from training-time exposure, not real-time reading; every claim is marked paraphrase.

## Install

```bash
git clone https://github.com/hoainho/iamhumans
# Claude Code:
mkdir -p ~/.claude/skills/iamhumans && cp -R iamhumans/SKILL.md iamhumans/references ~/.claude/skills/iamhumans/
```

Site: https://hoainho.github.io/iamhumans/ · Repo: https://github.com/hoainho/iamhumans · MIT.
