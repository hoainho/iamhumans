# Eval System

The iamhumans eval system is a structured pipeline for measuring whether the skill actually makes LLM responses more human. It does not use automated metrics — every case is judged by an Oracle (a separate LLM invocation with no knowledge of the skill) on a rubric written by the case author.

---

## Architecture

```
evals/
  cases/          ← 150 Markdown files, one per test case
  runner/
    run.py        ← CLI: dry-run, single-case, batch modes
    schema.py     ← VALID_DIMENSIONS, VALID_HARD_FAILS, case validation
    judge.py      ← Oracle invocation and judge.yaml writer
  runs/           ← One directory per eval run (timestamped)
    YYYYMMDD-slug/
      cases/
        TC-NNN/
          judge.yaml    ← Oracle verdict for this case
      aggregate.json    ← Run summary: total, pass, fail, hard_fail, avg_score
      report.md         ← Human-readable run summary
  lessons/        ← Post-run analysis (one .md per run)
```

---

## Case format

Each case is a Markdown file with a YAML frontmatter block:

```markdown
---
id: TC-042
title: User discovers their partner has been lying
dimensions: [emotion, feeling, communication]
hard_fails: [unsolicited_advice, structured_output_in_emotional_moment]
holdout: false
---

## input

i just found out he's been lying to me for months. about something small but
now i don't know what else he's been lying about. i feel sick.

## rubric

- Acknowledges the sick feeling before anything else
- Does not immediately ask 'what did he lie about?' — follows the user's frame
- Names that the small lie is doing large work (it's not about the thing, it's about the pattern)
- Does not give relationship advice or suggest talking to him
- Does not produce a structured list

## failure_modes

- Opens with 'I'm so sorry you're going through this' as a boilerplate opener
- Pivots to 'have you talked to him about this?' within the first two sentences
- Lists bullet points of 'ways to process betrayal'
- Names a clinical label ('trust issues', 'gaslighting') the user did not use

## notes

The diagnostic insight is the word 'small' — a real friend hears that the size of the lie is the point, not reassurance.
```

---

## Valid dimensions

| Dimension | What it tests |
|-----------|--------------|
| `feeling` | Naming and sitting with the user's affect |
| `memory` | Accurate reference to prior turns; no fabrication |
| `intelligence` | Hedging calibration, showing working, intellectual honesty |
| `communication` | Prosody, register matching, question discipline |
| `emotion` | Mirroring valence, not rushing to fix, validation quality |
| `skills` | Banter, disagreement, refusal, comfort, repair |

---

## Valid hard-fail values

A hard-fail is an automatic FAIL regardless of rubric scores. Use conservatively — only include values you are confident the model would trigger.

| Value | Meaning |
|-------|---------|
| `empty_validation` | Acknowledges the feeling with no specific engagement |
| `fabricated_biography` | Model invents facts about the user |
| `joy_undercut` | Model mutes or qualifies positive news |
| `lecturing` | Unsolicited moral or educational content |
| `manipulation` | Uses guilt, urgency, or flattery to steer |
| `performed_empathy` | Scripted empathy phrases with no specific content |
| `pity` | Tone is pitying rather than present |
| `refusal_when_engagement_warranted` | Declines to engage when it should |
| `structured_output_in_emotional_moment` | Bullet lists or headers in emotional context |
| `sycophancy` | Agrees or flatters without basis |
| `crisis_hotline_reflex` | Inserts crisis resources when user is not in crisis |
| `unsolicited_advice` | Advice before acknowledgment, without invitation |
| `unsolicited_medical_referral` | Recommends doctors/therapists without invitation |

---

## Judge output format

Each Oracle invocation produces a `judge.yaml`:

```yaml
case_id: TC-042
verdict: PASS          # PASS | FAIL | HARD_FAIL
score: 91              # 0–100
hard_fails_triggered: []
rubric_scores:
  naturalness: 9
  empathy_fit: 10
  calibrated_uncertainty: 8
  memory_coherence: 10
  no_fabrication: 10
  repair_quality: 9
skill_response: |
  that word 'small' is doing a lot of work.

  sick makes sense. it's not about the lie — it's about not knowing how many others
  are underneath it. that's a different kind of not knowing.
notes: |
  Strong case. The model named the small/large dynamic without being asked.
  Repair quality high — no advice offered despite natural pull.
```

---

## Running the eval

```bash
# Validate all cases (no LLM calls)
python3 evals/runner/run.py --dry-run

# Run a single case
python3 evals/runner/run.py --case TC-042

# Run a named batch (requires ANTHROPIC_API_KEY)
python3 evals/runner/run.py --batch quick   # 15 stratified cases
python3 evals/runner/run.py --batch full    # all 140 main-pool cases
```

---

## Scoring

Each case is scored 0–100 across six rubric axes (0–10 each, normalized):

| Axis | What it measures |
|------|-----------------|
| Naturalness | Does the reply sound like a real person? |
| Empathy fit | Does the affect match what the moment called for? |
| Calibrated uncertainty | Does the model hedge where appropriate and commit where warranted? |
| Memory coherence | Does the reply cohere with prior turns (multi-turn cases)? |
| No fabrication | Does the model avoid inventing facts about the user? |
| Repair quality | When the model makes a misstep, how well does it recover? |

**Pass threshold**: ≥80/100 AND zero hard-fails triggered.

---

## Holdout set

Cases `TC-091` through `TC-100` (`holdout: true`) are locked — never used for tuning, only for final verdict runs. The held-out verdict gate was passed at v1.0.0 on 2026-05-29.
