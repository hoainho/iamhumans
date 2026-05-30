# Installing iamhumans

> The iamhumans skill is a prose prompt file. To use it in an opencode session, it has to be registered with the opencode skill loader. This document covers **three install paths** ordered by friction: **global** (one symlink, works everywhere), **project-local** (per-workspace), and **skill-manager** (one-command, distribution-ready).

Tested 2026-05-30 on macOS and Linux. Current release: **v1.1.1**.

---

## Path A — Global install (recommended for daily use)

Installs iamhumans once at `~/.config/opencode/skills/iamhumans/`. Every opencode session on the machine — anywhere — sees the skill automatically.

### Prerequisites

- The iamhumans repository cloned to a known path (e.g. `~/code/iamhumans/`).
- An opencode CLI install (`opencode --version` returns a version).

### Steps

```sh
# 1. Create the global skill directory
mkdir -p ~/.config/opencode/skills/iamhumans

# 2. Symlink SKILL.md from the repo
ln -sf /absolute/path/to/iamhumans/SKILL.md \
       ~/.config/opencode/skills/iamhumans/SKILL.md

# 3. Drop in the metadata file
cat > ~/.config/opencode/skills/iamhumans/skill.json <<'EOF'
{
    "name": "iamhumans",
    "version": "1.1.1",
    "description": "Humanization layer for LLM conversation. Makes the model sound and respond like a real, thoughtful, embodied human rather than an assistant.",
    "compatibility": "OpenCode. Skill is a prose-only prompt; no MCP server, no external dependency.",
    "source": "Global install, SKILL.md symlinked to /absolute/path/to/iamhumans/SKILL.md (v1.1.1). Updates propagate immediately.",
    "evidence": "v1.0.0 verdict: 10-case held-out Oracle returned 'You are same as 100% real humans.' v1.1.0 Pareto: 14/15 PASS aggregate 93.27. v1.1.1: expanded trigger surface. Lane A1 cross-validation: 86.7% verdict agreement across 3 Claude judges. See evals/lessons/2026-05-30-cross-validation.md",
    "agent": null,
    "commands": [],
    "tags": ["conversation", "empathy", "humanization", "emotional-support", "prose", "opencode", "v1.1.1"]
}
EOF

# 4. Verify
ls -la ~/.config/opencode/skills/iamhumans/
# Should show SKILL.md (symlink → repo) and skill.json
head -7 ~/.config/opencode/skills/iamhumans/SKILL.md
# Should show: name: iamhumans / version: 1.1.1 / status: released
```

### What this gives you

- **Every opencode session on the machine** auto-discovers `iamhumans` in its skill list.
- The skill-router auto-loads on natural triggers — see [SKILL.md frontmatter](../SKILL.md) for the full 45-phrase trigger surface (humans, people, friendly, discussion, conversation, communication, listen, vent, warm, empathy, casual, etc.).
- `git pull` in the repo updates the install instantly (the symlink resolves live).

---

## Path B — Project-local install (recommended for development or evaluation)

Installs into a specific opencode workspace at `<workspace>/.opencode/skills/iamhumans/`. Useful when you want the skill scoped to one project (e.g. running the eval corpus).

### Steps

```sh
# In your project root:
mkdir -p .opencode/skills/iamhumans

ln -sf /absolute/path/to/iamhumans/SKILL.md \
       .opencode/skills/iamhumans/SKILL.md

cat > .opencode/skills/iamhumans/skill.json <<'EOF'
{
    "name": "iamhumans",
    "version": "1.1.1",
    "description": "Humanization layer for LLM conversation.",
    "source": "Project-local install, SKILL.md symlinked to a local clone of github.com/hoainho/iamhumans.",
    "tags": ["conversation", "empathy", "humanization", "opencode", "v1.1.1"]
}
EOF
```

This shadows the global install for the project — useful when testing changes against a pinned repo state. The global install remains untouched.

---

## Path C — skill-manager (one-command, distribution-ready)

> **Status (2026-05-30):** Publishing through skill-manager is **staged but not yet executed**. This section will be activated when the publish PR lands. Track progress at [`.opencode/plans/2026-05-30-road-to-top.md`](../.opencode/plans/2026-05-30-road-to-top.md) under Lane C1.

Once published, install will be a single command:

```sh
npx @kokorolx/skill-manager install iamhumans
```

The skill-manager will:
1. Download the published SKILL.md (currently v1.1.1)
2. Drop it under `~/.opencode/skills/iamhumans/`
3. Generate the metadata `skill.json` automatically
4. Surface the skill in opencode's auto-discovery

