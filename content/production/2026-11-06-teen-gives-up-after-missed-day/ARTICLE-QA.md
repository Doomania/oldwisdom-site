# Article QA — When Your Teen Gives Up After One Missed Day

**State:** `ARTICLE_LIVE — VERIFIED 2026-11-07 NZDT`. The first independent editorial audit on 2026-11-06 found a repairable **BLOCK for publication**, v4 §15 **19/20** (A–H and J 2; I credibility 1), no v4 hard fail. The four corrections below passed an independent focused recheck at **20/20**, with no hard fail. Eric approved this article only on 2026-11-07 NZDT; Pinterest and email remain held. `PUBLISH.json.status=published` renders the article; `RELEASE.json.article.state=live` records the separately verified production release.

## Preserved first independent finding and repair

1. `ARTICLE.md:1` audience comment leaked visibly through the minimal renderer. **Removed** the HTML comment; retain audience in `PUBLISH.json` and content card.
2. `ARTICLE.md:16` ISPA PDF link served a challenge/HTML to a reader. **Replaced** with the full original-study PDF mirror inspected by both author and independent QA; kept publisher DOI and the access caveat in `SOURCES.md`. Recheck reader access before article release.
3. `ARTICLE.md:8` implied every teen who declines the goal names a next chance. **Recast** as an invitation only if they want to continue.
4. `ARTICLE.md:74` made a single symptom sound like a clinical referral rule. **Narrowed** the second branch to ongoing, concerning wider changes and explicitly rejected diagnosis from one isolated sign; NIMH support remains adjacent.

**Focused recheck closed (2026-11-06):** A separate read-only reviewer verified all four fixes, opened the replacement PDF and matched DOI 10.1002/ejsp.674, reconfirmed the AAP and NIMH material, and tested all eight article links (HTTP 200). In-memory rendering: 8 H2, 3 H3, one list, six blockquotes; no leaked comment/table/rule. Review-stage templated title 53 characters and description 147. Scoped and repository-wide bundle checks, 9 tests, and `git diff --check` passed. **Verdict: READY_FOR_REVIEW, 20/20.** Media, site build/deploy and live URL were then release-stage gates.

## Author-side initial gate notes (historical, before approval)

- **Evidence / claims:** `CONTENT-CARD.yaml` and `SOURCES.md` preceded article drafting. The full Lally et al. paper was examined through an accessible mirror after the supplied ISPA repository link presented a bot challenge/403; it reports 96 enrolled, 82 with sufficient data for the main analysis, and a smaller omission comparison (140 omissions across 55 participants, 67 with next-day data after resumption). Article avoids participant counts and frames adult single-omission/automaticity result only as a narrow counterexample to an inevitable-erasure claim. AAP Ginsburg wording was initially checked via search-index excerpts only; independent reviewer subsequently read the full live AAP page and confirmed the qualified wording. NIMH persistent-symptom and urgent actions were directly fetched and have adjacent primary-source links. No parent method, teen restart, or book efficacy claim. **Focused reviewer to verify the corrected link and wording.**
- **Parent-first / busy-parent check:** The opening names the situation, immediately offers the neutral next-chance question, and gives an actionable script and three blanks (what/when/if barrier); refusal, owed promise and safety lanes are present. Reviewer to assess whether the article can be shortened without losing value and whether the emergency section is proportionate.
- **Portfolio separation:** A personal missed-day restart is not a recipient-facing missed promise (`reliability-signal`), daily homework reminder handoff (`stop-reminding-homework`), getting started before work (`task-start-runway`), or evening phone design (`phone-takes-whole-evening`).
- **Authority / ownership:** Teen chooses to resume, revise or stop a personal goal; parent retains school, household, access and immediate safety responsibilities. Check wording around sibling care and team duties for feasibility and respect, not an automatic pass for an externally owed obligation.
- **Book / scope:** Free article is complete before optional Chapter 1 sample bridge. Public sample is *The Promise Nobody Heard* (one action and rough when), not a missed-day excerpt. No hero, promotion, email or pin files. Review manifest has no published date/media; no public action authorised.
- **SEO / language:** Query phrase appears in title and opener. Search and Reddit language are hypotheses only; card's eight persona scores are constructed objections, not research or a real panel. Reviewer to check natural search intent, title length, source-link fidelity and mobile rendering later.

