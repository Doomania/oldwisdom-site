# Article QA — Why Your Teen Won’t Talk After School

**Bundle:** `2026-08-15-teen-wont-talk-after-school`
**Status:** `LIVE_VERIFIED`
**Final editorial score:** `20/20`
**Approval scope:** Eric approved this release package on 2026-08-15: article build/deployment and Pinterest scheduling are authorised. Email draft preparation is authorised; email send remains unauthorised pending a separate explicit send approval and provider preflight.

## Editorial gate

| Gate | Score | Result |
|---|---:|---|
| Audience job and immediate usefulness | 2/2 | PASS |
| Ordinary language and household realism | 2/2 | PASS |
| Framework order and actionability | 2/2 | PASS |
| Teen ownership and parent authority | 2/2 | PASS |
| Safeguarding branch | 2/2 | PASS |
| Evidence and claim boundaries | 2/2 | PASS |
| Scripts and observable language | 2/2 | PASS |
| Portfolio distinctiveness | 2/2 | PASS |
| Email and five-Pin copy package | 2/2 | PASS |
| Credibility and source mapping | 2/2 | PASS |

## Content verification

- 1,615 source words after duplicate-language repairs; ten scannable sections.
- SEO title: 38 characters before the site suffix; description: 153 characters.
- The narrow job is the home-arrival transition, not quiet personality, loneliness, confidence, diagnosis or broad relationship avoidance.
- RESET → NOTICE → INVITE → RETURN is labelled as editorial synthesis, not a clinical tool.
- No universal reset interval, mind-reading claim, diagnosis, disclosure promise or surrender of safety authority.
- The action path gives parent scripts, ordinary expectations, observable pattern checks and a clear immediate-risk bypass.
- Existing-portfolio overlap audit found no substantive copied section; remaining long-string overlaps are source URLs and standard safety phrasing.

## Source verification

- Directly inspected: Zapf et al. systematic review, Baudat et al. adolescent information-management study, Vijayakumar and Pfeifer disclosure review, and NIMH child mental-health guidance.
- HealthyChildren’s timing guidance was accessible through current search-index text rather than direct body extraction; `SOURCES.md` states that limitation explicitly.
- Observational and mostly cross-sectional evidence is described as association, not causation.

## Hero QA

- Unique GPT Image 2 full-generation; no composite or reused photography.
- Master: 1536×1024 WebP; responsive variants: 800×533 and 480×320; social: 1200×630.
- Master and corrected social crop passed emotional-fit, face visibility, anatomy, realism, no-text, no-logo and crop-safety review.
- The first social crop was rejected for black sidebars and regenerated correctly before approval readiness.

## Distribution readiness

- `EMAIL.md`: one parent-first email draft and one article CTA.
- `PINTEREST.md`: exactly five finished parent-first creatives with unique campaign content IDs and five distinct creative forms.
- All five decoded binaries are unique 1024×1536 one-pass GPT Image 2 generations and passed the approval gate before scheduling.
- Individual exact-text/emotional-truth review: PASS. Mechanical gate: PASS. Side-by-side contact-sheet review: PASS.
- Scheduling was explicitly approved; all five pins are now verified on Pinterest's Scheduled Pins page. Publishing remains time-gated and requires post-publication verification.

## Pinterest QA evidence

- Queue: `D:\Hermes\workspace-import\projects\oldwisdomretold\pinterest_assets\static_generated\quiet_after_school_batch_20260815\APPROVAL_QUEUE.json`
- Gate report: `D:\Hermes\workspace-import\projects\oldwisdomretold\pinterest_assets\static_generated\quiet_after_school_batch_20260815\qa\gate_report_quiet_quiet_20260815_145520.json`
- Contact sheet: `D:\Hermes\workspace-import\projects\oldwisdomretold\pinterest_assets\static_generated\quiet_after_school_batch_20260815\qa\gate_contact_sheet_quiet_quiet_20260815_145520.jpg`

## Mechanical verification

- `python scripts/site.py check content/production/2026-08-15-teen-wont-talk-after-school`
- Result: `PASS: Publishing Bundles are valid.`
- `python -m unittest discover -s tests -v`: 10/10 PASS.
- `python scripts/seo_article_qa.py ...`: 20/20 PASS.

## Production verification — 15 August 2026

- Published through merged PR `#18` to `main`.
- Clean article URL returns HTTP 200 with the approved H1, canonical URL and Article JSON-LD.
- Live hero, social image, Parent Hub, `sitemap.xml` and `llms.txt` all return HTTP 200.
- Live SEO QA: 20/20; canonical, keyword and metadata checks pass.
- Distribution authorisation captured from Eric on 15 August 2026; article deployment and Pinterest scheduling completed.
- Email sending remains a separate irreversible action and is not authorised by this record.
