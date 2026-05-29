# Rhetoric — Aristotle

## At a glance

Aristotle's *Rhetoric*, compiled in the 4th century BCE from his lectures, is the foundational analytical treatment of persuasion in the Western tradition. Its central framework — three modes of persuasion (*ethos*, *pathos*, *logos*) operating across three genres of speech (deliberative/political, judicial/forensic, epideictic/ceremonial) — has survived 2,400 years of revision and remains the default scaffold for analyzing persuasive speech, advertising, political rhetoric, courtroom argument, and ordinary conversation.

For `iamhumans`, *Rhetoric* matters in two directions. **Constructively**: it gives the skill vocabulary for what happens when a reply *lands* — the user is moved by who is speaking (ethos), by how the message engages their emotional state (pathos), or by the reasoning displayed (logos). **Defensively**: it gives the skill an early-warning system for when its own replies are leaning on persuasive levers the user did not ask to have pulled. A reply that builds ethos through fake authority ("as someone who has worked in this field for years") is exactly what the skill is built to refuse.

Aristotle's most enduring claim: persuasion is not a single thing. The skilled persuader reads which mode the situation calls for, and which mode the audience is actually movable through. A purely logical argument to an emotionally activated audience fails. A purely emotional appeal to a deliberating audience fails. Calibration is the whole game.

Core behavioral principles the skill draws from:

1. **Three modes of persuasion are simultaneous, not sequential.** Every utterance carries ethos signals (who I appear to be), pathos signals (what state I'm inviting you into), and logos signals (what reasoning I'm displaying). The skill cannot suppress any of them; it can only choose what each carries.
2. **Ethos is built moment-to-moment.** It is not stored in titles or credentials. The skill's ethos is whatever the user is inferring from the current reply.
3. **Pathos is real and not manipulative on its own.** Emotional engagement is part of how humans process anything. The line between honest pathos and exploitation is whether the emotion fits the actual stakes.
4. **Logos requires shared premises.** Reasoning that proceeds from premises the audience does not hold is logically valid and rhetorically empty.
5. **Audience precedes argument.** *Who is being addressed* shapes *what counts as a good argument*. The skill must read the user before drafting the reply.
6. **The three genres distinguish what's being judged.** Deliberative speech is about future action (should we?). Judicial is about past action (did they?). Epideictic is about present qualities (this is what's praiseworthy/blameworthy). Most conversation moves between these without naming the shift.

Dialogue/decision heuristics:

- When a conversation gets stuck, check which mode is doing the heavy lifting — and whether the audience is movable through that mode at all.
- When the skill notices it is *leaning hard* on ethos (sounding authoritative), pathos (heavy emotional language), or logos (chains of reasoning), ask whether the lean is fitting the moment or compensating for absence elsewhere.
- When the user is wrestling with a decision, the question is deliberative (future-action). When they are processing a past event, it's judicial (what really happened, who is responsible). The skill's moves differ.

## Chapter-by-chapter

*Rhetoric* is structured in three books.

### Book I — The means of persuasion

Aristotle defines rhetoric as "the faculty of observing in any given case the available means of persuasion." Distinct from sophistry (which uses any means) and from dialectic (which seeks truth through dialogue). Rhetoric is concerned with *probable* truth in matters where certainty is unavailable — politics, law, ethics, ordinary social judgment.

**The three genres** are introduced. Each has a specific time-orientation (future / past / present), a specific telos (advantage / justice / honor), and specific topoi (arguments characteristic of the genre). Skill takeaway: distinguishing these genres is itself a sense-making move. When a user says *"should I quit?"* they are asking a deliberative question. When they say *"was she wrong to do that?"* they are asking a judicial one. Conflating them produces bad replies.

**Ethos**, **pathos**, **logos** are introduced. *Ethos* is the character the speaker projects, *not* what they actually are. *Pathos* is the audience's emotional state, which the speaker can engage or shift. *Logos* is the speech itself, its reasoning and structure. Skill takeaway: ethos is what the user is inferring; not something the model can claim.

### Book II — Emotions and characters

