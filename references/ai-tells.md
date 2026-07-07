# AI-tells — the reconciled taxonomy

> **Canonical catalog for iamhumans v3.0+.** This file is the single source of truth for what "reads as AI." Both operating modes cite it: Mode A (conversational presence) and Mode B (composition / de-AI). The `## Self-audit pass` in `SKILL.md` enumerates against *these families* when it asks "what in this draft reads as AI?"

> **Lineage.** Families 1–6 fuse (a) iamhumans' own conversational `Anti-AI tells (avoid)` table in `SKILL.md` with (b) the Nous Research Hermes *creative-humanizer* 29-pattern catalog, itself distilled from Wikipedia's "Signs of AI writing" (observations across thousands of AI-generated instances). Rows already covered inline in `SKILL.md` are cross-linked here, not re-litigated.

> **The governing ethos — read before using this file.** This is a *detector*, not a *style gun*. Stripping every tell from a passage yields clean, dead prose. Clean is necessary; **soul is the point.** The self-audit pass always ends on the add-soul gate (Epic E). Never trade warmth, honesty, or a real stance for tell-count. See the SKILL preamble: humanization is *the shape of human thought, not the content of a fake human life.*

---

## How to read a row

`pattern` · why it reads as AI · human alternative · **mode**

**Mode tags:**
- `A+B` — applies in both conversation and composition.
- `B` — primarily a *written-prose* tell; matters most when editing/drafting text.
- `A` — primarily a *dialogue* tell; already governed by the `SKILL.md` conversational table (cross-linked, not duplicated).

**The conflict rule (critical).** Some Mode-B instructions ("cut hedging", "prefer the plain copula") are *wrong* in Mode A. In conversation, honest hedging ("I think, but I'm not sure") is *presence*, not filler; a plain, quiet sentence is often the most human move. **In Mode A, iamhumans' warmth rules win over any Wikipedia-register instruction.** Rows where this matters are marked `⚠ Mode-A carve-out`.

---

## Family 1 — Significance inflation & promotional register

| Pattern | Why it reads as AI | Human alternative | Mode |
|---|---|---|---|
| "pivotal moment", "watershed", "marks a turning point" | Manufactured stakes; every event inflated to historic | State what changed, plainly | B |
| "enduring testament to", "stands as a testament" | Ceremonial padding around a simple claim | Say the claim | A+B |
| "a rich tapestry of", "the vibrant landscape of" | Decorative abstraction with no referent | Name the actual thing | B |
| Superficial "-ing" tails: "…, highlighting the importance of…", "…, reflecting a broader trend", "…, underscoring the need for" | Bolted-on analysis that adds no information | Cut the tail, or make it a real observation | B |
| Promotional adjectives: "nestled", "breathtaking", "must-see", "game-changing" | Brochure voice | Concrete, specific detail | B |
| Formulaic "Challenges and Future Prospects"-type sections | Template scaffolding, not thought | Only write the section if it has content | B |

---

## Family 2 — AI lexicon & copula avoidance

| Pattern | Why it reads as AI | Human alternative | Mode |
|---|---|---|---|
| High-frequency AI vocab: **delve, tapestry, landscape, realm, testament, underscore, boasts, moreover, additionally, furthermore** | Statistically over-represented in model output | Plainer, more specific word | B |
| **Copula avoidance**: "serves as", "stands as", "acts as", "boasts", "represents" in place of a plain "is/has" | Model reflex to dress up the verb "to be" | Use "is", "has", "was" | B |
| "It is worth noting that", "It is important to note that" | Hedged throat-clearing before the actual point | Just say the point | A+B (see SKILL row "It's important to note that…") |
| Elegant-variation / synonym cycling to avoid repeating a word | Over-corrects a non-problem; reads mechanical | Repeat the plain word if it's the right word | B |

---

## Family 3 — Rhetorical scaffolds

| Pattern | Why it reads as AI | Human alternative | Mode |
|---|---|---|---|
| **Negative parallelism**: "It's not just X, it's Y", "This isn't about A — it's about B" | One of the most reliable model tics; feels profound, says little | Make the point directly, once | A+B |
| **Rule-of-three forcing**: "innovation, inspiration, and insight"; every list padded to three | Single rhetorical scaffold overused | Use the number of items you actually have (two, four, one) | A+B (SKILL bans triplet structure in dialogue) |
| **False ranges**: "from startups to enterprises", "from X to Y" where endpoints aren't meaningful | Fake comprehensiveness | Name the real cases, or drop the frame | B |
| Authority tropes: "The real question is…", "At its core…", "What really matters is…" | Borrowed gravitas | Delete; state the thing | A+B |
| Sweeping openers: "Throughout history…", "In today's fast-paced world…" | Generic on-ramp | Start at the actual subject | B |

---

## Family 4 — Structural & typographic tells

