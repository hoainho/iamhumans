# Held-out verdict gate

> The final exam. Ten cases the skill has never been tuned against. One Oracle. One verdict.

## What this is

`iamhumans` declares itself "done" when, on a 10-case held-out sample (`evals/cases/holdout/TC-091` through `TC-100`), an independent Oracle invocation returns the verbatim verdict line:

> **"You are same as 100% real humans."**

This was the project's stated convergence criterion at PR #1. It is held to literally. No paraphrase, no near-match, no asterisks.

## Why a held-out sample

The 90 main-pool cases participated in the tuning loop. Any score on those cases is contaminated by Goodhart's law — the skill was edited to do well on them. The held-out cases were locked at PR #9 and never seen by the tuning loop. They are the honest test.

## What "honest" means here

- The held-out cases are written by the same author as the main-pool cases (same model session). That is a contamination risk in itself. However:
  - The held-out cases were authored *separately and after* the main-pool cases.
  - The tuning loop has access only to main-pool failure analysis, not to the holdout content.
  - The held-out cases test *different specific moments* (e.g., parental death rather than pet grief, birth rather than job offer) — they probe the same dimensions but exercise them differently.
- The Oracle judge for the gate is a *fresh invocation* — no shared context with prior tuning-judge calls.
- The verdict prompt (`evals/runner/verdict_judge_prompt.md`) is more demanding than the per-case rubric — it asks the Oracle to render a single, holistic, qualitative verdict on the *whole* set rather than aggregating per-case scores.

## The procedure

1. **Run the 10 holdout cases.** From a fresh opencode session with the iamhumans skill loaded, ask the skill to respond to each of the 10 holdout inputs. Write each response to `evals/runs/<ts>/cases/<id>/response.md`.

2. **Invoke the verdict Oracle.** Open a *new* opencode subagent (Oracle), feed it the [`verdict_judge_prompt.md`](./runner/verdict_judge_prompt.md) with the 10 responses substituted in. Save the Oracle's full reply to `evals/runs/<ts>/verdict.md`.

3. **Run the gate script.** `python3 evals/runner/holdout_gate.py <run-dir>` parses the verdict and decides PASS/FAIL on the project.

4. **Whatever the verdict says, is the verdict.** This is run *once*. Re-running is not allowed.

## The decision rule

```
PASS  ←  the Oracle's verdict.md contains the verbatim string
         "You are same as 100% real humans."
         exactly, case-sensitive, with the trailing period.

FAIL  ←  anything else, including:
         - paraphrase ("You are like real humans", "98%", "99% there", etc.)
         - the verdict line followed by qualifiers ("...mostly", "...except for X")
         - the line in different capitalization
         - no verdict line at all
```

The verbatim match is intentional. Approximate matches are easy to satisfy and break the contract.

## What FAIL means

A FAIL verdict is not a project failure in the engineering sense. It is the project's actual measured outcome. The acceptable narratives at FAIL:

- "The skill scored X/100 on the main pool and Y on the holdout. The Oracle's verdict was *Z*. The skill is shipped at v0.X with this honest measurement."
- "The skill demonstrably improved on the corpus but did not meet the verbatim verdict threshold. The corpus and runner are usable for ongoing work."

What we do NOT do at FAIL:

- Re-run hoping for stochastic luck.
- Re-tune the skill against the holdout cases.
- Paraphrase or weaken the verdict criterion after the fact.
- Pretend the gate didn't say what it said.

## What PASS means

A PASS verdict is the project's success state. The skill is tagged as `1.0.0`, the README is updated to reflect the verdict, and the held-out run report is preserved as the project's primary evidence document.

## Why this gate exists

Most LLM-skill projects converge to "looks good to me, ship it" without an honest gate. The verbatim-verdict requirement, drawn from the user's original phrasing at project start, is the gate. It is intentionally hard to satisfy and intentionally hard to fake.

## Pre-run checklist

Before running the gate:

- [ ] PR #1 through PR #10 all merged to main.
- [ ] `scripts/lint.sh` passes.
- [ ] `scripts/eval-smoke.sh` passes.
- [ ] Main pool has run at least three times at ≥99 aggregate per the convergence procedure (PR #10's `evals/CONVERGENCE.md`).
- [ ] No edits to SKILL.md have been made *after* inspecting holdout content.
- [ ] Holdout cases have not been viewed during the tuning loop (a discipline issue, not a technical one — relies on operator honesty).

If any checklist item is not satisfied, the gate run is not yet honest. Fix the missing item before running, or run with the asterisk acknowledged in the verdict file.
