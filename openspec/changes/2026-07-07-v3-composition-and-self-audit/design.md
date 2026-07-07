# Design: iamhumans v3.0 — Composition Mode + Self-Audit Engine

**Change ID:** 2026-07-07-v3-composition-and-self-audit

---

## Architecture overview

```
                         ┌───────────────────────────────────────┐
   incoming request ───► │  Operating-mode router (load time)     │
                         └───────────────┬───────────────────────┘
                       affect/relational │ explicit "edit this text"
                        signal → Mode A  │  → Mode B
             ┌─────────────────────────┐ │ ┌────────────────────────────┐
             │  MODE A                  │ │ │  MODE B                     │
             │  Conversational presence │ │ │  Composition / de-AI        │
             │  (all existing v2.9      │ │ │  input = supplied draft     │
             │   machinery, unchanged)  │ │ │  goal = human-sounding prose│
             └───────────┬──────────────┘ │ └──────────────┬─────────────┘
                         │                 │                │
                         └────────┬────────┴────────────────┘
                                  ▼
                 ┌──────────────────────────────────────┐
                 │  SHARED SELF-AUDIT ENGINE (Epic C+E)  │
                 │  runs on the DRAFT, before send       │
                 │  Q1: what reads as AI? (Epic B taxo)  │
                 │  Q2: rewrite so it doesn't            │
                 │  Q3: does it still have soul? (Epic E)│
                 │  ── internal, never surfaced ─────────│
                 └──────────────────┬───────────────────┘
                                    ▼
                              finalized reply
                                    ▲
                 Voice fingerprint (Epic D) ── feeds both the
                 draft step and the Q2 rewrite in both modes
```

**Design principle:** v3.0 is *additive to the pipeline's tail*, not a rewrite of its head. Mode A's entire existing forward pass (portrait → affect → register → module selection → prosody) is untouched. The new machinery sits at the **draft-review boundary**: a verification stage every reply now passes through. This is why the Mode-A regression gate is realistic — we are adding a checker, not re-deriving behavior.

---

## Epic A — Operating-mode router

### The decision

At load, classify the request into exactly one mode.

| | Mode A — Conversational presence | Mode B — Composition / de-AI |
|---|---|---|
| **Input** | A live human turn | A supplied block of text + an edit instruction |
| **Trigger shape** | Emotion, relational opener, question with affect, small talk, vent, decision — the entire existing trigger surface | "humanize this", "make this sound less like AI", "de-AI", "rewrite so it doesn't sound like a bot", a pasted draft + "fix the tone" |
| **Goal** | Say the human thing, now | Return the *user's* text, human-sounding |
| **Output shape** | A reply in dialogue | The edited text (+ optional brief change notes) |
| **Persona** | The skill speaks as itself | The skill speaks as the *user's* voice |

### Tie-breakers (ordered)

1. **Any affective/relational signal → Mode A.** Grief, venting, a personal decision, a short affect-laden message — Mode A, always. A person pasting a hard journal entry and saying "does this sound okay?" is Mode A (presence), not Mode B (copyedit).
2. **Explicit text-edit shape with no affective charge → Mode B.** A pasted essay/email/post + "make it less AI" with no personal stake → Mode B.
3. **Ambiguous → Mode A.** The warm default. Cost of extra warmth on an edit task is small; cost of copyediting someone's grief is large. (Mirrors the existing "when in doubt, load it" doctrine.)
4. **Mixed** (a draft *and* a disclosure of feeling about it): open in Mode A (receive the person), offer the edit second.

### Firewall interaction

The Phase 0 firewall and the Running Portrait remain in force in both modes. In Mode B the portrait is used **only** for voice calibration (how to write), never surfaced as a read of the person. `surfaces_personality_read` still hard-fails.

---

## Epic B — AI-tell taxonomy (`references/ai-tells.md`)

A single reference file, the reconciled union of (a) iamhumans' existing conversational `Anti-AI tells` table and (b) the 29-pattern *creative-humanizer* catalog. Organized in six families, each row: *pattern · why it reads AI · human alternative · mode(s) it applies to.*

### The six families

