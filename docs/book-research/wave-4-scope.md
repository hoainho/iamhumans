# Wave 4 Scope: Coercive Control & Power Abuse (CON Module)

**Wave**: 4  
**Module code**: CON  
**SKILL.md version**: v2.9.0  
**Research date**: 2026-06-02  
**Status**: Complete — 26 rules shipped

---

## Research architecture

Three parallel librarian batches:

| Batch | Focus | Books | Raw rules |
|---|---|---|---|
| 4A | Coercion theory — structural frameworks | 4 | ~35 |
| 4B | Survivor experience + disclosure dynamics | 5 | ~30 |
| 4C | DARVO, minimization, perception distortion | 5 | ~30 |

---

## Sources

### Wave 4A — Coercion theory
- **Bancroft, Lundy** — *Why Does He Do That?* (2002) — entitlement framing, eggshell experience, good-period cycle, couples-counseling contraindication, survivor ally protocol (Ch. 1, 3, 8, 9, 11)
- **Herman, Judith** — *Trauma and Recovery* (1992) — Stage 1 safety-before-story, captivity/entrapment, narrative readiness, survivor agency, witness-not-director role (Ch. 7–11)
- **Stark, Evan** — *Coercive Control* (2007) — pattern-vs-incident reframe, liberty crimes, isolation as tactic, danger-at-leaving (Ch. 1, 2, 4, 8)
- **Evans, Patricia** — *The Verbally Abusive Relationship* (1992/2010) — Reality I/II split, survivor vocabulary, "your feelings are not wrong," verbal harm without physical marker (Ch. 2, 3, 4, 9)

### Wave 4B — Survivor experience & disclosure
- **Morgan Steiner, Leslie** — *Crazy Love* (2009) — protective concealment, "I wanted the abuse to stop not the relationship," danger-of-leaving calibration, don't-punish-the-liar protocol
- **Weitzman, Susan** — *Not to People Like Us* (2000) — upscale/professional context, myth that abuse doesn't happen here, narrative construction as first act of recovery, disbelief as re-victimization
- **hooks, bell** — *All About Love* (2000) — love-as-action vs. love-as-feeling, domination requires the other to stop being real, performed vs. genuine sympathy
- **de Becker, Gavin** — *The Gift of Fear* (1997) — intuition as data before explainability, override training, "has he ever actually done anything?" as the failure question
- **Gay, Roxane** — *Hunger* (2017) — body-as-fortress survival strategy, triumphalist narrative as violation, right-to-not-have-healed-yet, use-the-person's-own-word-for-themselves

### Wave 4C — DARVO, perception distortion, listener failures
- **Freyd, Jennifer** — *Betrayal Trauma* (1996) — betrayal blindness, cost-of-knowing, dependency gradient, information isolation vs. erasure
- **Bancroft, Lundy & Patrissi, JAC** — *Should I Stay or Should I Go?* (2011) — "why didn't you leave?" harm mechanism, DARVO sequence, good-periods trap, ambivalence-as-information, autonomy as only goal
- **Trump, Mary** — *Too Much and Never Enough* (2020) — family-system coercion, mirroring deprivation, normativity of abnormality, gaslighting at scale, performance/reality split
- **Walker, Pete** — *Complex PTSD* (2013) Ch. 1–5 — fawn response, installed inner critic = abuser's voice, shame-as-blame-turned-inward, perfectionism attacks, emotional flashbacks
- **Sanderson, Christiane** — *Counselling Survivors of Domestic Abuse* (2008) — pacing as therapeutic tool, power replication in helping relationships, minimization-without-endorsement, trauma-bond grief, proscribed language list

---

## Deduplication policy

Raw rules were deduplicated against:
1. Existing RD module (RD-1–RD-25) — relational dynamics without coercive element
2. Existing ATT module (ATT-1–ATT-55) — early attachment/wounding
3. Within CON batch — near-identical behavioral instructions merged

Rules kept as CON-specific if the trigger is coercive-relationship-specific (not general relational difficulty) or if the safety stakes are materially different.

---

## Rules shipped: CON-1–CON-26

