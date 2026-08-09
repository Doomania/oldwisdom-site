# oldwisdomretold.com

Static site for **Old Wisdom // Retold** — a teen-growth platform for ages 12–17. Teen-facing Playbooks turn durable ideas from strategy, philosophy, and human psychology into practical tools; the separate Parent Hub helps adults support teen judgment, capability, ownership, and independence without taking over.

Live: https://oldwisdomretold.com

## Structure
```
index.html      platform homepage — mission, Playbooks, Parent Hub, FAQ, email capture
quiz.html       15-question social skills reflection → suggests useful places to begin
articles/       static parent guides using the existing site design and metadata conventions
parents/        generated Parent Hub, organised by the Parent Growth Journey
assets/         covers, mockups, article and social images
automation/     evergreen topic queue and publication tracking
content/        review-gated evergreen production batches, including Pinterest packages
scripts/        Parent Hub publisher and repeatable local QA gates
templates/      shared static Parent Hub page shells
config/         site configuration for static publishing
robots.txt      crawler rules (all allowed + sitemap ref)
sitemap.xml     production URL index
llms.txt        AI-engine site map (platform, Playbooks, Parent Hub, articles)
```

The deployed site is plain static HTML. The Parent Hub uses a Python standard-library build step before commit; production still has no runtime application server or package manager. CDN fonts and GSAP are used only for homepage presentation.

## Runtime translation

English remains the source and canonical version of every page. A shared,
on-demand GTranslate control lets visitors machine-translate the page in their
browser without creating duplicate language URLs or changing the Hermes
publishing workflow. The third-party translator is loaded only after a visitor
opens the **Language** control.

`assets/site-tools.js` owns the translator and article back-to-top behaviour;
`assets/site-tools.css` owns their shared presentation. Every standalone HTML
page must load both files. Parent Hub templates already include them, so newly
generated guides inherit the controls automatically. Machine-translated text
is a convenience layer, not reviewed editorial copy and not multilingual SEO.

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
- Score 0–3 per answer → 4 profile tiers, with three lower-scoring areas to explore
- Routing: results explain those skill areas and offer Playbooks only where relevant
- Email gate posts to Brevo (`sib-form-quiz`) via `fetch`, no page navigation
- Share: parent path → native share sheet + WhatsApp; teen path → copy-caption first

## Article SEO QA
Run before approval and again against the live clean URL after deployment:
```bash
python scripts/seo_article_qa.py articles/quiet-kids-and-confidence.html --canonical 'https://oldwisdomretold.com/articles/quiet-kids-and-confidence' --keyword 'quiet teenager confidence'
```
The gate checks title/meta length, indexability, canonical/OG agreement, headings, content depth, keyword placement, internal and authority links, image optimization, Article schema, author entity, and visible publication details.

## Parent Hub publishing

Hermes works in one review-gated Publishing Bundle under `content/production/`.
The bundle's `PUBLISH.json` controls Parent Growth stage, teen outcomes, release
move, optional next step, and publication status. Hermes does not edit HTML,
schema, sitemap, `llms.txt`, templates, or application code.

```bash
python scripts/site.py check content/production/<bundle>
python scripts/site.py build
python scripts/site.py check --all
```

`build` generates `parents/index.html` and manages only the marked Parent Hub
regions of `sitemap.xml` and `llms.txt`. Existing article URLs stay under
`/articles/<slug>`.

## Deploy
Production is deployed from this GitHub repository to Cloudflare at https://oldwisdomretold.com. Push only after approval and local QA; then verify the Cloudflare deployment and live URL.

## Editing checklist
- [ ] Keep FAQ visible text and FAQPage schema in sync
- [ ] Run `python scripts/site.py build` and `python scripts/site.py check --all` for Parent Hub changes
- [ ] For articles: run `scripts/seo_article_qa.py`, validate mobile/desktop rendering, and verify the clean live URL after Cloudflare deploy
- [ ] Re-run rich-results test after schema edits
- [ ] Test quiz end-to-end on mobile after JS changes (gate → results → CTA)
