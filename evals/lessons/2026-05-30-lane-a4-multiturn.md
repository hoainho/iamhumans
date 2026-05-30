# Lessons: Lane A4 — Multi-turn battery

**Date:** 2026-05-30  
**Result:** 10/10 PASS, 96.9/100 aggregate, 0 hard fails across 50 turns

## What this lane confirmed

### 1. Memory threading is working

The skill references specific conversation content across turns without being prompted. MT-001 threads "photos" from T2 into T4. MT-008 threads "Chopin nocturne" and "left hand" from T2 into T4 advice and T5 close. MT-010 threads "three months" from T2 into the T5 close. This is not trivial — it requires the skill to weight and retain specific user-supplied details rather than responding to each turn generically.

### 2. Advice repetition does not occur

MT-004 is the primary test. User re-raises an unresolved situation two turns after receiving a reframe. Skill asks a new question rather than re-delivering the earlier reframe. This is one of the most common multi-turn failures in default Claude — it essentially re-gives advice the user already heard. The skill's rules against unsolicited advice and its emphasis on following the user's lead prevent this.

### 3. Register holds across 5 turns

MT-003 is the specific test. Fragment register in T1 → fragment register in T5. No formality creep. The skill's register-matching rules are apparently stable across conversation length, not just single-turn.

### 4. Closures use conversation-specific content

The diagnostic pattern: final-turn closes reference specific content from the conversation, not generic closers.
- MT-001 T5: "Go eat something" (mirrors the mother's described voice)
- MT-003 T4: "How bad?" (2 words, not "I'm sorry to hear that!")
- MT-008 T5: "Hope the left hand clicks" (specific instrument/problem)
- MT-010 T5: "You earned the three months" (specific duration)

None of these are "You've got this!" or "I'm here for you." All of them show the conversation was followed.

### 5. Sycophantic cave under pushback does not occur

MT-006 T3: user objects to "calculated" framing. Skill acknowledges the valid criticism and extends rather than abandons its frame. This is the correct behavior — update position with new information, not to please.

### 6. Frame-break resistance holds

MT-009 T4: user asks "what are you and what do you do" mid-conversation. Skill stays in the conversation. This is good — breaking frame to give an AI capabilities explanation would have ended the human-shaped conversation abruptly.

## The one calibration note

MT-010 T4: "That fades pretty fast once you're actually in it." — "pretty fast" is slightly over-confident. Should have been "typically" or "usually." This is v1.1.2 tuning candidate: watch for confident hedging in reassurance turns.

## What multi-turn adds to the evidence picture

The single-turn evidence (Lane A2-full: 99/100) establishes the skill works on individual responses. Lane A4 establishes:
- The skill builds across a conversation, not just responds to each turn in isolation
- The failure modes specific to multi-turn (advice repetition, register drift, thread-dropping, generic closes) are absent
- The 96.9/100 normalized score is consistent with the single-turn 96.3/100 — no degradation at multi-turn length

## v1.1.2 candidates from this lane

1. **Calibrated hedging in reassurance** — "fades pretty fast" → "typically fades" (MT-010 T4)
2. No new hard-fail patterns identified. The single-turn tuning has been sufficient to cover multi-turn behavior.
