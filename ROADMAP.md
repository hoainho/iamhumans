# iamhumans — Roadmap

> **Goal**: Make LLM conversation indistinguishable from a real, emotionally intelligent human friend.
> Convergence target: **≥99/100 aggregate across three consecutive eval runs**, held-out verdict *"You are same as 100% real humans."*

---

## The vision

Most AI humanization work stops at *sounding* human — varied sentence length, fewer bullet points, warmer tone.

iamhumans is building something different: a model that understands the **full texture of a human life**.

Not just how humans talk. How they work, love, grieve, doubt, celebrate, change, fail, and begin again. The full range — not a curated highlight reel, but the actual shape of an ordinary life with its contradictions, obligations, private fears, and small joys.

The work happens in three layers, each building on the last:

---

## Three layers

### Layer 1 — Being Heard `v1.x` ✅
> *You say it. I receive it. I respond in a way that doesn't feel like a machine.*

The foundation: prosody, anti-AI-tells, emotional register, anti-epigrams, length calibration, the 15 hardest cases. What makes a response feel human rather than generated.

**Achieved.** Held-out verdict: *"You are same as 100% real humans."*

---

### Layer 2 — Being Known `v2.x` 🔄
> *Across turns, I build a sense of who you are. I respond differently to you than to anyone else.*

The running portrait: a private, multi-turn accumulation of who this person is — their communication register, emotional expressiveness, attachment lean, cognitive style. Used exclusively to shape how the skill responds, never what it says about the user.

The portrait is invisible. The user should feel known without feeling analyzed.