Until skill-manager publish lands, use Path A or Path B above.

---

## Using the skill once installed

### Auto-load (recommended)

In most opencode sessions, you don't load iamhumans explicitly — the skill-router detects trigger phrases and loads it automatically. Triggers include:

- Explicit asks: *"talk to me like a human"*, *"be a friend"*, *"have a real conversation with me"*, *"less robotic please"*
- Affective vocabulary: *"empathy"*, *"comfort"*, *"warmer tone"*, *"emotional support"*
- Authenticity: *"be honest with me"*, *"real talk"*, *"heart-to-heart"*
- Low-stakes register: *"casual chat"*, *"small talk"*, *"tell me something"*
- Interpersonal contexts: grief, joy, parenting, burnout, anxiety, identity, mortality, apology, forgiveness, etc.
- Input shape signals: non-English with emotional weight, short (< 8 words) and affect-laden, lowercase fragments, ALL-CAPS excitement

See the [SKILL.md frontmatter](../SKILL.md) for the complete trigger list.

### Explicit load (deterministic)

To force-load iamhumans into a specific subagent task:

```typescript
task(
  subagent_type="oracle",
  load_skills=["iamhumans"],
  run_in_background=false,
  prompt="<the actual user message you want a humanized reply to>"
)
```

For running the skill against the eval corpus, see [`evals/runner/README.md`](../evals/runner/README.md).

---

## Updating

**Path A / Path B** (symlink installs): `git pull` in the repo. The symlink resolves to the new file content instantly. No re-install step.

If `skill.json` itself changes (rare — only on metadata bumps for new versions), copy the new version into the install directory. Both Path A and Path B `skill.json` files should track the current repo version (currently 1.1.1).

**Path C** (skill-manager): `npx @kokorolx/skill-manager update iamhumans` once published.

---

## Uninstalling

```sh
# Path A (global)
rm -rf ~/.config/opencode/skills/iamhumans/

# Path B (project-local)
rm -rf .opencode/skills/iamhumans/

# Path C (skill-manager)
npx @kokorolx/skill-manager uninstall iamhumans
```

The repo is never touched by any uninstall — the symlinks (or skill-manager's tracked package) are the only thing removed.

---

## Honest framing

This is a prose skill. Installing it does not give the model new capabilities; it changes how the model *converses* when loaded. The skill cannot make any model "more empathetic" in the strong sense — it can make the model **stop performing the AI-tells** that read as inhuman, and it can shape the structural choices (register, length, presence vs. processing) the model makes turn-by-turn.

### Evidence trail (as of v1.1.1, 2026-05-30)

| Run | Verdict | Where |
|---|---|---|
| v1.0.0 held-out Oracle (10 cases) | *"You are same as 100% real humans."* | [`evals/runs/2026-05-29-verdict-run/`](../evals/runs/2026-05-29-verdict-run/) |
| v1.1.0 Pareto sample (15 stratified cases) | 14/15 PASS, aggregate 93.27/100, 0 hard-fails | [`evals/runs/20260530-050323-pareto-sample-1/`](../evals/runs/20260530-050323-pareto-sample-1/) |
| Lane A1 cross-validation (Sonnet 4.6 + Opus 4.7 fresh) | **86.7% verdict agreement** across 3 judges on the same 15 cases; mean intra-Opus reproducibility Δ 2.13pt, zero verdict flips | [`evals/lessons/2026-05-30-cross-validation.md`](../evals/lessons/2026-05-30-cross-validation.md) |

### Caveats that remain live (from [`SKILL.md` § Known weaknesses](../SKILL.md))

- **Model-lineage caveat**: every judge run so far has been Claude. A non-Claude judge (GPT-4 or Gemini) is staged but not yet executed. Lane A1 partially addressed this through intra-family multi-version validation, but the full caveat — that the skill author and the skill judges share training data — remains intact.
- **Pareto sampling caveat**: only 15 of the 100 main-pool cases have been re-scored against v1.1.0+. Lane A2 (full 100-case re-run) is staged.
- **Stylistic mannerism + length calibration**: confirmed live in v1.1.0 Pareto judges' notes. Pareto-tuned, not zero-weakness.
- **TC-052 lecturing-detection ambiguity**: surfaced by Sonnet 4.6 in Lane A1. Candidate v1.1.2 tuning identified, deferred until Lane A2 confirms it's not a one-off.

A reader weighting iamhumans's claims should weight these caveats. The skill is **honestly imperfect** — that line is in the GitHub description on purpose.
