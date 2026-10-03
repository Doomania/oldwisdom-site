# Old Wisdom Retold — Eric feedback

## Pinterest creative
- Video Pins must use the matching `thumbnail_shot_<name>.png` as the **uploaded video cover**, not an automatically selected frame, with cover readback before scheduling. Keep MP4 unchanged. Verify title, description, and related topic tags against Pinterest content rules (accurate, non-spammy, relevant, truthful AI disclosure) and provider card before recording success; do not fabricate progress.

- Every Pinterest image must include exactly one visible, context-matched CTA. `SAVE THIS SCRIPT`, `READ THE GUIDE`, `TRY THIS TONIGHT`, or another clear action may be used according to the Pin’s purpose; “save” is not mandatory. Missing CTA is a QA failure.
- 2026-10-01: Eric rejected the four-guide refresh as technically correct but not parent-scroll-worthy. Before showing a batch, judge it as a busy mum: does the hook stop her, and does the image alone give a concrete line, decision, or mini-tool worth saving/forwarding? If not, redesign the full generation (not minor styling). Vary formats across the batch and keep scheduling separate from visual approval. The old `BRIEF.md` no-CTA instruction is superseded for this revision.
- Before creating OWR Pins, load and follow the proven static-Pin design system in `D:\Claude\Projects\owr-content-engine\07_DOCS\HERMES_PIN_TEST_QUIET_TEEN_CONFIDENCE_20260802.md`, plus `00_MEMORY\CONTENT_STRATEGY.md` and `00_MEMORY\CTA_RULES.md`.
- Preserve its core design rules: clean editorial utility card, Poppins/Lora hierarchy, OWR neutrals with electric-blue accent, 90 px safe margin, no decorative clutter, one CTA only, keyword-first title, and genuine composition variation. Do not add a logo/brand mark unless an active parent-guide Pin brief explicitly specifies the approved asset and placement.
- GPT‑Image‑2 only, full generation with typography integrated; no composites or fallback model.
- Visual QA must explicitly transcribe and verify the CTA, not only headline/body copy and branding.
- Character-led Pinterest scenes must not show forms, worksheets, open documents, notebooks with text, phone screens, calendars, or other legible in-scene surfaces. Generated perspective makes them appear upright to the viewer but upside down for characters; use non-text props and place all required copy only in the designed overlay.
- Across any future character-led Pinterest batch, deliberately balance race/ethnicity and family representation. Do not default to one race; record the intended mix in the creative manifest before generation.

## Repository workflow

- **Repository boundary:** `D:\Claude\Projects\oldwisdom-site` holds only live-site files: website source, article bundles (`ARTICLE.md`, `SOURCES.md`, `PUBLISH.json`, `RELEASE.json`, QA, hero media), rendered site assets and release records. ALL promotional content — Pinterest copy (`PINTEREST.md`), Shorts/YouTube scripts, emails, pin images, queues, QA, audits and Pinterest scripts — lives in `D:\Claude\Projects\oldwisdomretold-social\` (per article: `article_pins\<bundle>\`). 2026-10-03: the site build no longer requires `PINTEREST.md`.
- **No duplicate site checkouts:** never clone, worktree, or copy `oldwisdom-site` for an article, campaign, QA run, or release.
- Push/pull to origin from the single checkout. Do not re-clone or copy the repo for a blog, campaign, QA run, or release.
- Follow docs/OWR_OPERATING_WORKFLOW.md (single-checkout workflow) for every guide lifecycle.
- Housekeeping is mandatory: inspect the existing canonical structure before writes; use no speculative work folders; remove temporary test/download/render artifacts immediately after verification; report—not silently delete—ambiguous legacy material.
- Preserve live integrity: every article URL, Pinterest destination/card record, and social permalink stays recorded in the bundle `RELEASE.json` and generated `docs/OWR_CONTENT_REGISTER.md`. Tidy-up never changes public destinations.
- Weekly project audits are report-only and should use the cheapest configured capable model; report stale outputs, duplicate/untracked structures, and record gaps before any cleanup.