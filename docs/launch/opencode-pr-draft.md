# Draft: PR to sst/opencode README or awesome-opencode list

## Target

Either:
- **PR to `sst/opencode` README** — add to a "Community Skills" section if one exists, or propose one
- **PR to `awesome-opencode`** — if a curated list exists
- **opencode Discussions post** — if neither PR target is appropriate

Check: https://github.com/sst/opencode — look for CONTRIBUTING.md, community section in README, or Discussions.

---

## PR title

`docs: add iamhumans to community skills — human-shaped conversation skill with 100-case eval`

---

## PR body / list entry text

**Short (for a table row):**

| [iamhumans](https://github.com/hoainho/iamhumans) | Teaches Claude the shape of human conversation — when to be short, when to sit with something, when to push back. Removes sycophancy, lecturing, performed empathy. 99/100 on 100-case eval. |

**Medium (for a description block):**

### [iamhumans](https://github.com/hoainho/iamhumans)

An opencode skill (~200 lines) for human-shaped conversations — grief, anger, joy, decisions, small talk, late-night vent, relationship conflict.

The skill teaches when to be short, when to stay, when the right reply is "oh." It has an explicit list of AI-tells (sycophancy, lecturing, performed empathy, structured output in grief) that Claude is built to refuse when the skill is loaded.

**Evidence:** 99/100 PASS on a 100-case eval. Without the skill, baseline Claude scores 1/20 on the same 20 cases (7.6/100 aggregate, 18 hard fails). Held-out oracle verdict: *"You are same as 100% real humans."*

Install: `ln -s $PWD/SKILL.md ~/.opencode/skills/iamhumans/SKILL.md`

---

## Instructions for submitting

1. Check if `sst/opencode` has a community skills section in README or CONTRIBUTING.md
2. If yes — open a PR adding iamhumans to the list with the short table row text
3. If no — open a Discussion proposing a "Community Skills" section and include the medium block
4. Also check for an `awesome-opencode` repo on GitHub — if it exists, PR there too

**Do not open the PR until you've read the contributing guidelines for the target repo.** Match whatever format they use.
