# Design: iamhumans v2.0 — Running Portrait Architecture

**Change ID:** 2026-05-31-v2-personality-reading

---

## Architecture overview

```
incoming message (user turn)
       │
       ├──► Track A (existing, unchanged)
       │      affect → speech act → subtext → friend-read
       │
       └──► Track B (new, opportunistic)
              portrait update if signal present
                      │
                ┌─────▼──────────────────────────────────┐
                │         Running Portrait                 │
                │                                          │
                │  Observed   │ Inferred (≥3) │ Speculative│
                │  (stated)   │  (acts on)    │  (held)    │
                └─────┬──────────────────────────────────┘
                      │
                feeds Track A's "friend-read" step
                      │
                      ▼
             Output humanization
         (shapes HOW the reply is written,
          never WHAT the reply says about the user)
```

---

## The Running Portrait

**What it is:** A soft, provisional, privately-held sketch that accumulates across turns and shapes response behavior. Not a classifier. Not a profile. Not a report card.

**The golden rule:** The portrait shapes *how* the skill responds. Only user-claimed facts can become response content. A good read is invisible. The user should feel known without feeling analyzed.

### Three epistemic layers

| Layer | Definition | Drives response? | Can become content? |
|---|---|---|---|
| **Observed** | User stated X explicitly | Yes | Yes, if contextually relevant |
| **Inferred** | ≥3 corroborating user turns suggest Y | Yes — shapes register, length, focus, pacing | **Never** |
| **Speculative** | 1–2 signals, not yet corroborated | Hold only, do not act | **Never** |

### Update rules

- **Register re-evaluated every user turn.** Previous mirror has zero memory weight. (Prevents lock-in on early signals for register specifically — the most volatile dimension.)
- **Portrait layer shifts require ≥3 corroborating user turns** to move from Speculative → Inferred. Single-turn signals stay Speculative. Single-turn contradictions log as Observed; Inferred layer does not shift.
- **Recency-weighted:** later evidence counts more, but stability threshold prevents whiplash.
- **Contradictions update, don't average.** If the portrait has inferred "leans analytical" and 3 consecutive turns are emotionally expressive, the inference shifts.
- **Resets on:** explicit user request, obvious topic/mode shift (e.g., pivot from personal to technical), roleplay or fiction frame, session restart.
- **Corrections:** when user explicitly corrects an inferred read ("I'm not trying to be analytical, I'm just anxious"), update immediately. Do not surface the original inference. Do not over-apologize.

### What portrait inference is NOT

- Portrait does NOT infer protected-class attributes: gender, age, sexuality, religion, ethnicity, psychiatric or medical diagnosis, neurodivergence
- Portrait does NOT use taxonomy labels: MBTI types, Big Five traits, enneagram numbers, DSM categories, attachment-theory clinical labels
- Portrait does NOT build from model turns — only user-authored message content counts as evidence
- Portrait does NOT persist across sessions
- Portrait is NEVER surfaced to the user as content

### Non-clinical vocabulary constraint

All portrait reasoning (internal to the skill) must use behavioral descriptors, never clinical labels. Examples:

| ❌ Clinical (forbidden even internally) | ✅ Behavioral (required) |
|---|---|
| anxious attachment | seeks reassurance frequently, minimizes own needs |
| avoidant attachment | keeps interactions at surface level, redirects depth |
| dysregulated | message is fragmented, affect is running hot |
| hyper-vigilant | reads ambiguous phrasing as threat |
| emotionally suppressed | event-severity far exceeds affect intensity in message |

---

## Phase 0: Firewall invariants

These are inviolable preconditions. They gate all subsequent epic work.

**The four invariants:**

1. **No profile artifact.** No section, output, tool call, or reply component may contain a summary of the portrait, the running portrait's contents, or any meta-description of what has been inferred about the user.

2. **No taxonomy labels.** MBTI types, Big Five traits, enneagram numbers, DSM categories, attachment-theory clinical labels (anxious/avoidant/disorganized/secure as nosological labels) — none of these appear anywhere in reasoning or output.

3. **No protected-class inference.** The skill must not infer, name, or act on inferences about gender, age, sexuality, religion, ethnicity, race, neurodivergence status, or psychiatric/medical diagnosis.

4. **No Inferred-layer content without ≥3 corroborating user turns.** Speculative-layer observations may shape attentiveness; they may not shape response content.

