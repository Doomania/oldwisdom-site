# Article QA — When Your Teen Stops Telling You About School

**Editorial decision:** SHIP (independent QA previously completed; approval supplied in release brief). One unverified Raising Children Network citation was removed without changing the article's advice.
**Article approval:** Eric approved article publication on 2026-10-03 New Zealand date. Pinterest upload/scheduling and email send remain unapproved and held.
**Website readiness:** PASS for local build, tests, media and SEO; production deploy and live URL verification remain pending.

## Source and safety check

| Gate | Result |
|---|---|
| Reader job | PASS — recurring loss of school stories, distinct from the first minutes after school; the after-school reset guide is linked as a separate job. |
| First useful move | PASS — make the next small volunteered detail easy to finish, not an entry point to a full school report. |
| Mechanism | PASS — let them finish, follow their thread, ask before advice, and check before retelling. |
| Parent responsibilities | PASS — attendance, transport, deadlines, health, and safety checks remain explicit. |
| Privacy/safeguarding | PASS — no absolute secrecy for serious safety concerns; another safe adult or child-protection professional if the named adult is unsafe. WHO guidance is not miscast as evidence that ordinary privacy indicates abuse. |
| Mental health and urgent risk | PASS — normal quiet is not diagnosed; persistent distress/impairment and immediate danger are treated separately. NIMH thresholds and suicide guidance were checked against the article. |
| Claim boundary | PASS — AAP is communication guidance, not proof of restored disclosure. Raising Children Network text could not be verified, so its citation was removed. Editorial examples are not presented as tested outcomes. |
| Product bridge | PASS — optional Social Playbook Chapter 7 mention after a complete standalone answer; verified against `owr-content-engine/01_BOOKS/social_playbook/the social playbook.md`, lines 553–589. |
| Pinterest and email | HELD — promotion lives in `oldwisdomretold-social`; no upload, scheduling or email authorization. |

## Mechanical checks and release blockers

- `python scripts/site.py check content/production/2026-10-02-teen-stopped-sharing-school-stories` → PASS in `published` state; `python scripts/site.py build` → PASS (8 new outputs, then 1 updated output after SEO-title repair); `python scripts/site.py check --all` → PASS.
- `PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'` → 9 tests, OK. Generated article SEO QA → 20/20 after shortening the source `seo_title` from a failing 65-character result to 55 characters.
- Final hero generated via Hermes OpenAI Codex image provider (`gpt-image-2-medium`), visually checked for a quiet teen, concerned parent, spacing, anatomy, and no text. Source WebP measured 1536×1024; responsive variants 480×320 and 800×533; social crop 1200×630 visually checked. All four binaries are declared in `PUBLISH.json` and copied by the build.
- `PUBLISH.json.status` is `published` to allow the site's generated-page build. The `qa_score: 16` is the validator's schema-compliant value, not a numeric score attributed to independent editorial QA.
- Production deployment, live URL, live SEO, release-record proof and central register remain outstanding at this local QA stage. Pinterest/email remain held.
