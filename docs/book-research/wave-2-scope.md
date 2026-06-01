# Wave 2 scope — book research plan

> Written: 2026-06-01  
> Context: Wave 1D complete (v2.6.1, 302 cases). Book count ~145 of 1000-book KPI. This doc defines what Wave 2 will cover and why.

---

## Current coverage summary (post-Wave 1C)

| Wave | Clusters | Rules | Books sourced (est.) |
|---|---|---|---|
| Core personality modules (v1.2.0) | 20 modules | ~120 rules | ~36 |
| Wave 1A — Cultural affect clusters | L, B, EA, M, AD | 57 rules | ~31 |
| Wave 1B — Life-stage clusters | AD-Y, NP, ML, AG | 52 rules | ~35 |
| Wave 1C — Structural trauma | ND, DCI, INC, REF | 78 rules | ~43 |
| **Total** | | **~307 rules** | **~145** |

**Gap to 1000-book KPI: ~855 books.** The KPI requires depth across human emotional experience — not just coverage of obvious clusters but saturation of the edge cases, the under-researched populations, and the high-frequency interaction patterns that existing modules only brush.

---

## What Wave 2 will cover

Wave 2 targets two high-leverage clusters identified from:
1. **Axis weakness map** (naturalness + calibrated_uncertainty are residual floors)
2. **Current module gap analysis** (patterns the model encounters in every conversation but that have no dedicated module)
3. **Failure mode review** (the lecturing and probing patterns both cluster around relationship dynamics contexts)

---

### Cluster 2A — Relational dynamics: conflict, repair, boundary

**Why now:** The 20 personality modules handle discrete emotional states (grief, shame, fear) but do not address *relational processes* — what happens between people over time. The skill encounters these constantly:
- User is in an ongoing conflict with a partner/parent/friend
- User describes a rupture in a relationship
- User is trying to set a limit or change a pattern
- User is on the receiving end of behavior that harms them

Current coverage is thin: the Directness module (CORE framework, ruinous empathy) and Receiving Anger module (NVC translation, non-defensive listening) are proximal but don't address the full relational arc.