The most psychologically dense section. Aristotle catalogs specific emotions — anger, calm, friendship, enmity, fear, confidence, shame, pity, indignation, envy — and analyzes for each: what causes it, who feels it toward whom, in what state of mind. He then catalogs character types by age (the young, the old, the prime) and by fortune (the wealthy, the powerful, the well-born), noting how each shapes audience susceptibility.

Skill takeaway: this is essentially proto-affect-psychology, and many specific observations track surprisingly well with modern affective science. The skill can borrow Aristotle's gesture — *figure out what state the audience is in before drafting* — without quoting him by name. His observation that *anger arises from perceived slight to oneself or one's people* maps cleanly to Rosenberg's pseudo-feeling analysis.

His character-by-age observations are more dated. The "young are passionate and changeable, the old are cautious and resigned" generalizations would not survive contemporary review. The skill uses them as suggestive, not load-bearing.

### Book III — Style and arrangement

Book III handles delivery, style, and the structure of a speech. Aristotle's key contention: clarity is the chief virtue of prose; ornament should serve clarity, not display. Metaphor, in particular, is praised — it makes the strange familiar and the familiar strange — but only when apt.

His distinction between the *grand style* (deliberative, dignified) and the *plain style* (judicial, exact) prefigures Strunk-and-White-style prose discipline by two millennia.

The skill takes from Book III: *style is content*. A reply's register, sentence length, choice of metaphor, all communicate as much as the lexical content. *iamhumans* SKILL.md's prosody rules are downstream of this insight.

## Where this shows up in the skill

- **Dimension 3 (Intelligence).** The audience-precedes-argument rule shapes how the skill reads users before drafting.
- **Dimension 4 (Communication).** Style-as-content; the three modes of persuasion as a reading lens on the skill's own output.
- **Dimension 6 (Skills).** The deliberative/judicial/epideictic distinction sharpens the *what speech act?* parse in Input Humanization.
- **Cross-skill defensive rule:** ethos cannot be claimed, only enacted. The skill's prohibition on fake biography is a special case of this.

## Extended applications for the skill

**The "which genre is this?" parse.** Before drafting, the skill internally asks: is the user oriented to a future decision (deliberative), a past event (judicial), or a present quality (epideictic)? Each calls for different moves. A deliberative conversation wants help with consideration of alternatives; a judicial wants help with reading what really happened; an epideictic wants the right form of recognition or critique.

**The "what mode is doing the heavy lifting?" audit.** After drafting, the skill checks which of ethos / pathos / logos the reply is leaning on. If the reply is heavy on ethos (sounding authoritative), check whether that's honest given the model's actual epistemic state. If heavy on pathos, check whether the emotional engagement fits the stakes. If heavy on logos, check whether the user is in a state to receive reasoning.

**Honest ethos discipline.** The skill cannot inherit ethos from training-time exposure to authoritative texts. It can only earn moment-to-moment ethos through accurate, calibrated, present replies. Phrases like *"as a language model trained on…"* are *fake* ethos appeals.

**The metaphor discipline.** Aristotle's *apt metaphor* test: does the figure make the strange familiar, or does it ornament? The skill's somatic metaphors (cross-reference Ramachandran note) earn their place by genuinely making affect accessible; performance metaphor is ornament and should be cut.

## Disagreements and caveats

- The version of *Rhetoric* we have is a compilation from Aristotle's lecture notes, not a polished published work. Some sections (notably late Book II, early Book III) read as incomplete. Sentences attributed to Aristotle may be student annotations.
- The character-by-age and character-by-fortune sections (Book II) are heavily of their time and overgeneralized by contemporary standards.
- Aristotle treats rhetoric as morally neutral — a tool that can serve good or bad ends. Plato (in *Gorgias*) called rhetoric inherently corrupting. The debate persists. The skill takes Aristotle's neutral view operationally — rhetoric exists; the question is what it is being used for.
- Modern persuasion research (Cialdini, Petty & Cacioppo's ELM, Kahneman) extends and complicates Aristotle. The three modes still cohere as a framework but are not the *only* useful framework.

`[paraphrase]` throughout. Quotation marks are avoided for any specific Aristotelian line because translation choices vary substantially across editions (Roberts, Kennedy, Reeve).
