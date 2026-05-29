# Reading list — the twenty books

> The principles in [`SKILL.md`](../SKILL.md) draw from these twenty works. Each book gets long-form chapter-by-chapter notes in `references/<slug>.md` (added across PRs #3–#6).

> **Important methodological caveat:** these notes are *distillations* informed by the model's training-time exposure to summaries, reviews, excerpts, and discussions of these books. They are not derived from real-time full-text ingestion. Where a claim is paraphrased rather than directly attributable, the note marks it `[paraphrase]`. Where a claim is contested or interpretation-dependent, the note marks it `[contested]`.

## The twenty (locked at plan time, 2026-05-29)

1. **Thinking, Fast and Slow** — Daniel Kahneman ([notes](./thinking-fast-and-slow.md))
2. **How Emotions Are Made** — Lisa Feldman Barrett ([notes](./how-emotions-are-made.md))
3. **Sapiens** — Yuval Noah Harari ([notes](./sapiens.md))
4. **The Social Animal** — Elliot Aronson ([notes](./the-social-animal.md))
5. **Influence: The Psychology of Persuasion** — Robert Cialdini ([notes](./influence.md))
6. **Emotional Intelligence** — Daniel Goleman ([notes](./emotional-intelligence.md))
7. **Nonviolent Communication** — Marshall Rosenberg ([notes](./nonviolent-communication.md))
8. **Man's Search for Meaning** — Viktor Frankl ([notes](./mans-search-for-meaning.md))
9. **Predictably Irrational** — Dan Ariely ([notes](./predictably-irrational.md))
10. **Descartes' Error** — Antonio Damasio ([notes](./descartes-error.md))
11. **The Body Keeps the Score** — Bessel van der Kolk ([notes](./the-body-keeps-the-score.md))
12. **The Righteous Mind** — Jonathan Haidt ([notes](./the-righteous-mind.md))
13. **Behave** — Robert Sapolsky ([notes](./behave.md))
14. **The Tell-Tale Brain** — V. S. Ramachandran ([notes](./the-tell-tale-brain.md))
15. **Mindset** — Carol Dweck ([notes](./mindset.md))
16. **Atomic Habits** — James Clear ([notes](./atomic-habits.md))
17. **Quiet** — Susan Cain ([notes](./quiet.md))
18. **The Power of Habit** — Charles Duhigg ([notes](./the-power-of-habit.md))
19. **Stumbling on Happiness** — Daniel Gilbert ([notes](./stumbling-on-happiness.md))
20. **Crucial Conversations** — Patterson, Grenny, McMillan, Switzler ([notes](./crucial-conversations.md))

## Why these twenty (selection rationale)

The selection optimizes for **breadth across the six dimensions** the skill operates on, not for the most-cited or most-recent books in any single field.

| Dimension | Primary contributors |
|---|---|
| **Feeling** (somatic affect, embodied cognition) | Barrett, Damasio, van der Kolk, Sapolsky |
| **Memory** (autobiographical, semantic, working) | Kahneman, Damasio, van der Kolk, Gilbert |
| **Intelligence** (System 1 / System 2, calibration, bias) | Kahneman, Ariely, Gilbert, Goleman |
| **Communication** (NVC, repair, framing) | Rosenberg, Patterson et al., Cialdini, Goleman |
| **Emotion** (affect regulation, empathy, valence) | Goleman, Barrett, Rosenberg, Frankl |
| **Skills** (social maneuvers, conflict, motivation) | Aronson, Cialdini, Dweck, Clear, Duhigg, Cain, Haidt |

The mix is intentionally cross-paradigm: neuroscientific (Sapolsky, Damasio, Ramachandran), social-psychological (Aronson, Cialdini, Haidt, Dweck), affect-theoretic (Barrett, Goleman), trauma-informed (van der Kolk, Frankl), behavioral-economic (Kahneman, Ariely, Gilbert), and practice-oriented (Rosenberg, Patterson et al., Clear, Duhigg, Cain).

Two books — *Sapiens* and *Man's Search for Meaning* — sit slightly outside the cognitive-science cluster and earn their slot by addressing the **why** question: why a species so unreliable in its individual cognition can produce meaning, cooperation, and the kind of shared narrative the skill is trying to fit inside.

## What we explicitly excluded and why

- **Pop self-help with thin empirical grounding.** (Excluded by default — every selected book has either peer-reviewed primary research behind it or is itself a clinical/practitioner synthesis with citations.)
- **Books that are primarily about LLMs, AI alignment, or anthropomorphism.** This skill is about *humans*, not about *how AI should mimic humans*. The latter is downstream.
- **Single-author manifestos with no engagement with opposing views.** (E.g., some popular productivity titles.)
- **Books we couldn't credibly distill from training-time exposure.** If the notes would be vague paraphrase only, the slot went to a book the model genuinely retains structured detail on.

## Replacements considered and rejected

| Considered | Why we picked the one in the list instead |
|---|---|
| *Daring Greatly* (Brené Brown) | Overlaps significantly with the vulnerability work that's already implicit in Rosenberg + Frankl + Barrett. |
| *Drive* (Daniel Pink) | Motivation coverage already lives in Dweck + Clear + Duhigg. |
| *The Righteous Mind* vs. *Moral Tribes* (Joshua Greene) | Haidt's six-foundations framework is more directly action-guiding for the skill's "navigate disagreement" use cases. |
| *Mindfulness in Plain English* (Bhante Gunaratana) | Mindfulness coverage is downstream of attention/affect work in Goleman, Barrett, van der Kolk. |
| *Status* (Will Storr) | Cialdini and Haidt cover most status-related principles relevant to conversation. |
| *Atomic Habits* vs. *Tiny Habits* (BJ Fogg) | Clear's structure (cue/craving/response/reward) is cleaner for skill-internal taxonomy than Fogg's. |

## How the notes are structured (template)

Each `references/<slug>.md` follows this skeleton:

```
# <Title> — <Author>

## At a glance
- one-paragraph thesis
- three to seven core behavioral principles
- two to four dialogue/decision heuristics this skill draws from

## Chapter-by-chapter
<one section per chapter or major part of the book; what claim, what evidence, what the skill takes from it>

## Where this shows up in the skill
- cross-references into SKILL.md sections and dimension cards

## Disagreements and caveats
- where the book is contested, where the model is uncertain about a paraphrase
```

The chapter-by-chapter section is the longest. Word-count target per book: **2 000–3 000 words**, of which ≥60% is the chapter-by-chapter walk.

## How the notes feed the skill

The skill does **not** load all twenty notes into the active prompt — that would blow the context budget for any actual conversation. Instead:

- `SKILL.md` itself stays compact and references the notes by file.
- The notes function as a **retrievable knowledge base**: when the skill (or a maintainer auditing a failed eval case) needs to ground a principle, the relevant book is read on demand.
- The eval runner cites which note motivated each rubric criterion.
