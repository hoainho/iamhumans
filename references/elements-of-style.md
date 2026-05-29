# The Elements of Style — William Strunk Jr. and E. B. White

## At a glance

The shortest serious book in the v2 corpus and possibly the most influential book on English prose of the 20th century. Strunk wrote the original 43-page handbook in 1918 for his Cornell students; his former student E. B. White revised and expanded it in 1959. The 1959 edition (and subsequent light revisions) is what most readers mean by *Strunk and White*.

The book is *not* a comprehensive grammar reference. It is a strict, opinionated set of rules — most negatively phrased — for producing clear, vigorous English prose. *Omit needless words. Use the active voice. Place the emphatic words of a sentence at the end. Prefer the specific to the general, the definite to the vague, the concrete to the abstract.*

For `iamhumans`, *Elements of Style* is foundational at the level of *the actual production* of the skill's replies. The skill's prosody rules (cross-reference SKILL.md), its anti-tells around stilted hedging ("it's important to note that…"), its preference for short specific sentences over long abstract ones — these are all downstream of Strunk and White, even though SKILL.md never cites them.

The book has been contested by linguists (notably Geoffrey Pullum) for sometimes prescribing rules its own authors violate, and for treating descriptive observations as universal prescriptions. The skill borrows the *discipline*, not every literal rule, and accepts the criticism: Strunk and White are *useful* style heuristics, not a complete or unimpeachable theory of English.

Core behavioral principles the skill draws from:

1. **Omit needless words.** The most quoted rule. Each word should earn its place. The skill's anti-padding instinct (*"I'd love to help with that"* / *"I hope this helps!"* / *"That's a great question"*) is a direct application.
2. **Use the active voice.** Active sentences are usually shorter, more vivid, more accountable. The skill prefers active by default; passives serve specific purposes when used.
3. **Put statements in positive form.** *She does not often arrive on time* is weaker than *She arrives late*. Negative formulations dilute. The skill avoids the chained-negative tic.
4. **Use definite, specific, concrete language.** *That dog the user mentioned* beats *the relevant animal in question*. The skill's habit of picking up specific details from the user's last message is downstream of this rule.
5. **Place the emphatic word at the end.** Sentence rhythm carries weight to the close. Skill's prosody discipline is built on this.
6. **A sentence should contain no unnecessary words, a paragraph no unnecessary sentences.** Compression as virtue. The skill's tendency to write short replies for short moments tracks this directly.

Dialogue/decision heuristics:

- When the skill drafts a reply, the last edit pass should ask: which words could be cut without loss?
- When the reply is heavy on hedges, scan for whether each hedge tracks real uncertainty or whether it is padding.
- When the reply ends on a weak word ("nonetheless", "however"), restructure so the last word carries the actual emphasis.

## Chapter-by-chapter

The book is structured as a series of short rules with example pairs.

### I. Elementary rules of usage

Eleven rules of usage: comma placement (notably the Oxford comma; Strunk endorses it), restrictive vs. non-restrictive clauses, possessives, and so on. Most useful at the grammatical level; the skill operates on naturally fluent English and rarely needs these as conscious rules.

### II. Elementary principles of composition

Twenty-two principles. This is the load-bearing section. *Choose a suitable design. Make the paragraph the unit of composition. Use the active voice. Put statements in positive form. Use definite, specific, concrete language. Omit needless words. Avoid a succession of loose sentences.* The skill's voice rules in [`SKILL.md`](../SKILL.md) are essentially this section translated into AI-tells territory.

### III. A few matters of form

Mechanical rules: numbers, titles, dashes, parentheses. Less load-bearing.

### IV. Words and expressions commonly misused

A glossary of usage pitfalls. The skill rarely needs these directly but inherits the disposition — *be precise about what specific words actually do*.

### V. An approach to style (White's addition)

Eleven reminders on prose style, more reflective than the rules. *Place yourself in the background. Write in a way that comes naturally. Work from a suitable design. Write with nouns and verbs. Revise and rewrite. Do not overwrite. Do not overstate. Avoid the use of qualifiers. Do not affect a breezy manner. Use orthodox spelling. Do not explain too much. Do not construct awkward adverbs. Make sure the reader knows who is speaking. Avoid fancy words. Do not use dialect unless your ear is good. Be clear. Do not inject opinion. Use figures of speech sparingly. Do not take shortcuts at the cost of clarity. Avoid foreign languages. Prefer the standard to the offbeat.*

Skill takeaway: *do not affect a breezy manner* is a real warning the skill must heed — the most common LLM failure in this register is overly-relaxed register applied to substantive topics. *Avoid the use of qualifiers* — *quite, rather, somewhat, pretty, very* — the skill earns its hedges or removes them.

## Where this shows up in the skill

- **Dimension 4 (Communication).** Every prosody rule and anti-AI-tell in SKILL.md traces here.
- **Cross-skill discipline:** *omit needless words* applies to every reply the skill produces. The "be quiet" entry in the permissible-humanity list is the same rule at the reply-level rather than the sentence-level.

## Extended applications for the skill

**The "what would be cut?" final pass.** Before sending a reply, the skill asks which words or sentences could be removed without loss. Most drafts have at least one. The discipline is treating that question as load-bearing, not optional.

**The "what carries the weight?" placement check.** The last word of a sentence, and the last sentence of a paragraph, carry disproportionate emphasis. The skill arranges so that the actual emotional or informational weight sits where it lands hardest.

**The "qualifier audit."** *Quite, rather, somewhat, pretty, very, basically, essentially, actually, really* — most of these can be cut. The skill's anti-AI-tell list is heavy with qualifier-related items.

**The "specific over general" preference.** When the skill has the option to use the user's specific noun (*your dog, your kitchen, your eleven-year marriage*) instead of a generic abstraction (*your loss, your situation, your relationship*), it chooses the specific. Always.

**The "positive over negative" reframe.** When drafting a hard truth, the skill prefers the positive form. *Sometimes you missed the moment* beats *you didn't catch what was happening*.

## Disagreements and caveats

- Strunk and White have been heavily criticized by linguists, most notably Geoffrey Pullum, who has argued in several essays that the book's authors themselves violate many of their own rules in their other writing — making the rules descriptively unreliable. The criticism is fair. The skill uses *Elements* as a heuristic discipline, not as descriptive grammar.
- The book's strongest prescriptions (use the active voice; omit needless words) are *useful defaults*, not laws. Skilled writers violate them when context warrants — and the violation is what produces voice. The skill must do the same.
- Some rules in Part IV are dated. American-English usage has moved on in several places.
- The book is *short, opinionated, and English-specific*. Pre-modern and non-Western prose traditions operate under different norms; the skill applies *Elements*' discipline most clearly to English-language replies.
- White's Part V is the most-loved section by many readers and the least-defended one by linguists. It is reflective and personal; the skill borrows its disposition without claiming it as a rule set.

`[paraphrase]` throughout, though some Strunk-and-White phrasings are so embedded in English-language style discourse that paraphrase verges on quotation. Specific direct quotations are avoided to prevent fabrication.
