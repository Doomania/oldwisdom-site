# Article QA — What to Say After Your Teen Fails a Test

**Status:** `QA_ACCEPTED`
**Decision:** Accepted for publication and the approved five-pin Pinterest release. Eric authorised article publication, full pin generation, and scheduling across the next ten days on 2026-09-21.

## Pre-QA gate record

| Gate | Current result |
|---|---|
| Reader job | PASS — response after an already-received poor test result |
| First-screen usefulness | PASS — first sentence and FEEL → FACTS → ONE CHANGE appear before the long explanation |
| Portfolio distinctness | PASS — differs from general ownership handoff, homework monitoring, and TRY → ASK → NEXT |
| One-off result lane | PASS |
| Repeated/subject-wide pattern lane | PASS |
| Access/learning-support lane | PASS |
| Wellbeing and urgent-safety boundary | PASS — NIMH threshold and action linked in the reader-facing paragraph |
| Mind-reading/diagnosis | PASS — observable wording; one result does not establish a condition |
| Evidence boundaries | PASS — causal limits and editorial devices disclosed |
| Product bridge | PASS — War Playbook Chapter 29, soft, optional, after complete answer |
| Publication status | PASS — schema v2, status draft, no live fields or media |
| Automated bundle validation | PASS — `PASS: Publishing Bundles are valid.` |
| OWR analyzer | REVIEWED — 6/9; plain language, research background, scannability, scripts, jargon allowance, and parent readability passed |
| Readability | PASS — FK grade 6.4; 10.8 words/sentence; 3.8% complex words |
| In-memory renderer | PASS — no marker/H1/raw Markdown leakage; headings, quotes, lists, and five source links rendered |

## Generic-checker interpretation rule

The analyzer’s three reported failures are generic-pattern mismatches, not scoped defects:

- **Concrete examples:** its quota requires 10 keywords from a fixed list dominated by chores, screens, pets, rooms, and social situations. This focused test-result guide contains paper, rubric, recall, formula, timed-section, and marking examples that the script does not count.
- **Framework intact:** its hard-coded gate requires RESET → NOTICE → INVITE, while this approved brief requires a distinct mechanism. FEEL → FACTS → ONE CHANGE is present in order.
- **Emotional-truth aligned:** its check is only a ratio of five “controlling” keywords to five “permissive” keywords. The draft balances warmth, standards, teen choice, and adult-held access/safety duties without inserting unrelated keyword language.

True failures in readability, safety, mechanism order, ownership, or source boundaries remain defects.

## QA state

**ACCEPTED.** Independent release review confirmed:

- all evidence links resolve and the article preserves claim boundaries;
- wellbeing escalation language is proportionate and points to qualified support;
- readability remains FK grade 6.4 with practical scripts and scannable action steps;
- schema-v2 bundle validation passes;
- generated HTML contains the canonical URL, Article JSON-LD, hero `srcset`, social image metadata, mechanism, source links, and no raw Markdown or stale tracking token;
- hero visual accurately shows disappointment plus calm parental concern without a cheerful mismatch;
- five Pinterest assets passed individual text/artifact review and batch contact-sheet review;
- Pinterest metadata passes title, description, hashtag, aspect-ratio, hash, disclosure, and UTM checks.

Verification command: `python scripts/site.py check && python scripts/site.py build` → `PASS: Publishing Bundles are valid.` and `PASS: generated 8 file(s).`