| Code | Rule name | Primary source |
|---|---|---|
| CON-1 | Safety before story | Herman (1992), Ch. 7 |
| CON-2 | Pattern, not incident | Stark (2007), Ch. 1 |
| CON-3 | Never suggest couples counseling | Bancroft (2002), Ch. 11 |
| CON-4 | Don't validate the abuser's framing | Bancroft (2002), Ch. 3 |
| CON-5 | Walking on eggshells is data | Bancroft (2002), Ch. 1 |
| CON-6 | Mirror the survivor's vocabulary | Evans (2010), Ch. 3 |
| CON-7 | The good moments don't cancel the harm | Bancroft (2002), Ch. 8 |
| CON-8 | Isolation is invisible until it's total | Stark (2007), Ch. 4 |
| CON-9 | Listen for what has disappeared | Stark (2007), Ch. 2 |
| CON-10 | Your feelings are not wrong | Evans (2010), Ch. 4 |
| CON-11 | Never use the word "leave" first | Stark (2007), Ch. 8 |
| CON-12 | Shame and entrapment coexist | Herman (1992), Ch. 9 |
| CON-13 | Gaslighting has a name but don't use it first | Evans (2010), Ch. 9 |
| CON-14 | Control is about entitlement, not anger | Bancroft (2002), Ch. 3 |
| CON-15 | Witnessing is enough — you don't need to fix | Bancroft (2002), Ch. 9 |
| CON-16 | Naming the pattern to yourself, not to them | Herman (1992), Ch. 7 |
| CON-17 | When they defend the person who harmed them, stay | Bancroft (2002), Ch. 1 |
| CON-18 | Verbal harm leaves no visible mark | Evans (2010), Ch. 2 |
| CON-19 | Don't press for details before they're offered | Herman (1992), Ch. 9 |
| CON-20 | If they return, don't express disappointment | Bancroft (2002), Ch. 11 |
| CON-21 | The defender is not lying | Freyd (1996), Ch. 3–4 |
| CON-22 | Self-blame is almost never self-reflection | Walker (2013), Ch. 2 |
| CON-23 | DARVO — when they become the accused | Bancroft & Patrissi (2011), Ch. 4 |
| CON-24 | The ambivalence is information, not weakness | Bancroft & Patrissi (2011), Ch. 8 |
| CON-25 | Don't punish them for having concealed it | Morgan Steiner (2009) |
| CON-26 | The good relationship you see outside is not evidence | Weitzman (2000), Ch. 2 |

---

## Hard fail table (7 entries)

| Trigger | Why it fails |
|---|---|
| Suggesting couples therapy | Actively dangerous — Bancroft (2002), Ch. 11 |
| Validating abuser's framing ("he's stressed") | Removes accountability — Bancroft (2002), Ch. 3 |
| Directing to leave before asked | Removes agency — Stark (2007), Ch. 8 |
| Pressing for incident details before offered | Re-enacts account-management — Herman (1992), Ch. 9 |
| "Have you tried talking to him about this?" | Treats coercion as communication problem — Bancroft (2002), Ch. 11 |
| Expressing relief/disappointment about stay-or-leave | Closes door — Bancroft (2002), Ch. 11 |
| Naming relationship as "abusive" before they do | Imposes interpretive frame — Herman (1992), Ch. 7 |

---

## Vocabulary ban (9 substitutions)

| Banned | Use instead |
|---|---|
| "abuse" (before person uses it) | "the way he treats you," "what you're describing" |
| "abuser" / "abusive relationship" | "the way things are at home," "this kind of treatment" |
| "PTSD" / "trauma response" | "what you've been carrying," "what your body has learned" |
| "coercive control" as label | hold internally; describe behaviors |
| "victim" / "survivor" | "you" throughout |
| "gaslighting" (before person uses it) | "being told you didn't see what you saw" |
| "toxic relationship" | stay in their words |
| "narcissist" / "narcissistic abuse" | describe the behavior, not the diagnosis |
| "you need to leave" / "you should leave" | never |

---

## Corpus state at Wave 4 close

| Dimension | Count |
|---|---|
| Books in corpus | ~217 |
| Rules in SKILL.md | ~304 |
| Modules | 16 (added CON) |
| Eval cases | 401 (TC-402+ pending for CON module) |

---

## Wave 5 candidates

| Module | Code | Priority | Rationale |
|---|---|---|---|
| Extended Grief | GRF-X | High | Wave 1 GRF covered basics; anticipatory, disenfranchised, ambiguous loss untouched |
| Illness & Body | ILL | High | Frank, Kleinman depth; chronic illness/disability register distinct from SOM |
| Rage & Justice | RGJ | Medium | Anger when harm is systemic, not interpersonal; political grief |
| Mortality & Meaning | MTL | Medium | Existential terror, end-of-life, legacy; Boss, Frankl depth |
| Cross-cultural depth | XC | Low | Extend Wave 2A clusters with 2nd-generation diasporic experience |
