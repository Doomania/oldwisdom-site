# H6 — live guide title-length report (2026-11-07 NZDT)

**Status:** LIVE — all seven rendered titles verified 2026-11-07 22:56 NZDT (Eric: “yea apply”; release commit `8d7c1c5e585b7ed7f14aa0b0e44fc6daf3202cb3`). The approved action plan anticipated nine out-of-range guides; the live inventory had **seven**. No slug or on-page H1 was changed.

**Method:** Fetch `https://oldwisdomretold.com/sitemap.xml`, filter `/articles/`, retrieve all 43 guide URLs (43/43 HTTP 200), decode each rendered `<title>`, and count characters. Target: rendered title 50–60 characters, including ` | Old Wisdom Retold`. The approved `seo_title` values below are 30–40 characters and retain every existing canonical slug; lengths were computed by script. The source metadata edits were built and live-verified.

| Canonical article slug | Previous rendered title length | Live `seo_title` | Field length | Live rendered length |
| --- | ---: | --- | ---: | ---: |
| `argument-stop-or-communication-improve` | 65 | Teen Arguments: Stop or Talk Better? | 36 | 56 |
| `leave-group-drama-safely` | 67 | Help Your Teen Leave Group Drama | 32 | 52 |
| `let-him-handle-it-badly` | 62 | Let Your Teen Handle a Small Mistake | 36 | 56 |
| `quiet-or-lonely-teen` | 72 | Quiet or Lonely Teen? How to Tell | 33 | 53 |
| `teen-driving-curfew-trust-ladder` | 61 | Teen Driving Curfew: Build Trust | 32 | 52 |
| `who-owns-waking-up` | 67 | Who Owns Waking Up? A Teen Handoff | 34 | 54 |
| `why-is-my-teen-avoiding-me` | 62 | Why Is My Teen Suddenly Avoiding Me? | 36 | 56 |

**Approval scope:** Eric's “yea apply” authorised these seven `seo_title` changes and the two H5 FAQ placements, not H4, Pinterest, or email. Independent QA and live verification completed before closing the release. H4 gift-page handoff remains skipped.

**Release verification:** All seven canonical article URLs returned HTTP 200; live `<title>` values exactly matched the generated output (52–56 characters) and canonical links remained in place. Generated article diffs changed only `<title>`; independent review found H1 and description unchanged. Publisher bundle check, generated-output check and nine unit tests passed. The legacy article SEO script still reports unrelated pre-existing metadata/authority/depth deficits; this H6 release was deliberately title-only.
