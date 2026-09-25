# Old Wisdom Retold — Eric feedback

## Pinterest creative

- Every Pinterest image must include exactly one visible, context-matched CTA. `SAVE THIS SCRIPT`, `READ THE GUIDE`, `TRY THIS TONIGHT`, or another clear action may be used according to the Pin’s purpose; “save” is not mandatory. Missing CTA is a QA failure.
- Before creating OWR Pins, load and follow the proven static-Pin design system in `D:\Claude\Projects\owr-content-engine\07_DOCS\HERMES_PIN_TEST_QUIET_TEEN_CONFIDENCE_20260802.md`, plus `00_MEMORY\CONTENT_STRATEGY.md` and `00_MEMORY\CTA_RULES.md`.
- Preserve its core design rules: clean editorial utility card, Poppins/Lora hierarchy, OWR neutrals with electric-blue accent, 90 px safe margin, no decorative clutter, one CTA only, keyword-first title, and genuine composition variation. Do not add a logo/brand mark unless an active parent-guide Pin brief explicitly specifies the approved asset and placement.
- GPT‑Image‑2 only, full generation with typography integrated; no composites or fallback model.
- Visual QA must explicitly transcribe and verify the CTA, not only headline/body copy and branding.
- Character-led Pinterest scenes must not show forms, worksheets, open documents, notebooks with text, phone screens, calendars, or other legible in-scene surfaces. Generated perspective makes them appear upright to the viewer but upside down for characters; use non-text props and place all required copy only in the designed overlay.
- Across any future character-led Pinterest batch, deliberately balance race/ethnicity and family representation. Do not default to one race; record the intended mix in the creative manifest before generation.

## Repository workflow

- **Single source of truth:** all OWR blogs, Pinterest pins, rules, and guidelines live in ONE repo only: D:\Claude\Projects\oldwisdom-site (remote: Doomania/oldwisdom-site).
- **Never use git worktrees or standalone clones for OWR updates.** 2026-09-26 cleanup removed 12 worktrees + 4 clones (~1.8 GB duplicate disk).
- Push/pull to origin from the single checkout. Do not re-clone or copy the repo for a blog, campaign, QA run, or release.
- Follow docs/OWR_OPERATING_WORKFLOW.md (single-checkout workflow) for every guide lifecycle.
