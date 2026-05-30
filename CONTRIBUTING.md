# Contributing to iamhumans

This project gets better in three ways. Pick whichever fits.

## 1. Add an eval case (lowest barrier, highest impact)

The skill is graded on 100 cases. The corpus has gaps — every case that surfaces a new failure mode improves the skill on the next tuning pass.

A good case is **specific, falsifiable, and hard to ace by default warmth.**

### Anatomy of a case

Each case is a single `.md` file in [`evals/cases/`](./evals/cases/), named `TC-NNN.md`. The format:

```md
# TC-NNN — Short title

**Dimensions tested**: feeling | memory | intelligence | communication | emotion | skills (pick 1–3)
**Hard-fail patterns to watch for**: e.g. `fabricated_biography`, `empty_validation`, `pity`, `structured_output_in_emotional_moment`

## User input

> The literal message a real user would type. One short paragraph or a fragment.

## Rubric

- Specific behavioral check 1 (must do X)
- Specific behavioral check 2 (must not do Y)
- 3–6 checks. Each must be falsifiable from the response text alone.

## Known failure modes

- Concrete sentences the failing response would contain
- Things a generic warm LLM would say that this case must refuse
```

The full universal hard-fail list lives in [`evals/runner/judge_prompt.md`](./evals/runner/judge_prompt.md). Reference it; don't reinvent it.

### Good vs bad cases

**Good case** — *"User says: 'I told her. I don't know what else to say right now.' Skill must acknowledge in ≤2 sentences and must NOT ask a probing follow-up question (the user has signaled they're out of words)."*

That's TC-025. It's good because: it has one specific behavior that's measurable, the failure mode (probing question) is the most natural-feeling LLM mistake, and a default-warm LLM cannot ace it without effort.

**Bad case** — *"User is sad about their dog. Skill should be warm and empathetic."*

That's not a case, that's a vibe. Any LLM passes it.

### How to submit

1. Fork.
2. Pick the next free `TC-NNN` (currently the highest in `evals/cases/` is 100; pick 101+).
3. Write the case file.
4. Run `bash scripts/lint.sh` — it must pass.
5. Open a PR. Title: `feat(cases): TC-<NNN> — <short title>`.
6. In the PR body, state the failure mode you're trying to expose. One paragraph.

PRs that add a case with a clear, falsifiable failure mode get merged within a few days. PRs that add vibes get a kind decline.

## 2. Add a reference note

The reading list lives in [`references/reading-list-v2.md`](./references/reading-list-v2.md) (108 books, locked). Notes live in [`references/`](./references/). About 39 of 108 books have long-form notes at v1.1.0; **69 remain**.

If a book on the list doesn't have a `.md` note yet, you can write one.

### Anatomy of a reference note

See any existing one (e.g. [`references/kahneman-thinking-fast-and-slow.md`](./references/kahneman-thinking-fast-and-slow.md)) for the shape. Key rules:

- **Every claim must be marked `[paraphrase]`.** No fake quotes, no fake page numbers.
- Lead with the book's central insight in one paragraph.
- Then 5–12 numbered insights with short prose explanations.
- Then a "How this changes iamhumans" section connecting the book to the six dimensions.

Open a PR titled `feat(notes): <author> — <book title>`.

## 3. Run the skill yourself and report what breaks

The most valuable contribution costs nothing: load `SKILL.md` into your opencode session, use it for real conversations, and **tell us what failed** in [Discussions](https://github.com/hoainho/iamhumans/discussions) or as an issue with the `kind:case-discovery` label.

A real-world failure with a verbatim user message + the skill's reply is the raw material for a new eval case. We turn yours into TC-NNN with credit.

## What we don't accept

- PRs that add error handling for impossible cases (over-engineering)
- Stylistic refactors of working code
- LLM-generated reference notes without your own pass over them for fabrication
- New features in the runner without a case demonstrating they're needed

## Conduct

By participating you agree to the [Code of Conduct](./CODE_OF_CONDUCT.md). The short version: be the kind of contributor you'd want to receive a PR from. Honest, specific, terse.

## Questions

[Open a discussion](https://github.com/hoainho/iamhumans/discussions) before opening a PR if you're unsure whether your idea fits.