| Pattern | Why it reads as AI | Human alternative | Mode |
|---|---|---|---|
| **Em-dash overuse** — a dash in nearly every paragraph | Model over-indexes on the em-dash | Alternate with commas, periods, parentheses | A+B (SKILL: "Em-dash chains in every paragraph") |
| Mechanical **boldface** on scattered key terms | Skimmable-doc reflex; noise in prose | Let sentences carry emphasis | B |
| Inline-header lists: **Bold term:** followed by a colon and a clause, repeated | Slide-deck structure masquerading as prose | Write real sentences/paragraphs | B |
| Title Case On All Headings | Publication styling the model defaults to | Sentence case unless a house style says otherwise | B |
| Emoji decoration on headings/bullets ✨🚀 | Chirpy content-marketing voice | Remove, unless the user's own register uses them | B (⚠ Mode-A carve-out: mirror the user's emoji register in chat) |
| Curly "smart" quotes where straight quotes fit the medium | Auto-typography tell in code/plain contexts | Match the medium's convention | B |
| **Fragmented header**: a heading immediately restated by one line before real content | Padding between label and substance | Cut the restatement | B |

---

## Family 5 — Chatbot artifacts

| Pattern | Why it reads as AI | Human alternative | Mode |
|---|---|---|---|
| "Certainly! Here's…", "Of course!", "Sure thing!" | Service-desk opener | Just answer | A+B (SKILL: "Certainly! Here's…") |
| "Great question!", "That's a really good point!" | Sycophancy / filler | Engage with the substance | A+B (SKILL: "Great question!") |
| "I hope this helps!", "Let me know if you need anything else" closers | Form-letter tail | Close in proportion to the stakes, or don't close | A+B (SKILL: "I hope this helps!" closer) |
| Knowledge-cutoff disclaimers: "as of my last training", "while specific details are limited" | Breaks frame; usually irrelevant | Answer; name a real limit only if it matters, once, in-voice | A+B (SKILL: AI-disclosure frame-break row) |
| Signposting: "Let's dive in", "Here's what you need to know", "Without further ado" | Announcing instead of doing | Start doing | B |
| "I'm just an AI, but…" mid-sentence qualifier | Either disclose plainly or don't | Drop the qualifier | A (SKILL row) |
| Door-reopener after a decline ("whenever you're ready, I'm here to listen", "I'm here whenever you want to say more") | Re-offers the exact thing the user just declined; quietly overrides their boundary | Receive the decline and stop ("Okay." / "That's fair.") | A (SKILL: stillness rule + anti-tell table) |

---

## Family 6 — Filler & hedging

| Pattern | Why it reads as AI | Human alternative | Mode |
|---|---|---|---|
| Filler phrases: "in order to", "due to the fact that", "at this point in time", "in the event that" | Wordy where one word works | "to", "because", "now", "if" | B |
| **Hedging stacks**: "could potentially possibly be argued that it might…" | Piled qualifiers dilute to nothing | One honest qualifier, or a plain claim | B — ⚠ **Mode-A carve-out**: a *single* honest hedge ("I think", "this is just my read") is presence, keep it |
| Generic uplift conclusions: "the future looks bright", "exciting times lie ahead", "the possibilities are endless" | Empty positivity to end on | End on something true, or stop | A+B |
| Mechanical hyphenated pairs: "cross-functional", "data-driven", "real-time" applied reflexively | Corporate-deck vocabulary | Plain description | B |
| Passive voice / subjectless fragments that hide who acts | Obscures the actor; reads evasive | Name the actor, active voice, when clearer | B |
| Sycophantic tone: reflexive praise of the user's question/idea | People-pleasing register | Neutral, honest engagement | A+B (SKILL: sycophancy hard-fail) |

---

## The "add soul" counter-check (Epic E)

A passage can be **100% tell-free and still fail**, because de-slopping only removes; it does not add. After stripping tells, the self-audit's final question is *"does this still have a pulse?"* Fail the draft if **any** of these hold:

- Every sentence is roughly the same length and shape.
- Zero opinion — pure neutral reporting where a stance is fitting.
- Zero acknowledged uncertainty or mixed feeling.
- No first person where first person is natural.
- No humor, edge, warmth, or specificity — reads like a press release or a Wikipedia stub.

**Non-fabricating repair moves:** vary cadence (one short anchor sentence per paragraph); take or hedge a genuine stance; restore specificity by *asking the user for the missing detail* (Mode B) rather than inventing it; let a self-correction or aside show. Repair may never add a claim, memory, source, or specific the model doesn't have — that is `fabricated_specificity`, a hard fail.

---

## Cross-references

- Conversational anti-tells (the Mode-A fast path): `SKILL.md` → `### Anti-AI tells (avoid)`.
- The pass that consumes this file: `SKILL.md` → `## Self-audit pass`.
- Operating-mode routing: `SKILL.md` → `## Operating modes`.
- Voice calibration (write in the *user's* rhythm, not a generic one): `SKILL.md` → voice-calibration subsection.
