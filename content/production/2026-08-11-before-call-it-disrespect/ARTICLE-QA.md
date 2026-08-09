<!-- AUDIENCE: PARENT -->

# Day 4 Production Article — Independent QA

**Asset:** `content/production/2026-08-11-before-call-it-disrespect/ARTICLE.md`
**Audit date:** 2026-08-09
**Audience:** PARENT
**Test angle:** SEE
**Score:** **20/20 after verified resolution**
**Verdict:** **SHIP FOR HUMAN REVIEW**
**Hard fails:** **None**
**Publication:** **Human approval remains required; no publication action was taken.**

## Required fix — resolved 2026-08-09

1. **Repair the unsupported and under-operationalised escalation paragraph at ARTICLE.md line 90.**
   - The paragraph gives safety/health-adjacent guidance for threats, violence, abuse, self-harm risk, substance impairment, repeated contempt/aggression/shutdown, and family-life disruption, but it has no claim-level authoritative source.
   - Replace the vague immediate-risk instruction — `Seek appropriate professional or emergency help when risk is immediate...` — with a globally actionable line such as: **“If there is immediate danger or risk of self-harm, contact local emergency services or a crisis service immediately.”**
   - Add a direct authoritative link in that paragraph supporting the immediate-risk action. Also source the threshold that repeated aggression or shutdown disrupting family life warrants professional support, or narrow it to an explicitly labelled editorial recommendation that does not imply a clinical threshold.
   - Keep ordinary disagreement and one-off rudeness separate from danger, persistent functional disruption, or a need for assessment.

No other required fixes were found.

## 20-point OWR scorecard

| Dimension | Score | Finding |
|---|---:|---|
| A. Understanding the teen | 2/2 | Offers several possible contexts without claiming to know motive or using context as an excuse. |
| B. Parent self-reflection | 2/2 | Separates observable conduct from a character verdict and asks the parent to inspect timing, sequence, and assumptions. |
| C. Intent vs impact | 2/2 | Shows how identity labels can shift the exchange into self-defence while preserving the parent's legitimate concern. |
| D. Educational direction | 2/2 | Builds disagreement, pausing, return, repair, and completion of responsibility rather than instant submission. |
| E. Practical parent value | 2/2 | `BEFORE → BEHAVIOUR → REPAIR` is memorable, bounded, and demonstrated with usable language. |
| F. Authority balance | 2/2 | Explicitly preserves safety action, household expectations, reasonable limits, and proportionate consequences. |
| G. Teen ownership | 2/2 | The teen owns words, actions, the original responsibility, and repair; the parent does not take over the learning. |
| H. Respect / non-shaming | 2/2 | Neither parent nor teen is cast as the villain; real misconduct is named without turning it into identity. |
| I. Credibility | 1/2 | The developmental and guidance claims are carefully bounded and linked near use, but the safety/escalation paragraph is unmapped and too vague for immediate risk. |
| J. OWR distinctiveness | 2/2 | The SEE angle, behaviour-versus-label distinction, sequence mechanism, and repair ownership are recognisably OWR. |
| **Total** | **19/20** | Above the numeric threshold, but the claim-level safety defect keeps the verdict at FIX. |

## Claim and source audit

- **Van Doorn, Branje & Meeus:** **PASS.** The linked four-wave study used 314 Dutch early adolescents and both parents and measured changes in positive problem-solving, conflict engagement, and withdrawal. The article correctly labels it observational, avoids tactic-level causation, and does not use the study to explain one teen.
- **Kobak et al.:** **PASS.** The review discusses positive engagement, supervision/guidance, open communication, adolescent autonomy, safety, and communication skills. The article correctly presents it as a review and avoids promising that one repair conversation will produce disclosure or self-regulation.
- **Child Mind Institute communication guidance:** **PASS WITH ACCESS NOTE.** Current search indexing supports the article's use of listening and careful conversational timing. Direct automated retrieval returned 403, so no stronger empirical status is assigned; the article already labels it practical guidance rather than proof.
- **Child Mind Institute anger guidance:** **PASS WITH ACCESS NOTE.** Current indexing supports the bounded statement that stress can accompany teen outbursts and that less harmful expression can be coached. The draft explicitly says stress did not necessarily cause the episode or erase responsibility. Direct automated retrieval returned 403.
- **Raising Children Network:** **PASS.** Current indexing supports that disrespectful behaviour can occur in adolescence and should be handled with communication, relationships, and rules. The draft properly rejects the stronger inference that every rude exchange is harmless, typical, or temporary. Direct automated retrieval returned 403.
- **Escalation/support paragraph:** **FIX.** No source is placed at the paragraph, and `appropriate professional or emergency help` is not an operational immediate-risk instruction.

## Causal-boundary check

**PASS apart from the escalation-source defect.** The article consistently uses `can`, `may`, `might`, and `hypotheses to check`; distinguishes studies from expert guidance; and states that timing, stress, autonomy friction, or sequence review does not prove cause, reveal motive, guarantee honesty, prevent conflict, or excuse harm. The framework is presented as an observation-and-repair aid, not a diagnosis.

## Portfolio distinctiveness

**PASS.** The opening scope note explicitly separates this article from the adjacent pressure/disclosure and shutdown-script territories.

- Versus Day 2, this article does not reuse the Social Pressure Loop or `Listen → Offer → Agree`; its mechanism is one family-conflict sequence and the repair still owed.
- Versus Day 3, it does not reuse friendship count/judgment, `Notice → Name → Decide`, friend appraisal, or peer-risk guidance.
- Shared OWR elements — specific observation, non-shaming language, authority, safety, and ownership — are doctrine, not substantive duplication.

## Tone, usefulness, and human-quality checks

- **PARENT audience:** clear and consistent.
- **SEE angle:** dominant; observation is separated from interpretation before the article moves to understanding and repair.
- **Authority/ownership:** strong; empathy is never equated with permissiveness.
- **Standalone value:** strong; no product mention or forced CTA is needed for the article to be useful.
- **Practicality:** strong; the parent receives a stop-now script, a three-step review, examples of observable descriptions, repair options, and a clear division of responsibility.
- **OWR tone:** warm, direct, practical, and non-preachy.
- **AI-language scan:** no publish-blocking AI residue. The prose avoids canned signposting, significance inflation, vague expert attribution, repetitive inline-header lists, and a generic promotional ending. Repetition of “context is not permission” functions as the article's deliberate boundary rather than filler.

## Resolution verification — 2026-08-09

- Replaced vague escalation wording with: contact local emergency services or a crisis service immediately for immediate danger or self-harm risk.
- Added claim-level links to American Academy of Pediatrics self-harm guidance and Royal Children’s Hospital Melbourne teen-behaviour guidance.
- Replaced the unsupported family-disruption threshold with the RCH-supported conditions: intense, ongoing, worsening, or affecting daily life, relationships, or school.
- Explicitly excluded ordinary disagreement and one-off rudeness from that threshold.
- Updated `SOURCES.md`, reran the PARENT audience gate, bundle validation, unit suite, and diff checks: all PASS.
- Credibility is restored to 2/2; final score: **20/20**.

## Final recommendation

**SHIP FOR HUMAN REVIEW.** The safety-source defect is resolved and verified. The review bundle is complete; publication remains separately gated and unauthorised.