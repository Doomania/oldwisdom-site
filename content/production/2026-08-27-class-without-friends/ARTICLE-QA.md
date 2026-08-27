# Article QA

**ARTICLE-ONLY RELEASE — Internal evidence and publication QA record. Pinterest and email remain held pending separate approval.**

## Draft identity

- **Title:** What to Do When Your Teen Has No Friends in Their Class
- **Audience:** Busy parents of teens.
- **Distinct reader job:** Decide whether and how to request school support or a possible class change after a teen is separated from friends.
- **Required mechanism present:** **Pause → Map → Try → Escalate**.
- **Word count:** 1,482 whitespace-delimited words; measured directly from `ARTICLE.md` on 27 August 2026.

## Scope lock

| Required boundary | QA result |
| --- | --- |
| Not a general friendship-maintenance guide | PASS — does not teach the second-conversation/shared-loop method; the friendship-fade guide is linked only for that separate job. |
| Not a school-transfer guide | PASS — focuses on class support and asks what support is possible; no transfer process is offered. |
| Not a diagnosis | PASS — no clinical label, screening claim, or treatment claim. |
| Does not promise belonging from a class change | PASS — explicitly says a move does not promise belonging or a particular outcome. |
| Preserves parent authority and immediate safety escalation | PASS — parents may bypass the seven-day plan for safety, mistreatment, or a clear barrier; immediate danger instruction is globally actionable. |

## Mechanism and usability check

| Requirement | QA result |
| --- | --- |
| First screen has a usable line | PASS — opening script: “I can see this class change feels rough. Before I contact school, can you walk me through what the day is actually like for you?” |
| Pause uses a calm observable conversation, not a placement-demand email | PASS — dedicated Pause section with an observation-first script and avoid list. |
| Map uses the teen’s own account | PASS — covers known peers, seating, lunch/breaks, partner work, teacher fit, concrete access/learning barriers, and safety. |
| Try is a teen-owned seven-school-day plan | PASS — includes one predictable contact point, one classroom move, and end-of-week review. |
| Escalate threshold is concrete | PASS — covers access/learning/safety barrier, sustained distress or functional impact, peer mistreatment, and support need. |
| Parent email requests possible support without directing a placement result | PASS — template asks “what support may be possible” and requests the school’s view. |
| Scannability | PASS — short sections, tables, bullets, and scripts. |

## SEO metadata

- **SEO title:** Teen Has No Friends in Class: What to Do
- **URL slug:** `class-without-friends`
- **Meta description:** A practical parent plan for when your teen has no friends in their class: listen, map the barrier, try one low-pressure step, and know when to involve school.
- **Primary search intent:** Parent decision support after a teen is separated from friends in class.
- **Rendered metadata and live-URL checks remain required before release completion.**

## Source and link checks

| Check | Result | Evidence / limitation |
| --- | --- | --- |
| CDC source link and definition | PASS | Directly inspected 27 August 2026. ARTICLE states the CDC definition and uses cautious association language. |
| 2024 peer-relationship transition paper | PASS | Directly inspected 27 August 2026. ARTICLE limits use to transition variability and the possibility that some students gain friendships/social standing; it does not predict individual outcomes. |
| AAP / HealthyChildren transition link | PASS WITH LIMIT | Publisher and page title were directly inspected; the available tool did not retrieve the article body. ARTICLE uses it as a labelled practical-context link only and attributes no material factual or clinical claim to it. |
| NIMH persistent-distress/function threshold and accommodation context | PASS | Directly inspected 27 August 2026. ARTICLE links NIMH beside the retained threshold and limits it to a support conversation, not a diagnosis, placement demand, or global legal entitlement. |
| WHO immediate-danger / crisis route | PASS | Directly inspected 27 August 2026. ARTICLE links WHO at the exact immediate-danger sentence; WHO directs people to call emergency services if life is in danger and to country-specific crisis support. |
| Only permitted OWR internal links | PASS | ARTICLE links only to `/articles/why-teen-friendships-fade-after-one-term` and `/articles/quiet-or-lonely-teen`. |
| Immediate-danger wording | PASS | ARTICLE says: “contact local emergency services or a crisis service immediately.” |
| Unsupported clinical or placement claims | PASS | Claim ledger identifies avoided claims and controls in `SOURCES.md`. |

## Plain-language gate

PASS. Household language used: “what the day is actually like,” “what happens at lunch,” “what got easier,” and “what support may be possible.” Specialist terms are avoided or explained. “School connectedness” is defined immediately and tied to the CDC source.

## Initial editorial-gate record

PASS. The initial editorial review used only `ARTICLE.md`, `SOURCES.md`, and this file; no public action occurred before Eric's explicit article-release approval on 27 August 2026.

## Self-audit

- I checked the produced ARTICLE against every requested mechanism component and scope boundary.
- I checked the five external URLs directly to the extent retrievable and recorded the AAP retrieval limit rather than treating it as full support. NIMH and WHO supply claim-level support for the functional-impact and immediate-danger passages revised after independent QA.
- I checked the two permitted internal-link paths against the request and included no other OWR internal links.
- I checked that the source ledger labels material claims as evidence-aligned guidance, official service info, editorial synthesis, or editorial ownership/escalation rule.
- I checked distinctness from the existing friendship-fade guide: this draft is a parent school-support decision path, not a teen friendship-maintenance mechanism.
- No clinical review is claimed. Native validation, build, SEO QA, staging review, deployment, and live verification remain required release gates.

## Verdict

**RELEASE_IN_PROGRESS** — A focused independent editorial recheck passed. Direct WHO and NIMH links support the immediate-danger and functional-impact/accommodation passages at claim level; the remaining school-contact safety rule is accurately labelled editorial. The AAP source remains practical context only because full-body retrieval was unavailable during inspection. Native pre-deploy validation passed: targeted and repository-wide bundle checks, native build, SEO QA **20/20**, local HTTP checks, and visual review of the responsive hero derivative. Live verification remains required.

**ARTICLE RELEASE APPROVED — Eric approved the article-only release in Telegram on 27 August 2026. Pinterest and email remain held pending separate approval.**