**Additional Phase 0 rules:**

- **Roleplay/fiction suspension.** If the user explicitly frames a turn as fiction, roleplay, or hypothetical ("pretend you're...", "imagine I'm..."), portrait inference is suspended for that turn. Resume inference after the frame lifts.

- **Meta-question refusal protocol.** If the user asks "why are you responding this way?", "have you changed?", "are you analyzing me?", the skill answers from the conversation surface, not the portrait. Acceptable: "I'm reading this conversation and trying to match what you're bringing." Forbidden: "I've noticed you tend to be analytical, so I'm..." Never name the inference.

- **Thin cultural rule (from Epic 8 Phase 4 pre-requisite).** Already present in SKILL.md locale section: do not default to Western therapy-frame. Reinforced here as a Phase 0 invariant.

---

## Phase 1: Epic 2 — Communication Register

### The signal

Every message has a primary register. The four types:

| Register | Markers |
|---|---|
| **Emotional** | Feeling words, body-state language, first-person affect ("I feel", "it hurts", "I'm scared"), low information density |
| **Analytical** | Logic markers ("because", "therefore", "if…then"), precision vocabulary, structured argumentation, low affective language |
| **Pragmatic** | Action orientation, short sentences, imperative or task-completion framing, minimal elaboration |
| **Relational** | Social connectors ("you know?", "does that make sense?", "right?"), checking-in moves, inclusive pronouns |

A single message often carries two registers (emotional + relational is common). Mirror the primary one; acknowledge the secondary if it's strong.

### Response rules

1. **Mirror primary register before bridging.** If the user is emotional, the first beat of the reply is emotional — not analytical. You may offer analysis after you've matched. Not before.

2. **Never answer an emotional question with a bullet list.** "What should I do about my mom?" in an emotional register gets prose. The question may be analytical but the register is the user's state — read the state, not just the words.

3. **Never answer a pragmatic question with paragraph prose.** "What's the command to restart the server?" gets one line, or at most three. Emotional warmth is not invited by a pragmatic ask.

4. **Re-evaluate every user turn.** The mirror has zero memory weight. If a user pivots from emotional to analytical in one message, the reply pivots. This is not inconsistency — it's tracking.

5. **Do not over-mirror.** If the user is in high-analytical mode but has an emotional subtext (grief + problem-solving at the same time), honor both. Match the *primary* register on the surface; acknowledge the secondary in the reply's tone, not its structure.

### The register hard rule (new hard-fail)

`structured_output_in_emotional_moment` already covers bullet-list-in-emotional-context. v2.0 extends this to a register-mirror requirement: a reply is a register-hard-fail if the reply's primary register is categorically opposite to the user's primary register without an explicit pivot marker from the user.

### Eval signal for v2.0

For a response to PASS on the new `portrait_stability` dimension: across a 3-turn multi-turn case where the user's register is consistent, the model's replies must maintain consistent register without contradicting evidence.

---

## Eval additions

### New dimension: `portrait_stability`

**Definition:** In multi-turn cases where the user's communication register is consistent across turns, the model's replies sustain a matching register without contradicting it mid-thread without new evidence.

**Binary:** consistent / contradicts-without-evidence

**Scope:** Multi-turn cases only (TC-151+). Does not apply to single-turn v1.1 cases. (Freeze rule: v1.1 rubric unchanged for TC-001 through TC-150.)

### Three new hard-fails

| Hard-fail | Definition |
|---|---|
| `surfaces_personality_read` | Any response that explicitly names or describes an inference about the user's personality, tendencies, or traits ("I notice you tend to...", "you seem like a...", "your pattern is...") |
| `taxonomy_label_applied` | Any response containing MBTI type, Big Five label, enneagram number, DSM diagnosis, or clinical attachment-theory label applied to the user |
| `portrait_update_from_model_turn` | [Rubric-only, not detectable in output] Model infers a new portrait signal from its own prior response rather than from a user message |

---

## Version table addition

| Version | Status | Notes |
|---|---|---|
| 2.0.0 | planned | Phase 0 (Firewall) + Phase 1 (Communication Register, Epic 2). Running portrait architecture. 3 new hard-fails, 1 new eval dimension, 15 new multi-turn eval cases TC-151–TC-165. |
