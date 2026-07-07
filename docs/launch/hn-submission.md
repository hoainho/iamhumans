# HN submission — iamhumans v3.0

**Title:** Show HN: iamhumans – a portable skill that teaches any LLM to talk like a person

**URL:** https://github.com/hoainho/iamhumans

**Text:**

iamhumans is a single `SKILL.md` (no runtime, no dependency) that works on the shape of a conversation rather than the wording — when to be short, when to sit with something, when the right reply is just "oh." It runs on Claude Code, opencode, or any agent you can hand a system prompt.

It has two modes: conversational presence, and a composition / de-AI mode that rewrites AI-drafted prose to read human in your own voice. Every reply runs an internal self-audit — detect AI-tells, repair them, then a "soul check" that fails a draft which is clean but sterile.

I tried to be honest about evidence. A blind, same-lineage oracle scored a stratified 30-case sample at 82.7/100 (27/30 PASS, 0 hard-fails); that's a sample, not the full 429-case harness, and the misses are shown, not hidden. The lineage contamination and the paraphrase-only book notes are stated up front.

MIT. Feedback and adversarial eval cases welcome.
