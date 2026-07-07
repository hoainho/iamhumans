# opencode PR draft — add iamhumans to the skill registry

**Title:** Add iamhumans — a humanization skill (conversational presence + de-AI)

**What this adds**

iamhumans is a prose-only `SKILL.md` (no MCP server, no external dependency) that teaches the model to talk like a person: matching register, leading with acknowledgment, honoring silence, and — new in v3.0 — a composition / de-AI mode plus a self-audit pass (detect → repair → soul) on every reply.

It's portable by design (Claude Code, opencode, any agent), so it slots cleanly into opencode's skills directory.

**Evidence (honest)**

Blind-oracle-scored 30-case sample: 82.7/100, 27/30 PASS, 0 hard-fails. A sample, not the full 429-case harness; same-lineage judge caveat noted.

**Install**

```bash
mkdir -p ~/.opencode/skills/iamhumans
ln -s "$PWD/SKILL.md" ~/.opencode/skills/iamhumans/SKILL.md
```

Repo: https://github.com/hoainho/iamhumans · MIT.
