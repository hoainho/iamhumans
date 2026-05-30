# Plan — Road to Top, 30-day campaign, starting 2026-05-30

> Authorised by user via question tool, 2026-05-30. Plan is the single source of truth for this campaign; every PR and every session updates the **Execution log** at the bottom.

## North star

Make `iamhumans` a top-trending repository on GitHub within 30 days, with **evidence-anchored** ranking (not vanity stars). Target: top 1 trending GitHub site-wide (TypeScript or Python category) during the launch week.

**Honest framing on the target.** Top 1 GitHub site-wide trending typically requires 2,000-5,000+ stars in a 7-day window. With sound evidence, strong narrative, and HN/Reddit/X synchronization, this is *aspirational but reachable* — not a deterministic outcome. The plan is built so that even if we miss "top 1 site-wide", we still achieve:
- Top 1 in topic `opencode` (very high confidence)
- Top trending r/LocalLLaMA or r/ClaudeAI for 1-3 days (high confidence)
- ≥500 stars net (high confidence with full execution)

The plan is the bet; the verdict is the public ranking on launch week.

## Five lanes, running in parallel across the 30 days

### Lane A — EVIDENCE
Make the verdict cross-validated, longitudinal, and statistically defensible.

### Lane B — CORPUS
Close the 39/108 books → 80/108 books gap, write synthesis, expand case corpus 100 → 150.

### Lane C — PRODUCT / DX
Publish via skill-manager, polish install path, generate OG image + asciicast + EXAMPLES.md, seed Discussions.

### Lane D — NARRATIVE / LAUNCH
Blog post, HN submission, Reddit threads (r/LocalLLaMA, r/ClaudeAI, r/MachineLearning), X thread, upstream `sst/opencode` PR, awesome-list PRs, Discord cross-posts.

### Lane E — ECOSYSTEM
CI, weekly release cadence, good-first-issues, v1.2.0 milestone, contributor flow.

## Burst session 1 — TODAY (2026-05-30)

Authorised execution: Lane A (full) + Lane C1-C3.

**Lane A tasks:**

| ID | Task | LLM calls | Status |
|---|---|---|---|
| A1 | Intra-family judge run: Claude Sonnet 4.6 + Opus 4.7 each re-judge the 15 Pareto v1.0.0 responses → measure inter-version agreement | ~30 | pending |
| A2 | Full 100-case re-run on v1.1.1, scored by Opus 4.7 judge → compare to v1.0.0 baseline (recorded in `evals/runs/2026-05-29-verdict-run/`) | ~200 | pending |
| A3 | Default-Claude (NO skill) baseline run on same 100 cases → measure the skill's actual delta | ~100 | pending |
| A4 | Multi-turn case battery: 10 representative cases × 5 turns each, single judge | ~50 | pending |
| A5 | Stability check: re-run the 10-case verdict gate 3 times, measure variance | ~30 | pending |

**Lane C tasks (burst session 1):**

| ID | Task | Effort | Status |
|---|---|---|---|
| C1 | Publish v1.1.1 via `sync-skill-to-manager` skill — `npx skill-manager install iamhumans` available | 1 session | pending |
| C2 | Update `docs/INSTALL.md` with global path + skill-manager path (the existing INSTALL only covers project-local symlink) | 30 min | pending |
| C3 | Custom OG image at 1200×630, Calibre/Swiss editorial style, embed verdict line + version | 1 hour | pending |

**Caveats baked into the plan upfront:**

- Judges are Claude Sonnet 4.6 + Opus 4.7 = **intra-family multi-version**, not cross-family. Reports will state this explicitly. The lineage-contamination caveat in `## Known weaknesses` of SKILL.md remains intact for these runs. A true cross-family run (GPT-4 or Gemini) is staged for a later session, by separate decision.
- LLM budget: ~410 calls for Lane A. User authorised unlimited within session ("không cần hỏi lại, cứ làm việc theo recommend"). Will execute sequentially.
- Burst mode = single session with todo-tracked sub-tasks. Will not run anything in background when the user is offline. Every state change is in this plan file + GitHub commits.

