# Article QA — When the Phone Takes the Whole Evening

**State:** ARTICLE_LIVE — Eric approved article-only publication on 2026-11-03. The clean production URL, Cloudflare Pages deployment, SEO, mobile/desktop layout, and media were verified. Pinterest and email remain held. `PUBLISH.json.qa_score=20` records the independent v4 §15 score.

## Scope and evidence audit

- Source-first: `SOURCES.md` records directly inspected Pew survey, CDC ADHD guidance with age limits, NIMH escalation guidance and live OWR book page. Moreno et al.'s primary journal abstract was directly inspected via Europe PMC metadata; the full text and attrition figure were not verified here. The AAP page yielded only indexed excerpts. The revised article makes no reader-facing AAP or trial claim. Local `books/the-discipline-playbook.html` confirms the `#sample` anchor in checkout.
- No claim that a teen-designed first half-hour or weekly check-in has demonstrated efficacy. Survey conflict rate means **at least sometimes**, not every night. Family-plan trial's null result is not proof this distinct practice fails.
- Parent's half leads on opening screen: tonight's line, immediate sleep boundary when late, tomorrow's calm conversation and a response if the teen refuses. It now includes a clock-time example. Distinct from voluntary family leisure, homework reminders, task-specific start and checking a phone for safety/privacy.
- Parent retains sleep, safety and shared-space boundaries; teen chooses and revises the start. Daughters, part-time work, sibling care, grandparents, shared devices, and a step-parent's authority are concrete variants, not generalized demographic claims. ADHD and anxiety trigger adjustment, not diagnosis; persistence/unsafe risk triggers support.
- Book bridge is optional, exact Chapter 1 link after complete free answer, not a scientific citation. Product QA §16: useful without book **yes**; chapter's teen first-action skill **yes**; parent helped first **yes**; teen chooses excerpt **yes**; direct situation fit **yes**.

## v4 §15 original self-assessment (superseded; not independent QA)

| Dimension | 0–2 | Reason |
|---|---:|---|
| Teen understanding | 2 | Multiple possible functions; asks rather than presumes. |
| Parent reflection | 2 | Examines nightly grab and parent distraction. |
| Intent versus impact | 2 | Sleep intent versus possible distrust, qualified. |
| Educational direction | 2 | Start-and-adjust skill beyond tonight's compliance. |
| Practical value | 2 | Opening script, half-hour choice, one-week review. |
| Authority balance | 2 | Legitimate sleep/household/safety limits. |
| Teen ownership | 2 | Teen designs, tries, revises. |
| Respect | 2 | No lazy label or parent shame. |
| Credibility | 1 | Core survey/abstract and health guidance inspected; AAP and trial full-text access gaps require independent check. |
| Distinctiveness | 2 | OWR parent/teen handoff and optional chapter fit. |
| **Self-assessed total** | **19/20** | **Provisional only; independent reviewer must score and check hard fails.** |

## Independent review and revisions

The independent reviewer scored the original draft **18/20**, with practical value and credibility at 1 each, no v4 hard fail, and **FIX** for the busy-parent and evidence-link gates. The revised article adds a clock-time example and refusal script, removes the long research paragraph and unverified attrition figure, and places the NIMH link by the urgent action. A separate targeted recheck scored the revised draft **20/20**, with each v4 dimension 2/2, no hard fail, no remaining line-level fixes, and passing busy-parent, source/link, and optional product-bridge gates. The book-page destination was confirmed previously, though the second QA pass did not independently recheck the live URL.

**Release verification:** focused and repository-wide `site.py check` passed; `python -m unittest discover -s tests` returned 9 tests OK. Local and live article SEO scored **20/20**. Browser rendering at 375, 390, 768 and 1440 px had no horizontal overflow and loaded the responsive hero. Cloudflare Pages check on commit `36c41d9` completed successfully; the clean article URL returned HTTP 200, as did all clean article routes in the smoke test. The Parent Hub, sitemap and llms index contain the URL; all four live WebP binaries match the committed media bytes. Pinterest and email remain `held` and unapproved.
