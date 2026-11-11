# H13 — Discipline cluster intro release record

**Status: LIVE — approved by Eric, independently QA'd, and production-verified 2026-11-11 NZDT**

**Placement:** On `/parents/`, a distinct thematic section immediately after “WHAT HAPPENED THIS WEEK?” and before “THE PARENT GROWTH JOURNEY”; the five-stage journey is unchanged. Section heading: **WHEN FOLLOW-THROUGH GETS HARD AT HOME**. Implementation commit: `0d7e5164cebfa0f3df8573c6b21ae7bb950cf6e1`.

When a phone takes the evening, a plan falls apart after one missed day, or schoolwork becomes a nightly argument, the answer is not to call your teen lazy or take over every task. Start with the problem you can see, keep the limits and support that belong to you, and help your teen choose one workable next move. These five guides cover different moments: an evening start, a personal restart, a homework handoff, the first minutes of a task, and a promise that affected someone else.

1. [When the Phone Takes the Whole Evening: Help Your Teen Take It Back Without Confiscating It](/articles/phone-takes-whole-evening) — agree on a teen-chosen evening start while keeping sleep and household limits.
2. [When Your Teen Gives Up After One Missed Day: Make Room for a Restart](/articles/teen-gives-up-after-missed-day) — ask about the next chance after a missed *personal* plan, without turning the lapse into a verdict.
3. [When to Stop Reminding Him About Homework](/articles/stop-reminding-homework) — hand daily homework tracking to your teen with a calm weekly review and clear reasons to step back in.
4. [Help Your Teen Start Tomorrow’s Work Without Taking It Over](/articles/task-start-runway) — clear one blocker and prepare a small first action for one work session, not a nightly homework system.
5. [When Your Teen Worries They Seem Unreliable](/articles/reliability-signal) — address a missed commitment to someone else and practise one visible next action; do not promise restored trust.

**QA/source notes:** H13 order and shape: `docs/OWR_HERMES_ACTION_PLAN_2026-11.md` §§3, 5.3; parent-first framing: `docs/OWR_Parent_Gateway_Hermes_Execution_Manual_v4.md`, `docs/OWR_CONTENT_DIRECTION_2026-11.md`, and `feedback.md`; guide titles and distinct jobs: the five corresponding `content/production/*/ARTICLE.md` files (the fifth link uses its shorter live H1/card label). Independent copy QA initially returned FIX for misattributed live-check evidence; corrected before Eric's approval. Independent implementation QA returned SHIP. Site build, `check --all`, `build --check`, nine tests, and whitespace-exempt diff check passed. Chrome desktop (1440px) and mobile (390px) rendering showed legible copy with no horizontal overflow. After deployment, `/parents/` and CSS returned HTTP 200 with the new section and five ordered links; all five guide destinations returned HTTP 200; the existing journey remained intact. No Pinterest or email action was approved or taken.