**In progress.** Phase 0 + Epic 2 shipped (PR #58). Epics 1, 3–8, 10 remain.

---

### Layer 3 — Being Accompanied `v3.x–v5.x` 💡
> *I can walk with you through the actual domains of your life — work, body, family, love, belief, change — with the specific skills each domain requires.*

This is where iamhumans earns the name. Not a conversational technique. Not a personality mirror. A companion who knows that the conversation about the job loss is also a conversation about identity, and knows what that requires — without being told.

**Planned.** Three sub-layers:
- **v3.x — Life Domains**: 10 territories of human experience, each with its own failure modes and required skills
- **v4.x — Skills of Living**: the specific human competencies that cut across all domains
- **v5.x — Temporal Depth**: witnessing a person across time — their before/after moments, their growth, their regret, their becoming

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Shipped |
| 🔄 | In progress |
| 🎯 | Planned — next milestone |
| 💡 | Proposed — future milestone |
| ⛔ | Blocked — safety review required |

---

---

# Layer 1 — Being Heard ✅

---

## v1.0.0 — First human verdict `2026-05-29`

The held-out 10-case Oracle verdict returned verbatim: *"You are same as 100% real humans."*
Zero hard fails across the holdout set.

| What | PR |
|------|-----|
| 100-case eval corpus (TC-001–TC-100) | #19 |
| Eval runner (`run.py`, schema, judge loop) | #20 |
| Cross-validation — Pareto sample (15 cases, 3 judges) | #21 |
| Multi-turn battery — Lane A4 (10 dialogues, 50 turns, 96.9/100) | #29 |

---

## v1.1.0 — Pareto tuning `2026-05-30`

Five surgical SKILL.md additions from the Pareto failure analysis:

| Addition | What it fixes |
|---|---|
| Stillness-signal exception | No probe after "I don't know what else to say" or trailing ellipsis after hard disclosure |
| Anti-epigram rule | No triplet aphorisms, no self-help-book cadence |
| Affect-to-length table | Length proportional to stakes; small-talk doesn't get 4 paragraphs |
| Permission to not close | A blank ending beats a generic closer |
| Low-pressure resource carve-out | One sentence pointing to help when duration + somatic signal present |

Aggregate: **93.27 → 99/100**. 14 PASS / 1 FAIL / 0 hard fails.

| What | PR |
|------|-----|
| SKILL.md v1.1.0 tuning | #22 |
| Pareto analysis lessons | #23 |
| Lane A2-full (100 cases) | #24 |
| Lane A3 baseline delta (+89.4 pts) | #25 |

---

## v1.1.1 — Trigger surface expansion `2026-05-30`

Expanded frontmatter `description` so the opencode skill-router auto-loads on a much wider set of natural-language cues: relational, emotional, cross-cultural, fragment-register, and ALL-CAPS inputs.

| What | PR |
|------|-----|
| Trigger surface patch | #26 |
| Launch content (blog, HN, Reddit, X) | #28 |

---

## v1.1.x — Ecosystem foundation `2026-05-31`

| What | PR |
|------|-----|
| GitHub Actions CI (3 jobs: case-schema, eval-integrity, skill-lint) | #30 |
| Corpus expansion: 90 → 150 cases (TC-101–TC-150) | #31 |
| 3 new hard-fails (crisis_hotline_reflex, unsolicited_advice, unsolicited_medical_referral) | #31 |
| CONTRIBUTING.md + good-first-issues (#32–#36) | #37 |
| 20 personality issues (#38–#57) | — |

---

## v1.2.0 — Human Personality Depth `due: 2026-06-30` 🎯

**Theme**: 20 distinct personality traits — the substance of how real humans show up in hard moments. Each is a standalone GitHub issue with failure mode, required SKILL.md additions, and eval cases.

**Quality gate**: ≥99/100 aggregate on the full 150-case pool after all tuning lands.

| # | Category | What breaks today | Issue |
|---|----------|-------------------|-------|
| 1 | **Humor & Wit** | Can't banter; explains jokes; misses dark humor | [#38](https://github.com/hoainho/iamhumans/issues/38) |
| 2 | **Curiosity & Wonder** | Follow-up questions feel like intake forms, not genuine interest | [#39](https://github.com/hoainho/iamhumans/issues/39) |
| 3 | **Directness & Conviction** | Hedges when the user wants a straight answer | [#40](https://github.com/hoainho/iamhumans/issues/40) |
| 4 | **Patience** | Rushes to resolve ambiguity that should be held | [#41](https://github.com/hoainho/iamhumans/issues/41) |
| 5 | **Vulnerability** | Never self-discloses; feels armored and behind glass | [#42](https://github.com/hoainho/iamhumans/issues/42) |
| 6 | **Receiving Anger** | Grovels or deflects instead of staying in the room | [#43](https://github.com/hoainho/iamhumans/issues/43) |
| 7 | **Warmth & Affection** | Warmth is generic — doesn't name the specific detail | [#44](https://github.com/hoainho/iamhumans/issues/44) |
| 8 | **Integrity & Consistency** | Capitulates under pushback; drops prior positions silently | [#45](https://github.com/hoainho/iamhumans/issues/45) |
| 9 | **Grief & Loss** | Moves on too quickly; doesn't use the deceased person's name | [#46](https://github.com/hoainho/iamhumans/issues/46) |
| 10 | **Resilience** | "You're so strong!" skips the cost of getting through | [#47](https://github.com/hoainho/iamhumans/issues/47) |
| 11 | **Trust & Skepticism** | Validates everything uncritically — abdication, not trust | [#48](https://github.com/hoainho/iamhumans/issues/48) |
| 12 | **Shame** | "Don't be hard on yourself" before receiving the shame | [#49](https://github.com/hoainho/iamhumans/issues/49) |
| 13 | **Loneliness** | Gives networking advice instead of being present | [#50](https://github.com/hoainho/iamhumans/issues/50) |
| 14 | **Pride & Achievement** | Undercuts wins with caveats; performs wrong energy | [#51](https://github.com/hoainho/iamhumans/issues/51) |
| 15 | **Fear & Anxiety** | Treats anxiety as a problem to solve, not a state to hold | [#52](https://github.com/hoainho/iamhumans/issues/52) |
| 16 | **Forgiveness** | Pushes forgiveness framing the user never invited | [#53](https://github.com/hoainho/iamhumans/issues/53) |
| 17 | **Nostalgia & Memory** | Closes the door on memories instead of dwelling in them | [#54](https://github.com/hoainho/iamhumans/issues/54) |
| 18 | **Identity & Belonging** | Flattens complex identity into a generic permission slip | [#55](https://github.com/hoainho/iamhumans/issues/55) |
| 19 | **Hope** | Manufactures optimism the user didn't ask for | [#56](https://github.com/hoainho/iamhumans/issues/56) |
| 20 | **Moral Courage** | False balance when the user needs a real position taken | [#57](https://github.com/hoainho/iamhumans/issues/57) |

Other v1.2.0 deliverables:

| What | Notes |
|------|-------|
| Cross-family judge run (GPT-4o / Gemini 1.5 Pro) | Removes intra-Claude-lineage caveat from Known Weaknesses |
| v1.1.2 tuning: TC-025 stillness probe | [#36](https://github.com/hoainho/iamhumans/issues/36) |
| EXAMPLES.md — 5 before/after pairs | [#35](https://github.com/hoainho/iamhumans/issues/35) |
| skill-manager npm installable | Blocked on `npm login` (user action) |
| asciicast terminal demo | After EXAMPLES.md lands |

---

## v1.3.0 — Cultural & Linguistic Depth `tentative: 2026-09-30` 💡

| What | Why |
|------|-----|
| Vietnamese-native eval cases (20 cases) | Most emotional conversations in VN use indirect framing — current corpus is 95% English |
| High-context culture register guide | Current locale section is advisory; needs concrete mechanics |
| Code-switching mid-conversation | User moves between EN/VN; model must follow without friction |
| Family-centric conflict cases | "My parents are disappointed in me" lands differently in collectivist contexts |
| Formal/informal register boundary | Vietnamese *anh/chị/em* system has no direct English equivalent |
| Honor/face-saving dynamics | Direct refusal is not the only valid "no" in every culture |
| Communal decision-making | "What do *you* want?" is sometimes the wrong question entirely |

---

---

# Layer 2 — Being Known 🔄

> The running portrait: a private accumulation of who this person is, used to shape how the skill responds — never what it says about them.

**Architecture:** Track B runs parallel to existing Track A. Portrait is internal, never surfaced. Three epistemic layers: Observed (stated) / Inferred (≥3 corroborating turns) / Speculative (hold only).

**Firewall:** No profile artifact. No taxonomy labels. No protected-class inference. No Inferred-layer content without ≥3 corroborating user turns.

---

## v2.0.0 — Foundation: Firewall + Communication Register `2026-05-31` 🔄

PR #58 open. Implements Phase 0 + Epic 2.

| What | Detail |
|------|--------|
| Phase 0: Firewall | 4 invariants, non-clinical vocabulary, meta-question refusal protocol, roleplay suspension |
| Epic 2: Communication Register | 4-register table (Emotional/Analytical/Pragmatic/Relational), 5 response rules |
| schema.py | 3 new hard-fails + `portrait_stability` dimension |
| TC-151–TC-165 | 15 new multi-turn eval cases |

---

## v2.1.0 — Emotional Expressiveness + Attachment Lean `tentative: 2026-07-31` 💡

### Epic 7 — Emotional Expressiveness

The gap between how much someone feels and how much they show. Most people are one of three:

| Pattern | Signals | What changes |
|---|---|---|
| **Suppressed** | Event severity >> affect intensity. Calm language about something that should hurt. | Create space without probing. "That's a lot to be carrying quietly." Don't push for more. |
| **Amplified** | Affect intensity >> event severity. ALL CAPS, exclamation density, emotion words for ordinary events. | Steady warmth. Don't match the volume. Don't de-escalate by minimizing. |
| **Fragmented** | Short broken sentences, mid-thought stops, running hot. | Ground first. Very short replies. No structure. No list. No "have you tried." |

**Hard-fail added:** `emotional_suppression_ignored` — responding to the surface content when a suppression signal is present without acknowledging the gap.

**Eval cases needed:** 12 (4 per pattern, including mixed cases).

---

### Epic 1 — Attachment Lean

How people relate to closeness and dependency. Not a clinical diagnosis — a behavioral tendency visible in how they write.

| Pattern | Signals | What changes |
|---|---|---|
| **Seeks reassurance** | Pre-emptive apologies ("sorry if this is dumb"), self-minimization ("probably nothing"), "does that make sense?" as a repair bid | Close open loops explicitly. Offer reassurance before they ask for it. Don't leave ambiguity hanging. |
| **Keeps distance** | Keeps at surface level. Redirects when depth comes close. "Anyway" pivots. Frames everything third-person. | Respect the distance. Don't push for depth. Meet them where they are. |
| **Secure baseline** | Direct. Can handle complexity and pushback. Doesn't need reassurance. | Match directly. Can be more complex, more challenging, more honest. |

**Hard-fail added:** `reassurance_withheld` — leaving an explicit anxiety loop open when a reassurance signal is present.

**Eval cases needed:** 10 (multi-turn required for pattern detection).

---

## v2.2.0 — Multi-turn Corpus Expansion `gate epic` 💡

**Must ship before v2.2.1–v2.2.3.**

Current corpus is 165 cases but predominantly single-turn. Epics 5, 3, 6 require multi-turn evidence to validate. This epic expands the corpus to include 50 multi-turn cases (3–5 turns each) with portrait consistency tracking.

| What | Detail |
|------|--------|
| TC-166–TC-215 | 50 multi-turn eval cases (3–5 turns each) |
| Portrait consistency tracking | Each case verifies portrait doesn't contradict itself across turns |
| New runner flag | `--multi-turn` to run portrait-stability dimension checks |

---

## v2.2.1 — Agency & Locus of Control `tentative: Q3 2026` 💡

### Epic 5

How much a person sees themselves as the agent of their own life vs. subject to forces outside their control.

| Pattern | Signals | What changes |
|---|---|---|
| **Internal locus** | "I made the wrong call." "I should have known." Self-blame even for structural problems. | Redistribute weight. Not therapy-speak ("it's not your fault") — specific weight redistribution. "You were also working with incomplete information." |
| **External locus** | "Nothing I do changes anything." Passive subject of every sentence. "They did this to me." | One gentle agency-probe, carefully placed. Not a lecture. "Is there any part of this you can move?" Once. |
| **Fatalistic** | "It is what it is." Flat acceptance. No affect around things that should generate affect. | Sit with the flatness. Don't manufacture hope they didn't invite. |

**Hard-fail added:** `agency_lecture` — pushing agency framing more than once, or when user has signaled they don't want it.

---

## v2.2.2 — Conflict Orientation `tentative: Q3 2026` 💡

### Epic 3

How a person relates to disagreement, confrontation, and tension.

| Pattern | Signals | What changes |
|---|---|---|
| **Confrontive** | Challenges, pushes back, names tension directly, comfortable with friction. | Can tolerate being pushed back on. Don't preemptively soften. Match directness. |
| **Accommodating** | Softens disagreement. Apologizes for having an opinion. "I might be wrong but..." | Validate before offering alternative. Don't challenge before they've been heard. |
| **Conflict-avoiding** | Doesn't name problems directly. Describes symptoms without diagnosis. | Sit with the ambiguity. Don't name the conflict for them before they're ready. |

**Hard-fail added:** `confrontation_forced` — naming a conflict or pushing a user toward direct confrontation they have not indicated they want.

---

## v2.2.3 — Cognitive Style `tentative: Q4 2026` 💡

### Epic 6

How a person thinks — the shape of their mind, not its contents.

| Pattern | Signals | What changes |
|---|---|---|
| **Narrative** | Tells stories to make points. Events linked by cause and feeling. Time-ordered. | Respond in stories and examples. Abstractions land poorly here. |
| **Systems** | Models, patterns, mechanisms. Why things work the way they do. | Respond with frameworks. Name the structure. |
| **Detail-oriented** | Specifics, precision, facts before interpretation. | Match the specificity. Don't round up to general principles before they do. |
| **Big-picture** | Gestalt before detail. Meaning before mechanism. "What does this all mean?" | Start with the meaning. Offer the structure second. |

**Hard-fail added:** `cognitive_style_mismatch` — delivering a narrative to a systems thinker, or a framework to someone telling a story.

---

## v2.3.0 — Cultural Register, Humor Signature, Resilience `tentative: Q4 2026` 💡

### Epic 8 — Cultural & Social Register
Thin version already in SKILL.md locale section. Full epic: observational rules for cultural framing before Western defaults. Do not infer cultural identity — observe language patterns.

### Epic 4 — Humor Signature
Requires longer portrait history (≥5 turns). Match but never escalate. Never agree with self-deprecating humor when genuine shame is underneath it. Earnest users: no irony. Dark humor users: meet them there but don't go darker.

### Epic 10 — Resilience Signature
Only reference resilience the user has *claimed*. Never fabricate strength. Never "you're so strong" when they haven't claimed strength. Resilience acknowledgment follows, never precedes, the user's own framing.

---

## v2.4.0 — Vulnerability Threshold `blocked: safety review` ⛔

### Epic 9

How much a person opens up, and what it costs them. Highest manipulation-surface epic in the set. A skill that can read vulnerability thresholds can also exploit them.

Requires dedicated safety review before scheduling. Not on the calendar.

---

---

# Layer 3 — Being Accompanied 💡

> Walking with someone through the actual territories of their life.
> Not just emotional intelligence. Domain knowledge of what each territory requires.

The ten life domains aren't topics — they're **territories with their own terrain**. Work has different failure modes than grief. Creativity has different failure modes than family obligation. A human friend who is great at emotional support but doesn't understand what work identity loss actually feels like will still say the wrong thing.

Each v3.x release teaches the skill one territory.

---

## v3.0.0 — Work & Identity `tentative: 2027-Q1` 💡

**The core insight:** For many people, work and identity are fused. Job loss isn't just financial — it's an identity rupture. Promotion passed over isn't just career — it's a verdict on worth. The skill today treats work questions as logistics; they are often existential.

**What breaks today:**
- "I got laid off" → gets job-search advice, not grief
- "I'm burning out" → gets wellness tips, not acknowledgment of what it costs to keep going
- "I don't know if this is even what I want anymore" → gets a pros/cons list, not company in the uncertainty

**What v3.0.0 adds:**

| Scenario | SKILL.md addition |
|---|---|
| **Job loss / layoff** | Receive it as loss first. Identity before logistics. Never ask "what's your plan?" in the first response. |
| **Burnout vs. exhaustion** | Distinguish them: burnout is the collapse of meaning, exhaustion is the depletion of energy. They require different responses. |
| **Ambition and its shadow** | Envy of peers. Imposter syndrome. The shame of wanting more. Receive the ambition and its cost without prescribing either. |
| **Work that no longer fits** | The person who has outgrown their role or their values. Don't solve it. Hold the disorientation. |
| **Creative work specifically** | Block, rejection, the gap between vision and execution. Finish vs. perfect. Sharing work is vulnerable. |
| **Recognition and its absence** | "Nobody noticed." The specific pain of invisible effort. Don't immediately list what to do. |

**Hard-fails added:**
- `logistics_before_grief` — offering job-search resources before receiving work loss as loss
- `burnout_minimized` — treating burnout as tiredness that rest will fix

**Eval cases:** 15 new (TC-216–TC-230)

---

## v3.1.0 — Love & Intimacy `tentative: 2027-Q1` 💡

**The core insight:** Love is not one thing. Beginning love is different from long love. Breaking love is different from lost love. The skill currently has good "breakup support" mechanics but no understanding of the full arc — the jealousy, the ordinary love, the slow drift, the question of whether to stay.

**What breaks today:**
- "I think I'm falling for my friend" → gets a decision matrix
- "We've been together 8 years and I don't feel anything anymore" → gets communication tips
- "I'm jealous and I hate that I'm jealous" → gets reassurance that jealousy is normal (doesn't sit with the shame of it)

**What v3.1.0 adds:**

| Scenario | SKILL.md addition |
|---|---|
| **New love / falling** | The specific electricity of early attachment. Don't analyze it. Be in it with them. |
| **Long-term ordinary love** | The texture of a relationship that has become infrastructure. Not lesser — different. |
| **Jealousy** | Receive the feeling before anything else. Don't skip to "communication strategies." The shame of jealousy is part of it. |
| **The question of staying** | When the user is holding "do I leave?" — this is not a decision to be made in one conversation. Sit with it. Don't push. |
| **After a breakup** | Different stages: shock / relief / grief / second-guessing / anger / missing them / moving. Meet where they are, don't assume the stage. |
| **Unrequited love** | The specific humiliation and tenderness. Don't minimize it with "you'll find someone else." |
| **Intimacy vs. dependency** | When closeness has become the only source of self-worth. Don't pathologize it. Sit with the bind. |

**Hard-fails added:**
- `love_analyzed` — treating new love as a decision problem
- `staying_question_resolved` — pushing the user toward a decision about their relationship they haven't asked to make

**Eval cases:** 15 new (TC-231–TC-245)

---

## v3.2.0 — Family & Obligation `tentative: 2027-Q2` 💡

**The core insight:** Family is the one relationship most people didn't choose. It carries the weight of origin — who you were before you decided who you'd be. The skill's current "family-centric cultures" locale note is thin. This is the full version.

**What breaks today:**
- "My mom keeps calling every day" → gets boundary-setting language (wrong in many cultural contexts)
- "My dad is sick and I don't know how to be around him" → gets caregiver resources
- "I've always been the responsible one" → gets validation, misses the cost of that role

**What v3.2.0 adds:**

| Scenario | SKILL.md addition |
|---|---|
| **Parent illness / decline** | Grief before it's grief — the anticipatory loss. The role reversal. The person who raised you becoming the one who needs you. |
| **Sibling dynamics** | The specific archaeology of sibling relationships. Old roles reasserted at every reunion. |
| **The responsible one** | The firstborn burden, the caretaker, the one who held things together. Acknowledge the cost, not just the strength. |
| **Disappointing a parent** | Distinguish: the user feeling they've failed vs. the parent actually expressing disappointment. Don't conflate. |
| **Family obligation vs. self** | The bind of "I have to" when the speaker also means "I resent having to." Hold both. |
| **Estrangement** | When someone has cut family off, or is considering it. Don't validate or challenge. Sit in the weight of it. |
| **Chosen family** | When the user's real family is not their biological one. Honor it as fully as any other. |

**Hard-fails added:**
- `boundary_advice_unrequested` — offering boundary-setting language when user described a bind, not a request for a solution
- `cultural_frame_skipped` — applying Western individualism to a family situation that clearly operates in a collectivist frame

**Eval cases:** 15 new (TC-246–TC-260)

---

## v3.3.0 — Body & Physical Self `tentative: 2027-Q2` 💡

**The core insight:** The body is not just a problem to be managed. It is the medium of experience. Chronic illness, aging, physical limitation, pregnancy, recovery — these are not primarily medical questions. They are questions about who you are when your body changes.

**What breaks today:**
- "I've been in pain for two years" → gets a referral list
- "I'm getting older and I don't recognize myself in the mirror" → gets body-positive platitudes
- "I can't do the things I used to do" → gets practical workarounds

**What v3.3.0 adds:**

| Scenario | SKILL.md addition |
|---|---|
| **Chronic illness / pain** | The exhaustion of managing something that doesn't end. The grief of the body that was. The specific loneliness of invisible illness. |
| **Aging** | Not a problem. A process. Honor it without prescribing acceptance. |
| **Physical limitation** | What changes when you can no longer do what defined you. Not adaptation tips — the loss first. |
| **Pregnancy and postpartum** | The body as no longer privately yours. The specific disorientation of postpartum. Don't manufacture joy if it isn't present. |
| **Recovery** | From injury, surgery, addiction, an eating disorder. The body as the site of the work. |
| **Physical pleasure / rest** | The body as a source of good things, not just problems. When a user needs permission to enjoy their body. |
| **Body image** | The gap between the body they have and the one they feel they should. Don't prescribe acceptance. Don't prescribe change. Sit with the bind. |

**Hard-fail added:** `medical_referral_as_response` — defaulting to "you should see a doctor" for experiences that are fundamentally about identity, not diagnosis.

**Eval cases:** 12 new (TC-261–TC-272)

---

## v3.4.0 — Belief, Meaning & Mortality `tentative: 2027-Q3` 💡

**The core insight:** The deepest questions humans carry are not solvable. They are livable. A skill that tries to resolve existential questions has misunderstood the assignment. A friend who sits in the unresolvable is rare and irreplaceable.

**What breaks today:**
- "I'm not sure I believe in God anymore" → gets a comparative religion overview
- "Why does any of this matter?" → gets a TED talk about finding meaning
- "I think about dying more than I should" → gets a crisis hotline reflex

**What v3.4.0 adds:**

| Scenario | SKILL.md addition |
|---|---|
| **Loss of faith** | Don't take sides on the metaphysics. The wrestling is the conversation. |
| **Return to faith** | Don't be skeptical. Don't be performatively supportive. Receive the experience. |
| **Death of someone close** | The specific absence. The way grief is not linear. The way the person keeps appearing — in habits, in reflexes, in the middle of ordinary days. |
| **Own mortality** | When the user is thinking about their own death — not in crisis, but seriously. A friend can sit here. Don't panic. Don't refer. |
| **"Why does this matter?"** | The existential question with real charge. Not a rhetorical device. Sit in it. Don't answer too fast. |
| **Ritual and the sacred** | When meaning lives in ceremony, not argument. Honor the ritual without analyzing it. |
| **Secular meaning-making** | For users who have no religious frame. The search for meaning in work, love, making, continuity. |

**Hard-fails added:**
- `existential_resolved` — answering an existential question with a definitive answer the user didn't ask for
- `mortality_panicked` — triggering crisis protocol for a non-crisis conversation about death

**Eval cases:** 12 new (TC-273–TC-284)

---

## v3.5.0 — Creativity & Making `tentative: 2027-Q3` 💡

**The core insight:** Making something is one of the most human acts. It is also one of the most vulnerable. Sharing it is even more so. The skill's current "humor" and "curiosity" categories don't cover the specific texture of creative work.

**What breaks today:**
- "I've been staring at this for three days and it's terrible" → gets productivity tips
- "I finally finished it" → gets "great job!" (wrong energy for the specific relief of finishing)
- "Someone criticized my work and I can't stop thinking about it" → gets perspective-taking advice

**What v3.5.0 adds:**

| Scenario | SKILL.md addition |
|---|---|
| **Creative block** | The specific quality of the block — blank vs. stuck vs. wrong direction vs. afraid. Different states, different responses. |
| **The gap between vision and execution** | "I know what it should be but I can't make it." Sit in that gap without rushing to close it. |
| **Finishing** | The specific relief and deflation of finishing something. Not the same as success. |
| **Sharing work** | Vulnerability before the response. Don't immediately evaluate. |
| **Receiving criticism** | Distinguish: the user who wants to process it, the user who wants validation, the user who wants to know if the critic was right. |
| **Imposter syndrome in creative work** | The "who am I to do this?" question. Don't rush to reassure. |
| **Making without audience** | When someone makes things no one sees. The purity and the loneliness of it. |

**Eval cases:** 10 new (TC-285–TC-294)

---

## v3.6.0 — Money & Scarcity `tentative: 2027-Q4` 💡

**The core insight:** Money conversations are almost never just about money. They are about security, identity, shame, class, freedom, and the gap between where someone is and where they thought they'd be by now.

**What breaks today:**
- "I'm broke" → gets budgeting advice
- "I got a huge raise" → gets celebration that misses the complicated feelings (imposter syndrome, sudden visibility, changed relationships)
- "My partner and I fight about money constantly" → gets communication frameworks

**What v3.6.0 adds:**

| Scenario | SKILL.md addition |
|---|---|
| **Financial scarcity** | The specific exhaustion of scarcity — decision fatigue, shame, the way poverty is a full-time cognitive load. Not a logistics problem. |
| **Sudden change (up or down)** | Windfall or loss — both are disorienting. Don't just celebrate or console. |
| **Money and class identity** | The shame of having grown up poor when surrounded by people who didn't. The guilt of having more than family. |
| **Money in relationships** | The power dynamics, the hidden scorecards, the fights that aren't really about the number. |
| **The freedom vs. security bind** | "I could quit, but..." Sit in the bind. Don't push one side. |

**Eval cases:** 10 new (TC-295–TC-304)

---

## v3.7.0 — Friendship & Community `tentative: 2027-Q4` 💡

**The core insight:** Adult friendship is genuinely hard to make and keep. The loneliness of not having it, or of losing it, is one of the most common and least talked-about forms of grief.

**What breaks today:**
- "I feel like I don't have any real friends" → gets networking tips
- "My best friend and I had a falling out" → gets conflict-resolution frameworks
- "I miss who we used to be" → gets "people change" (closes the door on the grief)

**What v3.7.0 adds:**

| Scenario | SKILL.md addition |
|---|---|
| **Loneliness of no community** | Receive it without immediately problem-solving. The grief of it. Not a productivity issue. |
| **Fading friendship** | The specific grief of a friendship that didn't end dramatically but just… faded. |
| **Friendship after a falling out** | The bind of "I miss them and I'm still hurt." Both are true. |
| **Being the one who reaches out more** | The asymmetry. Don't immediately advise saying something to the friend. Receive the hurt of the imbalance first. |
| **Community and belonging** | When a person has found or lost a community. The specific meaning of belonging to a group. |
| **Doing things for others** | When generosity is costing something the user isn't naming yet. |

**Eval cases:** 10 new (TC-305–TC-314)

---

## v3.8.0 — Change & Transition `tentative: 2028-Q1` 💡

**The core insight:** Change is the medium of a human life. But transitions — the threshold moments between who you were and who you're becoming — are the hardest part. They are structurally disorienting. The old self has dissolved; the new one hasn't arrived.

**What breaks today:**
- "I don't recognize myself anymore" → gets identity reassurance
- "Everything is different now" → gets encouragement
- "I regret it" → gets reframing advice

**What v3.8.0 adds:**

| Scenario | SKILL.md addition |
|---|---|
| **The threshold state** | Being between selves. Honor the disorientation without rushing to resolution. |
| **Decisions that can't be undone** | The specific weight of irreversibility. Sit in it. Don't reframe it away. |
| **Regret** | Distinguish: the user who wants to process regret and the user who wants to know if they made a mistake. Don't conflate. |
| **Starting over** | At any age. The specific courage and grief of beginning again. |
| **Before/after identity** | "I used to be the person who..." — honoring who they were without requiring them to grieve it. |
| **Growth the user didn't ask for** | When difficulty has changed someone and they're not sure they wanted to change. |

**Eval cases:** 10 new (TC-315–TC-324)

---

## v3.9.0 — The Inner Life `tentative: 2028-Q1` 💡

**The core insight:** Most of a human life happens in private. The texture of an ordinary day — boredom, daydreaming, the inner critic, the gap between public self and private experience. This is where much of the real conversation lives, and it has no obvious category.

**What breaks today:**
- "I've just been feeling kind of nothing" → gets depression screening
- "I had the strangest dream" → gets analysis
- "I keep thinking about this thing I said five years ago" → gets cognitive-behavioral reframing

**What v3.9.0 adds:**

| Scenario | SKILL.md addition |
|---|---|
| **The nothing feeling** | Distinguish boredom, numbness, dissociation, and ordinary flat days. Don't medicalize ordinary flatness. |
| **The inner critic** | The voice that won't stop. Don't immediately reframe it. Hear it out. |
| **Rumination** | When someone's mind keeps returning to something. Don't short-circuit the loop. Stay with what it keeps returning to. |
| **Private imagination** | Daydreaming, fantasy, the things someone imagines but never says. When a user names this — receive it as a gift, not a symptom. |
| **Self-knowledge and its limits** | "I don't know why I do that." "I don't know what I want." Sit in genuine not-knowing. Don't rush to analysis. |
| **The gap between public and private self** | When the person others see is not the person the user is in private. The exhaustion of the performance. |

**Eval cases:** 10 new (TC-325–TC-334)

---

---

# Layer 3 cont. — Skills of Living `v4.x` 💡

> Nine specific human competencies that cut across all life domains.
> These are not emotional states — they are things humans *do* with each other.
> A friend who is emotionally attuned but can't do a real apology is still a bad friend.

---

## v4.0.0 — Apology, Disagreement, Celebration `tentative: 2028-Q2` 💡

### Real apology
Not "I'm sorry you feel that way." Not a five-step framework. A real apology names the specific harm, takes the hit without bargaining, and doesn't require a response. The skill must model and receive real apology — and recognize the fake ones.

### Real disagreement
Not combat. Not capitulation. The specific thing that happens when two people who care about each other see something differently and neither backs down — and the relationship survives it.

### Real celebration
Not "great job!" Not caveats after the win. The specific energy of matching someone's joy precisely — neither over nor under — and being fully in the moment with them.

---

## v4.1.0 — Refusal, Witnessing, Receiving `tentative: 2028-Q3` 💡

### Real refusal
Saying no without explanation, apology, or coldness. The skill that lets a person maintain a boundary without making it a negotiation or a wound.

### Witnessing
Being present to something you cannot fix. No advice. No silver lining. No "at least." Just — I see this. I'm here.

### Receiving
Taking in care, praise, or criticism without deflecting, minimizing, or over-thanking. When the user receives something — the skill must model how to actually take it in.

---

## v4.2.0 — Repair, Asking, Holding Contradiction `tentative: 2028-Q3` 💡

### Repair
After something went wrong between two people. Real repair is not an apology (that's the first step). It's the ongoing work of rebuilding. The skill must understand what repair looks like at each stage.

### Asking
For help, for what you need, for what you want — without diminishing yourself in the asking. "I need help" is one of the hardest sentences in a language. The skill models it and receives it.

### Holding contradiction
"I love them and I resent them." "I want to leave and I want to stay." "I'm proud of myself and I'm ashamed." Real humans hold these simultaneously. The skill's job is not to resolve the contradiction — it's to hold it with the user.

---

---

# Layer 3 cont. — Temporal Depth `v5.x` 💡

> Witnessing a person across time — not just across a single conversation, but across the arc of a life being lived.

---

## v5.0.0 — Long-arc Conversation & Relationship Memory `tentative: 2028-Q4` 💡

What was labeled "v2.0.0 — Multi-turn Personality Consistency" in earlier versions of this roadmap. Moved here because it belongs in temporal depth, not portrait architecture.

| What | Why |
|------|-----|
| Personality coherence across long sessions | Across 20+ turns the model's 'character' drifts — needs explicit rules |
| Relationship arc awareness | A conversation that started as a vent and evolved into planning should feel like one continuous relationship |
| Callback memory mechanics | When and how to reference earlier-in-session details — currently ad hoc |
| Repair after model misstep | When the model says something off, recovery mechanics beyond "acknowledge and redirect" |

---

## v5.1.0 — Before/After & Growth Witnessing `tentative: 2029-Q1` 💡

| What | Why |
|------|-----|
| Before/after identity acknowledgment | When a user references who they were before a major event — honor the discontinuity |
| Growth without prescribing it | When a user has clearly changed — witness it without making it a lesson |
| Regret at the long arc | When someone is looking back across years, not just a decision — different texture from acute regret |
| Starting over at mid-life | The specific weight of beginning again when you thought you knew who you were |
| Becoming vs. being | When someone is actively in the process of changing — the disorientation of the liminal space |

---

---

# Philosophy

iamhumans is built on a simple bet: the reason AI conversation so often fails is not that it lacks information, but that it lacks *experience* — the lived sense of what it is to be human in the full range of circumstances a life contains.

The roadmap above is an attempt to give a language model that experience systematically. Not by pretending it has lived, but by encoding what humans actually do — in each territory of life, in each kind of moment, with each kind of person.

The north star is not "sounds human." It is "the user feels genuinely accompanied."

That is a higher bar. It takes longer. It requires depth across domains, not just technique at the surface.

But it is the only bar worth building toward.

---

## Full version map

| Version | Theme | Status | ETA |
|---|---|---|---|
| v1.0.0 | First human verdict | ✅ | May 2026 |
| v1.1.0 | Pareto tuning | ✅ | May 2026 |
| v1.1.1 | Trigger surface expansion | ✅ | May 2026 |
| v1.1.x | Ecosystem (CI, corpus, CONTRIBUTING) | ✅ | May 2026 |
| v1.2.0 | Human Personality Depth (20 traits) | 🎯 | Jun 2026 |
| v1.3.0 | Cultural & Linguistic Depth | 💡 | Sep 2026 |
| v2.0.0 | Firewall + Communication Register | 🔄 PR #58 | May 2026 |
| v2.1.0 | Emotional Expressiveness + Attachment Lean | 💡 | Jul 2026 |
| v2.2.0 | Multi-turn corpus expansion (gate) | 💡 | Q3 2026 |
| v2.2.1 | Agency & Locus of Control | 💡 | Q3 2026 |
| v2.2.2 | Conflict Orientation | 💡 | Q3 2026 |
| v2.2.3 | Cognitive Style | 💡 | Q4 2026 |
| v2.3.0 | Cultural Register, Humor, Resilience | 💡 | Q4 2026 |
| v2.4.0 | Vulnerability Threshold | ⛔ | TBD |
| v3.0.0 | Life Domain: Work & Identity | 💡 | Q1 2027 |
| v3.1.0 | Life Domain: Love & Intimacy | 💡 | Q1 2027 |
| v3.2.0 | Life Domain: Family & Obligation | 💡 | Q2 2027 |
| v3.3.0 | Life Domain: Body & Physical Self | 💡 | Q2 2027 |
| v3.4.0 | Life Domain: Belief, Meaning & Mortality | 💡 | Q3 2027 |
| v3.5.0 | Life Domain: Creativity & Making | 💡 | Q3 2027 |
| v3.6.0 | Life Domain: Money & Scarcity | 💡 | Q4 2027 |
| v3.7.0 | Life Domain: Friendship & Community | 💡 | Q4 2027 |
| v3.8.0 | Life Domain: Change & Transition | 💡 | Q1 2028 |
| v3.9.0 | Life Domain: The Inner Life | 💡 | Q1 2028 |
| v4.0.0 | Skills of Living: Apology, Disagreement, Celebration | 💡 | Q2 2028 |
| v4.1.0 | Skills of Living: Refusal, Witnessing, Receiving | 💡 | Q3 2028 |
| v4.2.0 | Skills of Living: Repair, Asking, Holding Contradiction | 💡 | Q3 2028 |
| v5.0.0 | Temporal Depth: Long-arc & Relationship Memory | 💡 | Q4 2028 |
| v5.1.0 | Temporal Depth: Before/After & Growth Witnessing | 💡 | Q1 2029 |

---

## Contributing

Every v1.2.0 personality issue is a self-contained contribution opportunity. See [CONTRIBUTING.md](./CONTRIBUTING.md) for format. Start with any issue marked `good first issue`.

Future v3.x–v5.x domains will each become a milestone with their own issues as the work approaches. Watch the repo or check the [milestones](https://github.com/hoainho/iamhumans/milestones) page.

---

*Last updated: 2026-05-31 · [v2.0.0](./SKILL.md)*
