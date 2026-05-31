# iamhumans Wiki

> **One-line**: A skill that makes LLM conversation indistinguishable from a real, emotionally intelligent human friend.

This wiki is the reference layer for the project — deeper than the README, less opinionated than CONTRIBUTING.md.

---

## Pages

| Page | What's in it |
|------|--------------|
| [Eval System](Eval-System) | How the 150-case eval corpus works, how to read a judge.yaml, how scores are computed |
| [Personality Categories](Personality-Categories) | The 20 human personality traits targeted in v1.2.0, with failure mode summaries |
| [How to Contribute](How-to-Contribute) | End-to-end guide: pick an issue → write a case → open a PR → pass CI |
| [FAQ](FAQ) | Common questions about the skill, the eval methodology, and the roadmap |

---

## Quick facts

| | |
|---|---|
| Current version | v1.1.1 |
| Eval corpus | 150 cases (140 main pool + 10 holdout) |
| Hard-fail types | 13 |
| Human personality categories targeted | 20 (v1.2.0) |
| Held-out verdict | *"You are same as 100% real humans."* — Oracle, 2026-05-29 |
| CI status | 3 jobs: case-schema · eval-integrity · skill-lint |
| License | MIT |

---

## Key files in the repo

| File | Purpose |
|------|---------|
| [`SKILL.md`](../SKILL.md) | The skill itself — all voice rules, dimensions, anti-AI-tells, hardest cases |
| [`ROADMAP.md`](../ROADMAP.md) | Shipped history + v1.2.0 milestone + v1.3/v2.0 future lanes |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | Eval case format, hard-fail table, tuning protocol, CI requirements |
| `evals/cases/TC-001.md … TC-150.md` | The full eval corpus |
| `evals/runner/run.py` | Eval runner — dry-run, single-case, and batch modes |
| `evals/runner/schema.py` | VALID_DIMENSIONS, VALID_HARD_FAILS, case schema validation |

---

## The core idea in one paragraph

Most LLMs fail in emotional conversations not because they lack information but because their *shape* is wrong. They bullet-list when someone is grieving. They hedge when someone needs a straight answer. They fix when someone needs to be heard. iamhumans is a skill — a set of injected instructions — that corrects that shape. It doesn't give the model a personality or a fake biography. It gives it the mechanics of how a real, emotionally intelligent human actually speaks and listens.