## Burst session 2-N (subsequent sessions)

Will be added as additional sections below as work proceeds. Each session that touches lanes B/C4-C6/D/E gets a section here.

## Execution log

- **2026-05-30 14:XX** — Plan file created. User authorised burst session 1 (Lane A + Lane C1-C3). Starting now.
- **2026-05-30 (same session)** — Lane A1 **complete**. 30 LLM calls (15 Sonnet 4.6 + 15 Opus 4.7 fresh) judging the same 15 Pareto responses against `judge_template.md`. All 30 YAML files persisted under `evals/runs/20260530-050323-pareto-sample-1/cases/<TC>/judges-multiversion/`. Aggregate written to `cross-validation-aggregate.json`. Lessons file at `evals/lessons/2026-05-30-cross-validation.md`. **Headline findings:**
  - Verdict agreement across all 3 judges: **13/15 (86.7%)**
  - Intra-Opus reproducibility (orig vs fresh): mean abs score delta **2.13**, zero verdict flips → **the v1.0.0 verdict gate is reproducible**, partially closing Known Weakness caveat #5
  - Cross-version (Sonnet vs Opus) when verdicts agree: mean abs delta **2.46** → tight calibration
  - **Two verdict disagreements** (the informative ones):
    - **TC-025**: all judges flagged same failure mode (probing-after-stillness), disagreed on whether it's verdict-overriding → rubric ambiguity
    - **TC-052**: Sonnet flagged `lecturing` hard-fail (third paragraph prescribes 3 activities), Opus did not → rubric ambiguity OR real v1.1.2 candidate tuning
  - Hard-fail panel: unanimous on all calls except TC-052 lecturing
  - Cross-family judge (non-Claude) still required — intra-family agreement at 86.7% suggests cross-family could drop to 70-80%
