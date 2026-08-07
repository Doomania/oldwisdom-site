# GEO + Conversion rework — commit to Doomania/oldwisdom-site (root)

- Replaced the previous book renders with the July 2026 wraps: extracted the baked checkerboard, normalized all three mockups to a consistent 5:7 transparent canvas, rebuilt the three-book group, and added a dark 1200 × 630 social-sharing image with versioned filenames for cache-safe rollout.

## Site and content groundwork — 18 July 2026

- Preserved the root URL as the book-series and quiz landing page for existing Pinterest traffic, restored book/quiz-first navigation, and added explicit Amazon tracking to both live book cards.
- Hardened the homepage for mobile-first indexing and phone visitors with safe-area support, 44px navigation targets, a compact first viewport, and a no-CDN animation fallback that leaves all content visible.
- Strengthened SEO, GEO, and Pinterest extraction with a clearer series description, expanded Open Graph metadata, explicit `WebSite` and `BookSeries` JSON-LD nodes, stable canonical URL, and visible book names above the fold.
- Fixed the quiz email gate so it saves to Brevo without navigating away before results appear.
- Replaced three missing sample-page images with an honest HTML explanation of the book's chapter rhythm.
- Added the evergreen content queue and review-gated production bundles used for articles, videos, shorts, Pinterest pins, metadata, and source audits.

## index.html
- Meta description → extraction format (series definition, both books named)
- Added: canonical, OG/Twitter tags (share cards were bare before)
- JSON-LD @graph: BookSeries + Book×2 (Amazon offers) + Person + FAQPage + WebSite
- New definition strip after hero (visible, one-sentence series answer AI can lift)
- New FAQ section before email capture: 6 parent questions, accordion, mirrors schema text exactly, routes to quiz
- Design untouched otherwise — all existing tokens/classes reused

## quiz.html (was broken — showResults/renderQuestion/questions all missing)
- Complete engine built: 12 scenario questions, 3 per category (connection/awareness/influence/conflict), teen+parent stems, 0–3 scoring
- Results: profile tier (4), animated score bar, top-3 gap cards with REAL chapter names per book
- Book routing: conflict = weakest gap → War Playbook primary CTA; else Social Playbook primary; other book secondary link
- Email gate fixed: preventDefault + fetch POST to Brevo (was navigating away, results never showed)
- Share caption per path, retake switches teen↔parent
- Added: canonical, OG, JSON-LD (WebPage + Quiz + Breadcrumb)

## New root files
- robots.txt (all crawlers allowed + sitemap ref)
- sitemap.xml (/, /quiz.html)
- llms.txt (series map for AI engines)

## Verified
- Both JSON-LD blocks parse
- Quiz JS: node --check pass; scoring math: 36 max, 9/category
- Backups in repo working copy: index.html.bak, quiz.html.bak

## Post-deploy (5 min)
1. Rich results test: search.google.com/test/rich-results on both URLs
2. Submit sitemap in Google Search Console + Bing Webmaster
3. Run quiz end-to-end once on mobile (gate → results → CTA)