## v4 §15 independent editorial score after focused recheck

| Dimension | Review prompt | Score |
|---|---|---|
| Teen understanding | Multiple plausible perspectives, no motive claim? | 2 |
| Parent reflection | Parent considers own interpretation, not blamed? | 2 |
| Intent versus impact | Possibility, not causal guarantee? | 2 |
| Educational direction | Transfer skill beyond one-day compliance? | 2 |
| Practical value | One question, refusal branch, feasible next chance? | 2 |
| Authority balance | Real duties and safety limits protected? | 2 |
| Teen ownership | Teen chooses, parent does not manage streak? | 2 |
| Respect | No character verdict, no diagnosis? | 2 |
| Credibility | Source details and adjacent citations exact? | 2 |
| Distinctiveness | Standalone OWR parent/teen handoff, no overlap? | 2 |

**Hard-fail review:** Independent reviewer found none in the corrected draft: no unsupported causal/clinical claim, fabricated evidence, book-first sales pitch, misleading sample, teen agency loss, erased owed duty or missing urgent support. Eric's separately scoped article approval was recorded on 2026-11-07; release-stage checks and live verification remain.

**Technical verification (2026-11-06):** Scoped and repository-wide `python scripts/site.py check` passed with `PUBLISH.status=review`; `python scripts/site.py build --check` confirmed the existing generated output is current (S2 not generated); `python -m unittest discover -s tests` passed 9/9. `git status --short --branch` showed `main...origin/main` and only the untracked S2 bundle; `git diff --check` exited 0. These are schema/regression checks, **not article/media approval, a release build, or publication**. Site publication, media generation, deployment, Pinterest and email remain separate gates.

**Article-only release staging (2026-11-07 NZDT):** GPT Image 2 generated one editorial scene; the original was visually checked for topic fit, realistic people/hands and clean text-free background before deterministic WebP crops. Website hero 1536×1024, responsive 800×533 and 480×320, and social/OG 1200×630 were opened and checked for intact people, shoes and bag. SEO preflight initially scored 19/20 because the 147-character description was below its required range; revised description to 155 characters and rebuilt. `python scripts/seo_article_qa.py articles/teen-gives-up-after-missed-day.html --canonical https://oldwisdomretold.com/articles/teen-gives-up-after-missed-day --keyword 'teen gives up after a missed day'` now scores **20/20**. Bundle and repo checks, build current check, nine tests, and the diff whitespace gate with intentional SOURCES.md Markdown hard breaks exempted passed. At that staging point, provider deployment and live URL smoke were still pending (subsequently verified below). Native Edge headless desktop screenshot was visually sound. A 390px `--window-size` screenshot initially clipped because Edge kept a wider layout viewport; an explicit CDP 390×844 device-metrics override measured `innerWidth=390`, `scrollWidth=390`, H1/hero within x=20..370, and its captured screenshot showed intact title, summary and hero. The 500px capture also fit. No Pin or email action authorised.

**Independent predeploy release QA (2026-11-07): SHIP for the article only.** Separate read-only reviewer checked the generated HTML and article, approval scope, exact reader-facing Lally PDF (HTTP 200, `application/pdf`, `%PDF`), AAP/NIMH claims, all four image dimensions/crops and byte-identical generated copies, Parent Hub, sitemap, `llms.txt`, internal targets, bundle/repo/build-current checks, nine tests, and the repaired 155-character SEO description (**20/20**). No blocker. This verdict did not itself certify live deployment; canonical production URL and media were subsequently verified.

**Live verification (2026-11-07 NZDT):** Commit `11ce09da13a3f5b7fa996bbe8e0a33b9c13cd28f` pushed; Cloudflare Pages check completed **success** 2026-11-06T11:30:57Z. The clean canonical article URL returned HTTP 200 and live SEO **20/20**. Parent Hub, sitemap and `llms.txt` returned HTTP 200 with this article entry. Main, 480, 800 and social WebP URLs each returned HTTP 200 and matched their committed assets byte-for-byte. The exact reader-facing Lally PDF (`1931422` bucket) returned HTTP 200 `application/pdf` with a PDF signature; a different `1931222` variant returned 404 and is **not** the article link. Pinterest and email remain held.
