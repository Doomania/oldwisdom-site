# oldwisdomretold.com

Static site for **Old Wisdom // Retold** — a book series for teens 12–16 that rebuilds classic wisdom (Sun Tzu, Carnegie, the Stoics) into game-style playbooks.

Live: https://oldwisdomretold.com

## Structure
```
index.html      series hub — hero, definition strip, book series, FAQ, email capture
quiz.html       15-question social skills diagnostic → routes to the Playbooks
articles/       static parent guides using the existing site design and metadata conventions
assets/         covers, mockups, article and social images
automation/     evergreen topic queue and publication tracking
content/        review-gated evergreen production batches, including Pinterest packages
scripts/        repeatable local QA gates, including article SEO
robots.txt      crawler rules (all allowed + sitemap ref)
sitemap.xml     production URL index
llms.txt        AI-engine site map (series, books, articles)
```

No build step. No dependencies beyond CDN fonts + GSAP on the homepage (animation only, content is static HTML).

## Books
| # | Title | Source wisdom | Amazon |
|---|---|---|---|
| 1 | The Social Playbook | Dale Carnegie, Socrates | a.co/d/0gjqlkB6 |
| 2 | The War Playbook | Sun Tzu | a.co/d/0gu0a2CR |
| 3 | The Discipline Playbook | Stoics | in production |

## GEO (AI search) setup
- JSON-LD on both pages: `BookSeries`, `Book`×2, `Person`, `FAQPage`, `WebSite`/`Quiz`/`BreadcrumbList`
- Visible FAQ text mirrors schema exactly (index.html `#faq`)
- `llms.txt` at root — keep in sync when a book status changes
- Validate after any content edit: https://search.google.com/test/rich-results

## Quiz logic (quiz.html)
- 15 scenarios, 3 per category: connection / room reading / influence / conflict / confidence
- Score 0–3 per answer → 4 profile tiers, top-3 weakest categories = "gaps"
- Routing: results explain the weakest gaps and offer both Playbooks as relevant tools
- Email gate posts to Brevo (`sib-form-quiz`) via `fetch`, no page navigation
- Share: parent path → native share sheet + WhatsApp; teen path → copy-caption first

## Article SEO QA
Run before approval and again against the live clean URL after deployment:
```bash
python scripts/seo_article_qa.py articles/quiet-kids-and-confidence.html --canonical 'https://oldwisdomretold.com/articles/quiet-kids-and-confidence' --keyword 'quiet teenager confidence'
```
The gate checks title/meta length, indexability, canonical/OG agreement, headings, content depth, keyword placement, internal and authority links, image optimization, Article schema, author entity, and visible publication details.

## Deploy
Production is deployed from this GitHub repository to Cloudflare at https://oldwisdomretold.com. The site is plain static files from the repository root: no local build command and no package manager. Push only after approval and local QA; then verify the Cloudflare deployment and live URL.

## Editing checklist
- [ ] Keep FAQ visible text and FAQPage schema in sync
- [ ] Update `llms.txt` + `sitemap.xml` when adding a book, article, or page
- [ ] For articles: run `scripts/seo_article_qa.py`, validate mobile/desktop rendering, and verify the clean live URL after Cloudflare deploy
- [ ] Re-run rich-results test after schema edits
- [ ] Test quiz end-to-end on mobile after JS changes (gate → results → CTA)