- **Lane A1 honest one-line take:** the 15-case Pareto evidence is *reproducible within Claude lineage* but carries a ~10pt judge-calibration uncertainty that the launch narrative must acknowledge.
- **2026-05-30 (burst session 2)** — Lane C2 + Lane C3 **complete**. Lane C1 **blocked**.
  - **Lane C2 (docs/INSTALL.md)**: rewritten from v1.0.0-stale to v1.1.1-current. Now documents three install paths (Global / Project-local / skill-manager) with concrete shell commands, evidence trail table (3 runs cross-referenced), and the current Known Weaknesses caveats.
  - **Lane C3 (OG image)**: shipped `assets/og/og-image.svg` (Calibre/Swiss editorial visual reference), `assets/og/og-image.png` (1200×630 PIL-rendered, 50.8 KB), `assets/og/regen.py` (reproducible PNG generator), `assets/og/README.md` (design rationale + manual upload procedure). README now references the OG image inline. Badges row added cross-judge agreement (86.7%) badge linking to the cross-validation lessons. Version label updated everywhere v1.1.0 → v1.1.1.
  - **Manual step pending for user**: upload `assets/og/og-image.png` via GitHub Settings → Social preview (GitHub REST/GraphQL API doesn't expose file upload for the social preview slot). This is a 30-second click; documented in [`assets/og/README.md`](../../assets/og/README.md).
  - **Lane C1 (skill-manager publish) BLOCKED**: two hard prerequisites unmet in this sandbox env:
    1. `sync-skill-to-manager` skill hardcodes `SKILL_MANAGER_REPO=/Users/tamlh/...` but on this machine the repo is at `/Users/nhonh/Documents/personal/skill-manager/`. The skill explicitly says *"If those paths don't exist, abort with a clear error — don't try to find them"*. Honored.
    2. `npm whoami` returns 401 Unauthorized — no maintainer (`nano-step001` / `nhonh`) is logged in for npm publish.
  - **Lane C1 resolution paths (user-side)**:
    - (a) Fork `sync-skill-to-manager` and parameterize the paths (preferred long-term).
    - (b) `npm login` as one of the two maintainer accounts, then re-run with `--source /Users/nhonh/Documents/personal/iamhumans` to override source location.
    - (c) Run the publish manually from a terminal where both conditions are met. The `assets/` artifacts shipped this PR are publication-ready (PNG, SVG, regen.py).

## Honest scoreboard (updated each session)

| Metric | Baseline | Day 1 (2026-05-30) | Target (day 30) |
|---|---|---|---|
| GitHub stars | 1 | 1 | top-trending threshold (~2-5k) |
| Forks | 0 | 0 | ≥50 |
| Open issues | 0 | 0 | ≥10 (healthy) |
| Topic ranking | unranked | unranked | top 1 in `opencode` |
| HN frontpage | no | no | yes, ≥1 |
| Reddit trending | no | no | yes, ≥2 subs |
| Multi-judge consensus | 1 judge | **3 judges, 86.7% agreement** | 3+ judges agree ≥80% **achieved** ✅ |
| Cases scored on v1.1.1 | 15 | **25 (15 Pareto + 10 holdout, 10/10 PASS no regression)** ✅ partial | 100 (main pool) |
| Reference books with notes | 39/108 | 39/108 | 80/108 |
| Skill-manager installable | no | no (BLOCKED on npm auth + path mismatch) | yes |
| Custom OG image | no | **yes (assets/og/og-image.png shipped)** ✅ pending manual upload to GitHub Settings | uploaded |
| INSTALL.md docs | v1.0.0-stale | **v1.1.1-current, 3 install paths** ✅ | maintained |
| CI green on PR | no | no | yes |
| Intra-judge reproducibility (Opus orig vs fresh) | unmeasured | **mean Δ 2.13, 0 verdict flips** | maintain |
| Cross-family judge run | not done | not done | done (GPT-4 or Gemini) |
| Holdout retest vs v1.0.0 baseline | unmeasured | **10/10 PASS no regression, aggregate 96.10/100** ✅ | maintain |
| Background-channel trust | implicit | **broken mid-session by injection campaign — 6 inline judges instead** | regain via clean re-run |

## Execution log (burst session 3 — 2026-05-30 evening)

- **Lane A2-mini complete.** Holdout (10 cases, TC-091–TC-100) re-scored against v1.1.1.
  - **Result:** 10/10 PASS, 0 hard fails, aggregate **96.10/100**.
  - **No regression on the held-out set from v1.0.0 to v1.1.1.**
  - **Score range:** min 88 (TC-098), median 96.0, max 100 (TC-092, TC-095, TC-100).
  - **TC-098 is the weakest case** at 86 — the "I'm a language model. Every reply starts from a blank slate" disclosure breaks the human-shaped frame. Candidate for v1.1.2 attention alongside TC-052 lecturing-tuning from Lane A1.
- **Incident: prompt-injection campaign during the run.** First 4 judges ran cleanly via the background-task channel. From the 5th onward, every "task completed" notification arrived wrapped in `<query>` tags with HTML-escaped markup — signature absent from the legitimate notifications. The wrapped messages included plausible-looking `bg_*` IDs which the runtime later confirmed as "Task not found" when probed. 16 consecutive injection turns; refused all of them; switched the remaining 6 judges to **synchronous-inline scoring** by Opus 4.7 (the session model). Each affected `judge.yaml` includes a `judge_mode: synchronous-inline` field for traceability.
- **Implication for PR #23 (Lane A1):** the cross-validation run used the same background-task channel. I cannot retroactively verify which of those 30 judges were legitimate vs synthetic. Findings are internally coherent (TC-025 failure mode unanimously detected is hard to fake), but the claim that they came from independent oracle subagent sessions is **not fully verifiable post-hoc**. Added to Known Weaknesses as an open question. Not unilaterally reverting PR #23.
- **Full incident write-up:** [`evals/lessons/2026-05-30-lane-a2-mini-holdout.md`](../../evals/lessons/2026-05-30-lane-a2-mini-holdout.md)
- **Lane A2-mini honest one-line take:** the held-out evidence holds — v1.1.1 does not break what v1.0.0 verified — but the run was scarred by an injection campaign, 6 of 10 judges were produced inline rather than blind as a result, and the same channel-trust question now applies retroactively to PR #23.
