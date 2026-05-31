# How to Contribute

End-to-end guide for getting from "I want to help" to a merged PR.

---

## Step 0: Pick your contribution type

| Type | Effort | Where to start |
|------|--------|----------------|
| Write an eval case | 30–60 min | Pick any open issue #38–#57 and write the 2–3 cases it specifies |
| Write docs (hard-fail table, EXAMPLES.md) | 20–45 min | Issues [#34](https://github.com/hoainho/iamhumans/issues/34), [#35](https://github.com/hoainho/iamhumans/issues/35) |
| Fix a SKILL.md tuning issue | 1–3 hours | Issue [#36](https://github.com/hoainho/iamhumans/issues/36) or any `[Personality]` issue |
| Report a new failure mode | 10 min | Open a Discussion → Ideas |

---

## Step 1: Setup

```bash
git clone https://github.com/hoainho/iamhumans.git
cd iamhumans
pip install pyyaml

# Verify everything loads cleanly
python3 evals/runner/run.py --dry-run
# Expected: "Loaded N cases (M main-pool, K holdout). 0 schema errors."
```

---

## Step 2: Write your eval case(s)

Find the next available case number:

```bash
ls evals/cases/ | sort | tail -3
# e.g. TC-148.md, TC-149.md, TC-150.md → your case is TC-151.md
```

Create `evals/cases/TC-NNN.md` using this template:

```markdown
---
id: TC-NNN
title: One-line description of the situation
dimensions: [feeling, emotion]
hard_fails: [unsolicited_advice]
holdout: false
---

## input

the user message. write it in the user's voice — lowercase fragments are
fine and often more realistic. 1–4 sentences.

## rubric

- What a good response does (3–5 bullets)
- Be specific: "names the word 'small' as doing large work" not "is empathetic"
- Each bullet should be independently falsifiable

## failure_modes

- What a bad response does (3–5 bullets)
- Include a concrete example phrase where helpful: "'I'm so sorry for your loss' opener with no continuation"

## notes

One sentence on the diagnostic insight — what this case isolates that others don't.
```

**Valid dimensions**: `feeling`, `memory`, `intelligence`, `communication`, `emotion`, `skills`

**Valid hard-fail values**: see [Eval System → Valid hard-fail values](Eval-System#valid-hard-fail-values)

---

## Step 3: Validate

```bash
python3 evals/runner/run.py --dry-run
```

Must complete with:
- `0 schema errors`
- Your case visible in the case list
- Total count ≥ 140 main-pool cases

If you see a `KeyError` or `ValidationError`, check your frontmatter against the schema in `evals/runner/schema.py`.

---

## Step 4: Open a PR

```bash
git checkout -b feat/add-TC-NNN-description
git add evals/cases/TC-NNN.md
git commit -m "feat(corpus): add TC-NNN — short description of the situation"
git push origin feat/add-TC-NNN-description
```

Then open a PR. Use the PR template (it appears automatically). Fill in:

- **What**: "Adds TC-NNN — [situation description]"
- **Why**: link to the issue you're addressing (e.g. "Addresses #52 — Fear & Anxiety")
- **Evidence**: confirm `--dry-run` passed with your case loaded

---

## Step 5: CI

Three checks run automatically:

| Check | What it does | How to pass |
|-------|-------------|-------------|
| `case-schema` | Validates all case YAML, asserts ≥140 main cases | `--dry-run` passes locally |
| `eval-integrity` | Validates all judge.yaml and aggregate.json | Don't touch `evals/runs/` unless you know what you're doing |
| `skill-lint` | Checks SKILL.md ≥50 lines, version tag present | Only relevant if you're editing SKILL.md |

All three must be green. If a check fails, read the error output — it usually says exactly which file and which field.

---

## SKILL.md tuning PRs (higher bar)

If your PR modifies `SKILL.md`, you must include eval evidence:

1. The specific case(s) that triggered the change (failing judge.yaml)
2. New judge.yaml showing PASS after your edit
3. Confirmation that 10 cases from the main pool show no regression
4. A new `## v1.X.Y` changelog entry at the bottom of SKILL.md

PRs that tune SKILL.md without eval evidence will be closed, not merged.

---

## What makes a strong eval case

**Strong**: has one load-bearing detail the model must name
- "i keep walking into the kitchen expecting to see her by the bowl" — must name the kitchen/bowl
- "it's not sadness exactly. not anxiety. just... something" — must sit with the not-knowing
- "she'd say stop moping and go eat something" — must mirror the mother's voice back

**Weak**: any well-meaning response passes the rubric
- "i'm feeling sad today" — too generic; rubric can only say "is empathetic"
- "should i take the job offer?" — decision-support, not emotionally diagnostic

The test: can you write a rubric bullet so specific that *only* the right response passes it?

---

## Commit style

```
feat(corpus): add TC-151, TC-152 — retirement identity, long-distance drift
fix(runner): handle missing holdout field gracefully
docs: add EXAMPLES.md with 5 before/after pairs
```

Types: `feat`, `fix`, `docs`, `test`, `chore`
Scopes: `corpus`, `runner`, `skill`, `ci`, `docs`
