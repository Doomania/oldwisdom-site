# GEO + Conversion rework — commit to Doomania/oldwisdom-site (root)

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
