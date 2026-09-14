# Article QA — teen apology guide

**Status:** `PASS — 2026-09-14`

## Initial independent result — 2026-09-14

- Verdict: `BLOCK`.
- Context 5/5; originality 4/5; GEO 4/5; evidence 1/5; expertise 4/5; experience 4/5; authority 1/5; trust 2/5.
- Findings preserved: uncited compound safety branches; unsafe delete/preserve wording around sexual material; ungrounded no-mediation rule; visible renderer artifacts; missing source record; SEO metadata length failure; premature `qa_score: 20`.

## Repair record

- Split urgent safety guidance into self-harm/immediate-danger, sexual-image, stalking, and ongoing-bullying branches.
- Added adjacent reader-facing authority for every material branch.
- Confined ordinary deletion advice to non-sexual material; explicitly prohibited copying, downloading, or forwarding sexual/possibly illegal material as proof.
- Labelled the no-contact/no-mediation position as OWR's conservative safeguarding floor.
- Removed the visible horizontal-rule token and inline-code backticks.
- Added `SOURCES.md` and `CLAIM-LEDGER.md` with scope and jurisdiction limits.
- Adjusted SEO title/description and lowered `qa_score` pending recheck.
- Focused recheck returned `BLOCK` for one remaining overbroad branch: physical danger and unspecified self-harm risk were combined under WHO suicide guidance. Split them into separately sourced physical-danger and immediate-self-harm-danger actions.

## Final independent acceptance

- Verdict: `SHIP`, 2026-09-14.
- Physical danger and immediate self-harm danger are separately sourced and separately rendered.
- Source scopes, renderer output, metadata, readability, and bundle validation passed.
- Repository tests: 10/10 passed.
- GPT-Image-2 hero QA passed: the teen owns the phone and apology; the parent is attentive without touching, pointing, or taking over; no visible text, anatomy fault, logo, or watermark.