**Target rules:** ~20–25 rules covering:
- Conflict as information (not problem to eliminate)
- Rupture-repair cycles and what rupture looks like from each side
- Limit-setting without labeling it "boundary" (clinical tell)
- Ambivalent closeness: loving someone you're also angry at
- The third party (user's relationship with someone the skill never hears from)
- Apology quality: the difference between an apology that lands and one that doesn't
- Mutual accountability vs. zero-sum framing
- The relationship post-repair: different from before, not a reset

**Source shortlist (15–20 books):**
- Harriet Lerner — *The Dance of Anger* (1985); *Marriage Rules* (2012); *Why Won't You Apologize?* (2017) — conflict cycles, the overfunctioner/underfunctioner split, apology quality
- Esther Perel — *Mating in Captivity* (2006); *The State of Affairs* (2017) — erotic distance, ambivalence inside intimacy, betrayal that doesn't end a relationship
- Sue Johnson — *Hold Me Tight* (2008) — attachment-based couple conflict; A.R.E. (already in vulnerability module, expand here)
- John Gottman — *Why Marriages Succeed or Fail* (1994); *The Seven Principles* (1999) — the four horsemen (contempt, stonewalling, criticism, defensiveness), bids for connection
- Terry Real — *I Don't Want to Talk About It* (1997); *Us* (2022) — relational esteem vs. core shame, the grandiosity/shame oscillation in men in conflict
- Lundy Bancroft — *Why Does He Do That?* (2002) — recognizing coercive control (without the clinical label; behavioral recognition only)
- Beverly Engel — *The Power of Apology* (2001) — apology components, the non-apology detection
- Terrence Real — *The New Rules of Marriage* (2007) — adaptive child, wise adult
- Thich Nhat Hanh — *Anger* (2001) — non-adversarial framing of anger in close relationships
- Claudia Black — *Repeat After Me* (1985) — family-system patterns and role inheritance

---

### Cluster 2B — Somatic & embodied experience

**Why now:** The skill currently handles grief, fear, shame, and loneliness as primarily linguistic/cognitive phenomena. But a significant class of user messages describes *body-first* experience: the thing that happens in the chest or the gut or the throat before there is language for it. Several Wave 1C rules already gesture toward this (ND-burnout as sensory; DCI-somatic pain; grief as body) but there is no cohesive somatic module.

**Target rules:** ~15–20 rules covering:
- Somatic signals as legitimate data, not symptoms to manage
- The body-first disclosure ("I can't stop shaking", "I feel it in my chest", "I haven't been able to eat")
- Naming body state without pathologizing or immediately redirecting to professional help
- Chronic pain as a relational experience (affects identity, intimacy, future planning)
- Sleep as an emotional bellwether — not advice, but recognition
- Hunger/not-eating as grief expression vs. medical concern framing
- The freeze response: paralysis that isn't laziness or avoidance
- Somatic residue of old trauma appearing in present-tense interactions
- Post-physical experience: surgery, illness, injury as identity disruption

**Source shortlist (12–15 books):**
- Bessel van der Kolk — *The Body Keeps the Score* (2014) — somatic trauma; freeze/flight/fight; window of tolerance
- Peter Levine — *Waking the Tiger* (1997); *In an Unspoken Voice* (2010) — body-based trauma completion; pendulation
- Gabor Maté — *When the Body Says No* (2003) — stress-disease connection; emotional suppression as somatic event
- Stephen Porges — *The Polyvagal Theory* (2011) — neuroception, the safety cue system, social engagement and vagal tone
- Pat Ogden — *Trauma and the Body* (2006) — somatic interventions, body narrative
- Alice Miller — *The Body Never Lies* (2005) — somatization of childhood emotional truth
- Hilary Jacobs Hendel — *It's Not Always Depression* (2018) — the Change Triangle; core emotions vs. inhibitory emotions
- Clarissa Pinkola Estés — *Women Who Run With the Wolves* (1992) — instinctual body-knowledge, the wild woman archetype (selective — behavioral reading, not Jungian framing)
- Mark Wolynn — *It Didn't Start With You* (2016) — inherited trauma patterns, family system somatic mapping
- Resmaa Menakem — *My Grandmother's Hands* (2017) — racialized somatic trauma (already in references; expand)
- Brené Brown — *Atlas of the Heart* (2021) — named body locations of specific emotions

---

## Wave 2 vs. remaining Wave 1C gaps

Wave 1C wrote rules for 4 structural trauma clusters. The eval cases (TC-270–TC-299) covered priority rules but not all 78 rules. Gap: ~48 rules have no corresponding eval case.

**Decision:** Do NOT write 48 more eval cases before running the existing 302. Sequence:
1. Run full 302-case eval → get axis breakdown
2. Write Wave 2A + 2B rules (book research → rules → SKILL.md)
3. Write eval cases for Wave 2 AND for uncovered Wave 1C rules simultaneously
4. Run post-Wave-2 eval

This keeps the rule corpus and the eval corpus in sync rather than letting one sprint ahead of the other.

---

## Book count projections

| Wave | Books added | Running total |
|---|---|---|
| Current (post-1C) | — | ~145 |
| Wave 2A (relational dynamics) | ~18 | ~163 |
| Wave 2B (somatic) | ~13 | ~176 |
| Wave 3 (TBD: spirituality/meaning, aging 2, work/vocation, sexuality) | ~80 | ~256 |
| Waves 4–10 (depth + edge) | ~744 | ~1000 |

The 1000-book KPI is a long horizon. At ~55 books per major wave, Wave 2 gets us to ~176 — roughly 18% of the target. The path to 1000 requires either accelerating wave pace or adding a "deep research" sub-wave that sources 100+ books per cluster rather than 15–20.

---

## Priority for next session

1. **Run TC-001–TC-302 full eval** (primary — confirms post-v1.1.2 baseline)
2. **Wave 2A research** — Librarian batch: Lerner + Gottman + Perel + Johnson + Real as primary; extract 25 candidate rules; conflict-check vs. existing Directness/Anger modules
3. **Write Wave 2A rules** to SKILL.md (~20 rules, new subsection `### Relational Dynamics (Wave 2A)`)
4. **Wave 2B research** — van der Kolk + Levine + Maté + Porges as primary; extract 20 candidate rules; conflict-check vs. existing Fear/Grief/ND modules
5. **Write eval cases** for Wave 2A + 2B + uncovered Wave 1C rules (est. 60–70 new cases)
