# Installing iamhumans

> The iamhumans skill is a prose prompt file. To use it inside an opencode session, it has to be registered with the opencode skill loader. This document covers two install paths: **local** (recommended for development, evaluation, and testing) and **published** (for distribution).

## Local install (recommended)

Tested 2026-05-30. Works on macOS and Linux.

### Prerequisites

- The iamhumans repository cloned to a known path.
- An opencode workspace at `~/.config/opencode/` or `<workspace>/.opencode/`.
- The opencode CLI installed (`opencode --version` returns a version).

### Steps

1. **Locate your opencode skills directory.** In a workspace, this is `<workspace>/.opencode/skills/`. Globally, it is `~/.config/opencode/skills/`.

2. **Create a folder for the skill.** Inside the skills directory:

   ```sh
   mkdir -p .opencode/skills/iamhumans
   ```

3. **Symlink SKILL.md to the cloned repo.** This makes the install track the repo state. Updates to SKILL.md in the repo propagate immediately.

   ```sh
   ln -s /absolute/path/to/iamhumans/SKILL.md .opencode/skills/iamhumans/SKILL.md
   ```

4. **Add the metadata file.** Create `.opencode/skills/iamhumans/skill.json`:

   ```json
   {
     "name": "iamhumans",
     "version": "1.0.0",
     "description": "Humanization layer for LLM conversation. Use this skill whenever the agent's reply will be read by a human and the goal is for the reply to feel like it came from a thoughtful, embodied, fallible person rather than an assistant.",
     "compatibility": "OpenCode. Skill is a prose-only prompt; no MCP server, no external dependency.",
     "source": "Local install, SKILL.md symlinked to a local clone of github.com/hoainho/iamhumans.",
     "evidence": "Held-out 10-case Oracle verdict (2026-05-29) returned the verbatim verdict line. See evals/runs/2026-05-29-verdict-run/ in the repo.",
     "agent": null,
     "commands": [],
     "tags": ["conversation", "empathy", "humanization", "emotional-support", "prose"]
   }
   ```

5. **Verify the install.** From an opencode session:

   ```
   ls .opencode/skills/iamhumans/
   ```

   should show both `SKILL.md` (the symlink) and `skill.json`. Reading `SKILL.md` should return the frontmatter `version: 1.0.0` / `status: released`.

### Using it

In an opencode session, load iamhumans into a subagent task when the conversation calls for it:

```typescript
task(
  subagent_type="oracle",
  load_skills=["iamhumans"],
  run_in_background=false,
  prompt="<the actual user message you want a humanized reply to>"
)
```

For testing the skill against the eval corpus, see [`evals/runner/README.md`](../evals/runner/README.md).

### Updating

Because `SKILL.md` is a symlink, `git pull` in the iamhumans repo updates the installed skill immediately. No re-install step is needed.

If `skill.json` changes (rarely — only on metadata bumps), copy the new version into the skills directory.

### Uninstalling

```sh
rm -rf .opencode/skills/iamhumans/
```

The symlink is removed; the repo is untouched.

## Published install (future)

The skill is **not yet** published to the [skill-manager](https://github.com/kokorolx/skill-manager) npm package. Publishing is staged behind:

1. A v1.1.0 release that absorbs lessons from a representative test run (in progress; see [`.opencode/plans/2026-05-29-iamhumans-v2.md`](../.opencode/plans/2026-05-29-iamhumans-v2.md)).
2. A clean separation of public vs. private skill components (the eval corpus, run reports, and verdict evidence stay in the repo; the SKILL.md prompt itself is what gets distributed).

When published, install will be:

```sh
npx @kokorolx/skill-manager install iamhumans
```

## Honest framing

This is a prose skill. Installing it does not give the model new capabilities; it changes how the model *converses* when loaded. The skill cannot make any model "more empathetic" in the strong sense — it can make the model *stop performing the AI-tells* that read as inhuman, and it can shape the structural choices (register, length, presence vs. processing) the model makes turn-by-turn.

The v1.0.0 verdict came from a 10-case held-out Oracle judgment in a single run. That evidence is preserved verbatim in the repo, including the model-lineage caveat: the model that authored the skill, the cases, the responses, and was invoked as the Oracle judge are all the same lineage. A reader weighting the verdict should weight that caveat.
