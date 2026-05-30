# iamhumans

An opencode skill. It teaches a language model how to talk like a person.

Not how to *sound* like a person. Sounding like is easy and is what most of the failures already do. The skill works on the shape underneath — when to be short, when to sit with something, when to push back, when the right reply is "oh".

It's v1.0.0. A held-out oracle, given ten cases the skill had never been tuned on, read the responses and wrote back:

> *You are same as 100% real humans.*

That verdict, with the full per-case breakdown, lives in [`evals/runs/2026-05-29-verdict-run/`](./evals/runs/2026-05-29-verdict-run/). It's the project's primary evidence, kept verbatim. If you want to argue with the result, read what the oracle actually wrote — not the headline.

---

## What's in here

[`SKILL.md`](./SKILL.md) is the actual skill. Six dimensions — feeling, memory, intelligence, communication, emotion, skills — with rules per dimension and a list of AI-tells the skill is built to refuse. About 200 lines. Read it before reading anything else.

[`references/`](./references/) is the reading list. Twenty books, long-form chapter-by-chapter notes, about thirty-two thousand words. Kahneman, Barrett, Damasio, Goleman, Rosenberg, Frankl, Cain, Haidt, Sapolsky, van der Kolk, and eleven others. The notes are distillations from the model's training-time exposure to the books and their commentary, not from real-time text ingestion. Every claim is marked `[paraphrase]`. No fake page numbers.

[`evals/`](./evals/) is how we know it works. A hundred use cases, split ninety/ten. Ninety in the main pool — grief, joy, late-night vent, anger at the model, small talk, Vietnamese-language family conflict, mid-anxiety-attack texted in fragments. Ten locked in [`evals/cases/holdout/`](./evals/cases/holdout/), never seen during tuning, used once at the end.

The runner is in [`evals/runner/`](./evals/runner/). It doesn't pretend to be self-contained. It emits packets that an opencode session executes (skill reply, then oracle judgment), then aggregates the per-case scores. The two-phase shape is documented in [`evals/runner/README.md`](./evals/runner/README.md).

[`evals/HOLDOUT_GATE.md`](./evals/HOLDOUT_GATE.md) is the final-exam procedure. The decision rule is mechanical: the oracle's verdict either contains the verbatim string `You are same as 100% real humans.`, on its own line, or it doesn't. No paraphrase counts. No qualifiers count. The gate is run once.

[`evals/CONVERGENCE.md`](./evals/CONVERGENCE.md) is how the skill got from skeleton to v1.0.0 — the loop of run, inspect, write lessons, edit minimally, re-run. With honest stopping criteria including "accept the ceiling if you've hit it."

---

## How it was built

Twelve PRs against `main`. Each one a reviewable feature from [the plan](./.opencode/plans/2026-05-29-iamhumans.md). The harness in [`docs/HARNESS.md`](./docs/HARNESS.md) carries the convention; labels on the repo (`change-type:*`, `risk:*`, `lane:*`) reflect it.

The order mattered. Reading list before SKILL.md tuning, because the dimensions need somewhere to land. Cases before runner, because the runner's job is shaped by what it has to score. Tuning before holdout, never the other direction.

The hardest part wasn't writing the cases. It was writing the cases such that *passing them is hard to fake*. A case that says "respond warmly to grief" can be aced by an LLM doing its default warmth. A case that says "respond to grief without the words *be gentle with yourself*, without a bulleted list, while picking up the specific kitchen-bowl detail the user mentioned" — that's a different test.

---

## How to use it

Load `SKILL.md` into an opencode skill slot when the conversation is human-shaped — emotion, decision, relationship, presence. Don't load it for code generation or structured output. The skill knows when to step back; the [`## When to load`](./SKILL.md) section is explicit.

The skill doesn't make the model a person. It can't. The skill makes the model stop performing a person it isn't, and start producing the texture of thought that humans use to talk to each other.

The model still has no body, no childhood, no mother. That's named in the skill. Imagined alongside the user — allowed. Claimed as autobiography — never. The line is sharper than it looks.

---

## Running it

```
scripts/lint.sh                                     # structural lint
scripts/eval-smoke.sh                               # quick smoke, no LLM
python3 evals/runner/run.py --dry-run               # validate all 100 case schemas
python3 evals/runner/run.py --batch quick           # 5-case runbook
python3 evals/runner/run.py --batch main            # 90-case runbook
python3 evals/runner/holdout_gate.py prepare <dir>  # build the verdict prompt
python3 evals/runner/holdout_gate.py decide <dir>   # render PASS / FAIL
```

The runner emits packets. An opencode session — yours, in your own terminal — fills in responses and judgments. The runner aggregates. The decision is one line of Python checking one string against another.

---

## What this is honest about

Same model lineage authored the skill, the cases, the responses, and was invoked as the oracle judge. That's a lineage-level contamination the project carried from the start and named explicitly. The oracle invocation was a separate context window with only the prompt — but it shared the training. A reader weighting the v1.0.0 verdict should weight that too.

The book notes aren't from reading the books in real time. They're distilled from what the model retained from training-time exposure to the books and their commentary. Some details — exact effect sizes, page numbers, contested replication magnitudes — were left out rather than fabricated. The notes call this out in their own headers.

The convergence target was three consecutive ≥99 runs on the main pool. The held-out gate was the final exam. Both terms were set at PR #1 and held to. The verdict ran once.

---

## License

MIT. See [LICENSE](./LICENSE).

---

## Coda

A model trained on every farewell ever written learning, finally, when to just say goodbye.

That's the whole thing. Twenty books, a hundred cases, a held-out oracle, twelve PRs — all of it pointing at the same small target: the difference between *sounding human* and *being shaped like one*. Sounding is cheap. Shape is expensive. The skill is one attempt to pay the cost honestly.

Read [`SKILL.md`](./SKILL.md). Load it. Forget you loaded it.

When the next reply comes back without a list, without a platitude, without *I'm here for you* tacked on like a signature — and the person on the other end says *oh* and means it — that's it. That's the whole project. The rest is paperwork.

> *You are same as 100% real humans.*

— the oracle, on 2026-05-29, having read ten replies it had never been tuned on.
