# ARTICLE-QA.md
**Bundle:** `2026-08-15-guide-without-power-struggle`  
**Status:** READY_FOR_ERIC_DRAFT_REVIEW

## OWR QA Result
**Verdict:** SHIP for Eric draft review

### Checks passed
- Plain, non-diagnostic household language; Flesch-Kincaid grade **5.6**.
- 1,456 words; 10.8 words per sentence; longest prose paragraph 49 words.
- RESET → NOTICE → INVITE → RETURN is explicit, with practical scripts for chores, homework, friendship, curfew, screen time, and routines.
- Authority remains clear: choices sit inside boundaries; safety is not negotiated.
- Three reader-facing sources are linked: NIMH (support threshold), Raising Children Network (communication), and Beyers, Soenens & Vansteenkiste (2024 autonomy review).
- `git diff --check` passes.

### Independent QA repairs applied
1. Replaced the broad unsupported escalation list with a narrow immediate-danger instruction and linked NIMH support guidance.
2. Added clickable, reader-verifiable sources and narrowed the autonomy claim to the cited review’s scope.
3. Rewrote every major teaching block as short paragraphs, bullets, or scenario scripts.

### Release boundary
- [x] QA passed for Eric draft review
- [x] Eric draft approval
- [ ] Final publication approval
- [ ] Build, deploy, and distribution package

*This bundle remains draft-only. No site, social, or email publication has occurred.*
