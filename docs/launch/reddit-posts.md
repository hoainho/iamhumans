# Reddit drafts — iamhumans v3.0

## r/LocalLLaMA / r/ClaudeAI

**Title:** iamhumans v3.0 — a portable skill that teaches any LLM to talk like a person (Claude Code, opencode, any agent)

It's a single `SKILL.md` (no runtime) that works on the *shape* of a reply, not the wording — when to be short, when to sit with something, when to push back.

Two modes:
- **Mode A** — conversational presence: matches your register, leads with acknowledgment, honors silence.
- **Mode B** — composition / de-AI: paste AI-drafted prose and get it back human, in your voice.

Every reply runs a self-audit pass: detect AI-tells → repair → soul check (a sterile-but-clean draft fails).

**Honest numbers:** a blind independent oracle scored a 30-case sample at 82.7/100, 27/30 PASS, 0 hard-fails (Mode A 83.6, Mode B 80.0). It's a sample, not the full 429-case harness, and the misses (two de-AI, one register pivot) are shown. Same-lineage judge caveat noted; book notes are paraphrase.

Install: drop it in `~/.claude/skills/`, symlink into opencode, or paste into any system prompt. MIT.

Repo: https://github.com/hoainho/iamhumans · Site: https://hoainho.github.io/iamhumans/
