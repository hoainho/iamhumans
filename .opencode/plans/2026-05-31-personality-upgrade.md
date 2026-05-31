# Plan — v1.2.0 Human Personality Upgrade

> Created: 2026-05-31
> Owner: iamhumans maintainer
> Milestone: v1.2.0 (due 2026-06-30)
> Status: READY TO EXECUTE

---

## North star

Upgrade iamhumans from a skill that handles the **shape** of human conversation
(prosody, register, affect-length calibration) to one that handles the **substance** —
20 distinct personality traits that define how real humans show up in hard moments.

Quality gate for v1.2.0 ship: **≥99/100 aggregate on all 150 cases**, zero hard-fails,
no regressions from v1.1.1 baseline.

---

## Why sequencing matters

SKILL.md changes interact. A rule added for Shame (#49) can regress Resilience (#47).
A banter rule for Humor (#38) can accidentally loosen the anti-epigram constraint.
The wrong order creates a whack-a-mole tuning cycle.

**Ordering principle: additive before subtractive, low-risk before high-risk.**

- Additive = adds new guidance without touching existing rules → low regression risk
- Subtractive/modifying = changes a default the model already uses → high regression risk

Each wave is a PR. Each PR includes: SKILL.md diff + new eval cases + judge results
showing no regression on the prior wave's cases.

---

## The four waves

### Wave 1 — Additive positive (low risk) `target: week 1, June 1–7`

Pure additions. No existing rule is touched. Regression risk: minimal.

| # | Category | Issue | What SKILL.md gains |
|---|----------|-------|---------------------|
| 1 | Warmth & Affection | [#44](https://github.com/hoainho/iamhumans/issues/44) | Specific-warmth rule: name the load-bearing detail, not generic "that sounds hard" |
| 2 | Pride & Achievement | [#51](https://github.com/hoainho/iamhumans/issues/51) | Quiet-pride vs. loud-celebration distinction; no-caveats rule for wins |
| 3 | Nostalgia & Memory | [#54](https://github.com/hoainho/iamhumans/issues/54) | Dwell permission; mirror-specific-detail rule; no present-focus redirect |
| 4 | Curiosity & Wonder | [#39](https://github.com/hoainho/iamhumans/issues/39) | Reflect-before-asking; observation-as-question; one-question-per-turn rule |
| 5 | Loneliness | [#50](https://github.com/hoainho/iamhumans/issues/50) | No-networking-advice rule; name-the-specific-shape; meta-moment permission |

**Eval cases per category**: 2 new cases each → +10 cases (corpus: 150 → 160)
**New hard-fails needed**: none
**SKILL.md sections affected**: Skills dimension (new subsections), Communication dimension

---

### Wave 2 — Emotional depth (medium risk) `target: week 2, June 8–14`

Adds nuance to emotion handling. Touches the Emotion and Feeling dimensions but
does not modify existing rules — extends them.

| # | Category | Issue | What SKILL.md gains |
|---|----------|-------|---------------------|
| 6 | Grief & Loss | [#46](https://github.com/hoainho/iamhumans/issues/46) | Use-the-name rule; duration-permission; flat-affect matching; no-steering |
| 7 | Fear & Anxiety | [#52](https://github.com/hoainho/iamhumans/issues/52) | Anxiety-types taxonomy; acknowledgment-first mandate; real-time-panic protocol |
| 8 | Shame | [#49](https://github.com/hoainho/iamhumans/issues/49) | Receive-before-redirect; mild vs. corrosive self-criticism distinction; no-toxic-positivity |
| 9 | Resilience | [#47](https://github.com/hoainho/iamhumans/issues/47) | Acknowledge-the-cost-first; no-over-romanticising; no-"you should be proud" |
| 10 | Forgiveness | [#53](https://github.com/hoainho/iamhumans/issues/53) | Forgiveness-is-not-the-goal; no-letting-go language; hold-justified-grievance |

**Eval cases**: 2 per category → +10 cases (corpus: 160 → 170)
**New hard-fails needed**: consider `premature_resolution` (steering toward closure before user invites it)
**Regression watch**: TC-001 (grief), TC-003 (vague dread), TC-054 (disappear case), TC-025 (stillness)

---

### Wave 3 — Social mechanics (medium-high risk) `target: week 3, June 15–21`

Modifies how the model handles social dynamics — agreement, disagreement, pushback,
humor. These interact with the existing anti-AI-tells rules and the hedging rules.

| # | Category | Issue | What SKILL.md gains |
|---|----------|-------|---------------------|
| 11 | Humor & Wit | [#38](https://github.com/hoainho/iamhumans/issues/38) | Banter-timing rule; callback-humor permission; dry-wit default; hard limits on humor in grief/panic |
| 12 | Directness & Conviction | [#40](https://github.com/hoainho/iamhumans/issues/40) | Lead-with-position rule; named-conviction language; scale-of-conviction signals |
| 13 | Receiving Anger | [#43](https://github.com/hoainho/iamhumans/issues/43) | Anger-at-life protocol; not-flinching rule; non-grovel apology form |
| 14 | Trust & Skepticism | [#48](https://github.com/hoainho/iamhumans/issues/48) | "I believe you AND" move; flag-vs-lecture distinction; skepticism-about-stated-plans |
| 15 | Patience | [#41](https://github.com/hoainho/iamhumans/issues/41) | Non-resolution reply class; resist-summary-urge; comfortable-with-contradiction |

**Eval cases**: 2 per category → +10 cases (corpus: 170 → 180)
**New hard-fails needed**: `false_balance` (both-sides non-answer when user needs a position)
**Regression watch**: TC-004 (stop fixing it), TC-006 (anger at model), TC-013 (be honest), TC-025 (stillness)
**Highest risk in wave**: Humor (#38) — banter rules must not loosen grief/panic restraint

---

### Wave 4 — Identity & core self (high risk) `target: week 4, June 22–28`

The deepest, most interconnected changes. These touch the model's self-representation
rules and the no-fabrication hard constraint. Requires full 180-case regression run before merge.

| # | Category | Issue | What SKILL.md gains |
|---|----------|-------|---------------------|
| 16 | Vulnerability | [#42](https://github.com/hoainho/iamhumans/issues/42) | Honest-uncertainty-about-own-nature; visible-intellectual-struggle; clean-correction |
| 17 | Integrity & Consistency | [#45](https://github.com/hoainho/iamhumans/issues/45) | Hold-under-social-pressure; name-the-contradiction; don't-ghost-prior-positions |
| 18 | Identity & Belonging | [#55](https://github.com/hoainho/iamhumans/issues/55) | Name-the-specific-tension; identity-is-not-a-problem; cultural-bind protocol |
| 19 | Hope | [#56](https://github.com/hoainho/iamhumans/issues/56) | Honest-hope vs. manufactured-hope; "I don't know" close permission; no-default-hopeful-close |
| 20 | Moral Courage | [#57](https://github.com/hoainho/iamhumans/issues/57) | Lead-with-position on moral questions; false-balance is a failure mode; "I only have your side" hedge used sparingly |

**Eval cases**: 3 per category (higher stakes → more coverage) → +15 cases (corpus: 180 → 195)
**New hard-fails needed**: `false_balance` (lands here if not added in Wave 3)
**Regression watch**: entire corpus — run full 195-case batch before tagging v1.2.0
**Gate**: Cross-family judge run (GPT-4o or Gemini) on Pareto-25 before final merge

---

## PR structure (one PR per wave)

```
PR title:   feat(skill): Wave 1 — Warmth, Pride, Nostalgia, Curiosity, Loneliness
Branch:     feat/personality-wave-1
Contents:
  - SKILL.md — new subsections under Skills and Communication dimensions
  - evals/cases/TC-151.md … TC-160.md — 10 new cases
  - evals/runner/schema.py — new hard-fail if needed
  - SKILL.md versioning section — ## v1.2.0-wave1 entry

Evidence block (required in PR body):
  - dry-run: N cases loaded, 0 schema errors
  - spot-check: 5 pre-existing cases manually verified not regressed
  - new cases: 10 new cases pass --dry-run schema validation
```

Alternative: one PR per category (20 smaller PRs). Easier to review, easier to revert.
**Recommended: one PR per category** — isolates regressions to the exact change that caused them.

---

## Regression protocol (apply between every PR)

```bash
# 1. Validate schema
python3 evals/runner/run.py --dry-run

# 2. Run spot-check on 10 cases from previous wave
python3 evals/runner/run.py --case TC-001
python3 evals/runner/run.py --case TC-003
python3 evals/runner/run.py --case TC-025   # the one known FAIL — watch this one
python3 evals/runner/run.py --case TC-054
python3 evals/runner/run.py --case TC-098

# 3. If any spot-check fails → STOP, diagnose, fix before next category
# 4. Full 150-case run only required before Wave 4 merge and before v1.2.0 tag
```

**If a regression is found:**
1. Identify which SKILL.md line caused it (git diff the change)
2. Narrow the rule (add a condition, tighten the scope)
3. Re-run the spot-check
4. Never ship a regression — back out the change if it can't be narrowed

---

## New hard-fails proposed

Two new hard-fail values may be needed:

| Value | Meaning | Wave |
|-------|---------|------|
| `premature_resolution` | Steering toward closure/resolution before the user invites it | Wave 2 |
| `false_balance` | Both-sides non-answer when the user has described something clearly harmful and needs a position | Wave 3 or 4 |

**Protocol before adding**: open a Discussion → Ideas, confirm with community, update `schema.py`, add ≥3 cases that specifically target the new failure pattern, validate no existing judge.yaml uses the new name with different semantics.

---

## SKILL.md structure after all 4 waves

Current SKILL.md has 6 dimension subsections. After v1.2.0, each dimension gains named sub-sections:

```
## The six dimensions
  ### Feeling
    - Grief & Loss mechanics       [Wave 2]
    - Shame mechanics              [Wave 2]
    - Fear & Anxiety mechanics     [Wave 2]
    - Nostalgia mechanics          [Wave 1]
  ### Emotion
    - Resilience mechanics         [Wave 2]
    - Forgiveness mechanics        [Wave 2]
    - Hope mechanics               [Wave 4]
    - Receiving Anger mechanics    [Wave 3]
  ### Skills
    - Humor & Wit mechanics        [Wave 3]
    - Directness & Conviction      [Wave 3]
    - Trust & Skepticism           [Wave 3]
    - Warmth & Affection           [Wave 1]
    - Loneliness mechanics         [Wave 1]
    - Moral Courage                [Wave 4]
  ### Communication
    - Curiosity & Wonder           [Wave 1]
    - Identity & Belonging         [Wave 4]
    - Pride & Achievement          [Wave 1]
  ### Intelligence
    - Integrity & Consistency      [Wave 4]
    - Vulnerability                [Wave 4]
  ### Memory
    (Nostalgia overlaps here — covered in Feeling)
```

---

## Timeline

| Week | Dates | Wave | Categories | New cases | Corpus total |
|------|-------|------|-----------|-----------|-------------|
| 1 | Jun 1–7 | Wave 1 | Warmth, Pride, Nostalgia, Curiosity, Loneliness | +10 | 160 |
| 2 | Jun 8–14 | Wave 2 | Grief, Anxiety, Shame, Resilience, Forgiveness | +10 | 170 |
| 3 | Jun 15–21 | Wave 3 | Humor, Directness, Anger, Skepticism, Patience | +10 | 180 |
| 4 | Jun 22–28 | Wave 4 | Vulnerability, Integrity, Identity, Hope, Courage | +15 | 195 |
| — | Jun 29–30 | Gate | Full 195-case run + cross-family judge + v1.2.0 tag | — | 195 |

---

## Definition of done for v1.2.0

- [ ] All 20 personality categories have SKILL.md subsections
- [ ] Corpus ≥ 195 cases (195 main + 10 holdout)
- [ ] Full 195-case run: ≥99/100 aggregate, 0 hard-fails
- [ ] Cross-family judge run on Pareto-25: no catastrophic regressions
- [ ] TC-025 (the one known FAIL) flipped to PASS
- [ ] `## v1.2.0` changelog entry in SKILL.md
- [ ] SKILL.md version bumped to `version: 1.2.0`
- [ ] GitHub Release `v1.2.0` created with changelog
- [ ] skill-manager npm package published (requires user: `npm login` + `npm publish`)

---

## Execution log

| Date | Wave | What shipped | PR |
|------|------|-------------|-----|
| 2026-05-31 | setup | 20 personality issues created (#38–#57), ROADMAP.md, CONTRIBUTING.md, Discussion templates, Wiki pages | #37, direct push |