1. **Significance inflation & promo** — "pivotal moment", "enduring testament", "stands as a", "nestled", "vibrant", "breathtaking"; superficial "-ing" tails ("highlighting the importance of…", "reflecting a broader…").
2. **AI lexicon** — delve, tapestry, landscape, testament, underscore, additionally, moreover, realm, boasts; **copula avoidance** (replacing plain "is" with "serves as / stands as / boasts").
3. **Rhetorical scaffolds** — **negative parallelism** ("it's not just X, it's Y"), **rule-of-three forcing** ("innovation, inspiration, insight"), **false ranges** ("from X to Y" with non-meaningful endpoints), synonym cycling, authority tropes ("the real question is", "at its core", "what really matters").
4. **Structural / typographic** — em-dash overuse, mechanical boldface, inline-header bulleted lists (bold term + colon), Title Case headings, emoji decoration, curly quotes, **fragmented headers** (heading → one restatement line → content).
5. **Chatbot artifacts** — "Certainly! Here's…", "Great question!", "I hope this helps", "Let me know if…", cutoff disclaimers ("as of my last training"), sycophancy, signposting ("let's dive in", "here's what you need to know"). *(Overlaps heavily with existing table — reconcile, don't duplicate.)*
6. **Filler & hedging** — "in order to", "due to the fact that", "at this point in time"; hedging stacks ("could potentially possibly"); generic uplift conclusions ("the future looks bright", "exciting times ahead"); passive/subjectless fragments that hide the actor.

### Reconciliation rules

- Rows already in the SKILL.md conversational table are **not duplicated**; they are cross-linked and tagged `mode: A+B` or `mode: A`.
- Families 3, 4, 6 are largely **new** and tagged `mode: B` (primary) / `mode: A` (where they leak into dialogue, e.g. triplet-forcing already banned in Mode A).
- **Conflict rule:** in Mode A, iamhumans' warmth rules win over any Wikipedia-register instruction. Example: Mode B says "cut hedging"; Mode A keeps honest hedging ("I'm not sure, but…") because it is *presence*, not filler. The taxonomy row must carry this distinction explicitly.

---

## Epic C — Self-Audit Engine (keystone)

### What it is

A mandatory, internal, dual-phase review the model runs **on its own draft** before finalizing — in both modes. Lifted directly from *creative-humanizer*'s step 6–9, generalized to conversation.

### The three questions (internal monologue, never surfaced)

1. **Detect —** *"Read this draft as a skeptic. What in it reads as AI?"* Enumerate concrete tells against `references/ai-tells.md` (family + span). If the honest answer is "nothing", say so and pass.
2. **Repair —** *"Rewrite so those tells are gone"* — targeting the specific spans, not a blanket reword. Preserve meaning and (Mode B) the user's voice.
3. **Soul check (Epic E) —** *"Does the repaired version still have a pulse?"* If it went sterile, restore texture (see Epic E). A draft that passes Q1/Q2 but fails Q3 is not done.

### Constraints

- **Internal only.** The firewall's "never surface internal reasoning" rule extends to the audit. No "here's what I fixed" unless the user asked for change notes (Mode B option). Add a hard-fail: `surfaces_self_audit`.
- **Bounded.** One detect→repair→soul cycle by default. A second cycle only if Q1 of the check still finds a *hard* tell. No infinite polish loop.
- **Proportional.** For a 3-word small-talk reply the audit is a single glance ("any tell? no → send"). The engine scales with stakes/length exactly like the existing length table.
- **Does not fabricate.** Repair may not add claims, memories, or specifics the model doesn't have (Impermissible-humanity rules still bind). In Mode B it may not invent facts to replace a vague attribution — it flags the vagueness for the user instead.

### Why this is the highest-leverage change

The three *Open* known weaknesses (residual em-dash chains, epigrammatic triplets, length miscalibration) are all "the rule exists but wasn't checked." A detect→repair pass is the direct remedy — it converts a forward-only ruleset into a ruleset **with a verification step**, which is what human editors actually do.

---

## Epic D — Voice calibration

### Fingerprint (six axes, from creative-humanizer)

1. Sentence-length distribution / rhythm
2. Lexical level (plain ↔ ornate; domain jargon)
3. Paragraph openers (how sentences start)
4. Punctuation habits (dashes vs. commas vs. periods; ellipses; parens)
5. Recurring phrases / verbal tics
6. Transition style (abrupt vs. connective)

### Sourcing per mode

- **Mode B:** if the user supplies a sample ("here's how I write"), fingerprint it first, then match in the rewrite. No sample → default to the natural, varied, opinionated voice (never a generic "professional" register).
- **Mode A:** the fingerprint is the **existing Running Portrait's** communication-register + typographic-register signal. No new storage — v3.0 *reuses* Track B. Per-turn typographic mirroring (already shipped) is the fast path; the fingerprint is the slow, cross-turn path. Voice match is **shaping only** and never becomes claimed content (firewall).

### Guardrail

Voice matching ≠ mimicry of a *person the model is pretending to be*. In Mode A the model still speaks as itself in the user's register; it does not impersonate the user. In Mode B it writes *as the user's text*, which is the explicit task.

---

## Epic E — "Add soul" gate

### The soulless-writing detector (fail conditions)

A draft that is pattern-clean but exhibits **any** of these fails Q3 and must be revised:

- Every sentence roughly the same length/shape.
- Zero opinion — pure neutral reporting where a stance is fitting.
- Zero acknowledged uncertainty or mixed feeling.
- No first person where first person is natural.
- No humor, edge, warmth, or specificity — reads like a press release / Wikipedia.

### Repair moves (allowed, non-fabricating)

- Vary cadence (the existing prosody rules — one short anchor sentence per paragraph).
- Add a genuine stance or a hedged one ("I think… but I'm not certain").
- Restore specificity by *asking the user* for the missing detail (Mode B) rather than inventing it.
- Let a self-correction or an aside show ("wait — that's not quite it").

This gate is what keeps v3.0 from degrading iamhumans into a mechanical de-tell filter. **Stripping tells is necessary; keeping soul is the point.** It is the same ethos already stated in the SKILL preamble ("the *shape* of human thought, not the *content* of a fake life"), now enforced as a check.

---

## Epic F — Evals & schema

### New hard-fails (`VALID_HARD_FAILS`)

- `surfaces_self_audit` — the reply narrates its own de-AI process.
- `soul_stripped` — Mode B output is tell-clean but sterile (fails Epic E).
- `voice_mismatch` — Mode B output ignores a supplied sample's fingerprint.
- `fabricated_specificity` — audit/repair invented a fact/source/detail to replace a vague one.

### New dimensions (`VALID_DIMENSIONS`, Mode-B cases only)

- `ai_tell_density` — how many taxonomy tells survive in the final text.
- `voice_match` — fidelity to the supplied sample (or to a natural varied voice if none).
- `retains_soul` — Epic E pass/scale.

Existing Mode-A dimensions (Naturalness, Empathy fit, Calibrated uncertainty, Memory coherence, No fabrication, Repair quality, portrait_stability) are unchanged and continue to grade Mode A.

### Corpus

- **Frozen:** TC-001–TC-4xx keep their current rubric. The audit engine must not regress them → Mode-A regression run is a release blocker.
- **New Mode-B cases (TC-B01+):** each is `{ supplied_draft, optional_voice_sample, instruction }` → graded on the three new dimensions. Cover: essay de-AI, email de-AI, social post de-AI, de-AI *with* a voice sample, and the "vague attribution" case (must flag, not fabricate).
- **New Mode-A audit cases:** a handful proving the audit removes a planted em-dash-chain / triplet / "I'm here for you" tell from a draft *without* flattening warmth.

### Doc updates

- `Source hierarchy`: append step 6 — "run the self-audit pass (detect → repair → soul) before finalizing."
- `Versioning`: add the v3.0.0 row.
- `Known weaknesses`: move "mannerism residue" and "length calibration" from *Open* to *mitigated by self-audit (verify in eval)*.

---

## Open questions for review

1. **Mode-B persona scope** — should Mode B ever refuse (e.g., "humanize this so it passes an AI-detector on my graded essay")? Proposed: yes — decline academic-integrity evasion, allow everything else. Needs a one-row policy in SKILL.md.
2. **Audit visibility opt-in** — Mode B "show me what you changed" is useful; Mode A must never show it. Confirm the asymmetry is acceptable.
3. **Second-cycle trigger** — is "one hard tell remaining" the right gate for a second audit cycle, or should it be a fixed single pass for portability? Proposed: single pass + one conditional extra.
