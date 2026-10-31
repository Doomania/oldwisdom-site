# Growth implementation — 1 November 2026

## Published scope

- Situation-led homepage with the book selector immediately after the hero and a free homework handoff companion.
- Three permanent book pages with manuscript excerpts, source explanations, purchase links, related books and free parent guides.
- Parent Hub entry by concrete situation, preserved in its generation template.
- Three guide-to-book sample invitations, preserved by the publisher.
- Quiz results available immediately after question 15. Email signup is optional and specifically offers the Social chapter.
- Sitemap and llms.txt include book URLs. Homepage Book schema points to those URLs and identifies the Amazon listings separately.

## Source provenance

Social and War excerpts come from the DOCX manuscripts in owr-content-engine/01_BOOKS. The Discipline folder supplied contained only the cover PDF. Its excerpt comes from C:/Users/wen12/Downloads/The_Discipline_Playbook_KDP.docx, whose subtitle matches the published Amazon listing. content/books.json records provenance and reviewed excerpts. scripts/build_book_pages.py regenerates the pages without needing the original manuscript files. Website practices are explicitly distinguished from manuscript passages.

## Measurement state and limitation

No analytics collector or reporting credentials were found in the site repository. No historical baseline, confirmed signup rate, order attribution or controlled A/B test can be established from site code alone.

The shared script emits anonymous interaction events to dataLayer, an owr:analytics browser event, and gtag when a configured gtag collector exists. This does not itself install or configure an analytics destination. Purchase and review clicks use distinct event names. Quiz events carry no scores, response content, email, or teen/parent path. Page paths exclude query strings.

Events verified locally include amazon_purchase_clicked, amazon_review_clicked, sample_opened, parent_guide_opened, quiz_started, quiz_completed and signup_requested. Signup requested is not confirmed subscription. An opaque no-cors Brevo request does not expose the server response, so confirmed signup must be measured in Brevo. Outbound Amazon clicks are not orders.

## Reporting access needed

Connect the owner's existing analytics destination or approved collector, Search Console property and Brevo reporting. Historical data access and Amazon order reports are needed before calculating lift. No new paid service or visitor tracking provider was installed.

## Review after rollout

Use 28 days of comparable traffic when available. Split by source, landing page and device. Measure Amazon purchase clicks per visitor, sample-to-Amazon progression, guide-to-sample progression, quiz completions and confirmed signups per quiz starter. Exclude review invitation clicks from purchase intent. Compare orders separately against available Amazon reporting.

The quiz change is a single rollout, not a randomized experiment. Treat before/after results as observational. Five first-time reader sessions can test whether four readers identify the appropriate book and one useful action within a minute. Those human sessions remain pending.

## Regeneration and verification

Run scripts/build_book_pages.py, then scripts/site.py build and scripts/site.py check --all. Browser QA must cover desktop and mobile, the full 15-question quiz through results and optional signup, sample links, and three guide companions. Do not submit invented contacts to Brevo during testing.
