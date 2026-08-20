# Production-Package QA — When Your Quiet Teen Freezes in Group Work

**Status:** `READY_FOR_RELEASE_AND_SCHEDULING_APPROVAL`  
**Boundary:** The source bundle, images, email draft, and Pinterest creative are complete. Nothing has been built into production, deployed, uploaded, scheduled, sent, or posted.

## Article

| Gate | Result |
|---|---|
| Editorial approval | PASS — Eric approved 2026-08-20 |
| Parent-first, quietness not pathologised | PASS |
| Distinct mechanism | PASS — RESET → NOTICE → INVITE → RETURN; Enter → Contribute → Recover |
| Teen ownership and proportionate escalation | PASS |
| Source map | PASS — `SOURCES.md`; NIMH safety link appears in the article |
| Readability | PASS — 1,715 words; Flesch–Kincaid grade 6.2; complex words 2.4% |
| OWR article QA | PASS — 9/9 standards |
| Bundle schema | PASS — `python scripts/site.py check content/production/2026-08-20-quiet-teen-group-work` |

## Hero

| Gate | Result |
|---|---|
| Unique scene | PASS — quiet teen pauses beside a classroom group; parent remains discreetly in doorway |
| Output | PASS — 1536×1024 WebP; 800px and 480px responsive WebPs; 1200×630 social WebP |
| Pixel QA | PASS — no text, watermark, crop defect, or invented product imagery |

## Pinterest campaign

| Gate | Result |
|---|---|
| Finished assets | PASS — five one-pass GPT Image 2 1024×1536 PNGs |
| Copy | PASS — titles 45–50 characters; descriptions 340–383 characters; four end hashtags each; literal alt text |
| Diversity | PASS — five distinct forms: editorial, pen-pal note, checklist, recovery scenario, strategy map |
| Visual QA | PASS — full-size review plus contact sheet; no garbled on-image copy accepted |
| Mechanical gate | PASS — no layout clone pairs, metadata failures, routing failures, palette warnings, or batch text-diversity failures |
| Audit report | `media/pinterest-audit/gate_contact_sheet_pin-01-group-work-freeze_pin-05-parent-plan_20260820_171505.jpg` |

## Email

- PASS — parent email draft is present in `EMAIL.md`; no ESP draft or send action was taken.

## Required approvals before public action

1. **Release approval:** build the approved bundle, run full local QA, commit/push, and verify the live clean URL.
2. **Scheduling approval:** after the destination is live, schedule the five audited Pinterest pins; no pin is currently uploaded or scheduled.
3. **Email approval:** create and send only after separate review of the final email in the ESP.
