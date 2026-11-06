<!-- AUDIENCE: PARENT · FOR: Hermes (content creator) · OWNER: Eric Han -->

# Hermes Action Plan — Parent Hub, Nov 2026 to Jan 2027

**Version:** 1.0 · 2 Nov 2026
**Applies to:** new Parent Guides in `content/production/` and copy handoffs for site pages
**Status:** active once Eric approves this file

## 0. Authority and scope

When documents disagree, use this order:

1. `OWR_Parent_Gateway_Hermes_Execution_Manual_v4.md` decides doctrine (SEE → UNDERSTAND → REFLECT → GUIDE → RELEASE), the QA scorecard and the territories.
2. `docs/OWR_OPERATING_WORKFLOW.md` decides files, folders, status values, approvals and cleanup.
3. This plan decides **what to write next, in what order, and in what shape**.

**Hermes does:** topic intake, `CONTENT-CARD.yaml`, `ARTICLE.md`, `SOURCES.md`, `PUBLISH.json`, `ARTICLE-QA.md`, `RELEASE.json`, hero briefs, and copy handoffs for pages Hermes cannot edit.

**Hermes does not:** edit HTML, templates, schema, `sitemap.xml`, `llms.txt`, `scripts/` or book pages; write anything teen-facing; put promotional files (pins, Shorts, email) in a site bundle; open a second guide before the first is closed or held at a named gate.

---

## 1. The goal in one line

Every new guide solves the parent's half of a real moment tonight, then offers the teen's half: one Playbook chapter the teen can choose.

**Primary measure:** clicks from a guide to a book page (`/books/the-<id>-playbook#sample`) per guide reader.
**Secondary:** quiz starts and email signups from guides.
**Not a measure:** guides published. Volume without distribution is the failure mode Eric has named.

## 2. What changes from today

| Before (Aug–Oct) | From now |
| --- | --- |
| Any useful parent topic | Only topics where a Playbook covers the teen's side of the same moment |
| Book mention usually `none` | `book_relevance: relevant` with a named situation or chapter, passing v4 §16 |
| Book link, when present, goes to the homepage grid (`/#series`) | Link goes to the matching book page excerpt |
| 27 of 40 guides at the GUIDE stage | More UNDERSTAND and REFLECT pieces |
| Mostly sons, nuclear families | Daughters, stepparents, multi-generational homes and second-language parents in examples |
| Titles sometimes doctrine-flavoured | Titles in the parent's own words; never "war" in a parent-facing title |
| 9 live guides fail the title-length check | `seo_title` is 30–40 characters (section 6.4) |

---

## 3. Action plan

Tick each box in `RELEASE.json` evidence or the weekly report, not in this file.

### Week 1 · 2–8 Nov

- [ ] **H1. Preflight.** Read this plan, v4, the operating workflow, `docs/OWR_CONTENT_REGISTER.md` and `automation/content-queue.md`. Confirm no overlap with topic seeds S1 and S2 (section 5.1).
- [ ] **H2. Open bundle S1** `content/production/2026-11-DD-phone-takes-whole-evening/`. Fill `CONTENT-CARD.yaml` from seed S1, then `PUBLISH.json` with `status: draft`. Run `python scripts/site.py check content/production/<bundle>`.
- [ ] **H3. Research S1.** Write `SOURCES.md` before `ARTICLE.md`. Every claim gets "claim-safe use" and "limit" lines.
- [ ] **H4. Copy handoff: gift page.** Draft the copy for "Books for Teens Who Don't Like Reading" (section 5.3). Deliver it to Eric for review; it is not a bundle. Due **9 Nov**, because Christmas shipping cut-offs fall in late November.
- [ ] **H5. Copy handoff: book page FAQ answers.** "Is The Art of War OK for a 12-year-old?" for the War page; "What does Stoicism have to do with my teen's habits?" for the Discipline page. 300 characters or fewer for the first answer sentence; detail after.
- [ ] **H6. Report only: title-length fixes.** List the 9 live guides whose rendered title falls outside 50–60 characters, each with a proposed `seo_title`. Change nothing until Eric approves.

### Week 2 · 9–15 Nov

- [ ] **H7. Draft S1** `ARTICLE.md` to the skeleton in section 6.3. Run the persona check (section 4.4) and record it in `CONTENT-CARD.yaml`.
- [ ] **H8. QA S1** in `ARTICLE-QA.md`: v4 score of 16 or higher, SEO thresholds (section 6.4), bridge check (section 4.5). Set `status: review` and present for the `article` approval.
- [ ] **H9. Hero brief S1** in `HERO-BRIEF.md` (follow the existing brief format; no legible text in the scene).
- [ ] **H10.** After S1 is approved or held at a named gate, open **bundle S2**. Repeat H2–H3.

### Week 3 · 16–22 Nov

- [ ] **H11. Release S1** after `article` approval, following workflow step 4.
- [ ] **H12. Draft, QA and present S2.**
- [ ] **H13. Copy handoff: Discipline cluster intro.** One paragraph plus an ordered list: S1, S2, `stop-reminding-homework`, `task-start-runway`, `reliability-signal`. A developer places it on Parent Hub.

### Week 4 · 23–29 Nov

- [ ] **H14. Release S2** after approval.
- [ ] **H15. Decision table for Eric.** For S1, S2 and the three guides that already link to a book page (`help-teen-start-conversation-without-making-it-weird`, `stand-up-without-fighting`, `stop-reminding-homework`): readers, book-page clicks and click rate. If no analytics collector exists yet, report "no data" and stop; do not estimate.
- [ ] **Gate:** if the new guides match or beat the old bridged guides → continue to December. If they fall below, rework the teen's-half section before writing more.

### December

- [ ] S3 (teacher is unfair) and S4 (comparing themselves online), one at a time.
- [ ] **By 10 Dec, copy handoff:** "Summer holidays without screens all day" (backlog B1), for NZ and AU readers whose school year ends mid-December.

### January

- [ ] **First week:** "Starting a new school: the first two weeks" (backlog B2), ahead of NZ and AU term 1 in late January to early February.
- [ ] S5 (alpha influencers).
- [ ] S6 (online manipulators) **only after** the safety gate in section 6.7 is signed off.
- [ ] Copy handoff: "Lead, don't manage" start-here block for Parent Hub.

---

## 4. Planning guide

### 4.1 Six gates every topic must pass

1. **Book-adjacent.** The teen's side of this moment is a situation or chapter in a live Playbook (anchor table, section 4.5). No anchor means it is not a priority topic, although it may still be a useful guide later.
2. **A real moment.** You can write the parent's question as a first-person prompt of six words or more, typed at 11pm. Collect real wording from Search Console, Pinterest search suggestions or public forums, and put it in `search_language_patterns`.
3. **No overlap.** Check the register, the queue and each live guide's `portfolio_boundary`. One guide does one job.
4. **Persona check passes** (section 4.4).
5. **A values line fits:** strength without cruelty, confidence without arrogance, influence without manipulation, or discipline without self-hatred.
6. **Risk class known.** Standard, or high-stakes (sexual exploitation, self-harm, abuse, legal exposure). High-stakes topics need the safety gate in section 6.7.

### 4.2 Priority score

| Factor | Points |
| --- | --- |
| Book bridge: direct anchor / soft / none | +2 / +1 / 0 |
| Persona panel mean of 3.5 or higher | +1 |
| Real parent wording or query data attached | +1 |
| Fills a thin cluster (War or Discipline, or the UNDERSTAND stage) | +1 |
| Time-bound with a real date (term start, holidays, exams, Christmas) | +1 |
| High-stakes risk class | −1, plus the safety gate |

Highest score ships first. On a tie: Discipline, then War, then Social, until each book has at least 8 guides.

### 4.3 Cadence

- One guide open at a time (workflow rule).
- Two new guides in November, then the week-4 gate decides the pace.
- After the gate, aim for one guide a week. Refresh one older guide a month instead of writing a new one when a live guide fails the title or bridge rules.

### 4.4 Persona panel check

The eight parents below are **constructed**, not real. Each one's main worry comes from a published figure (sources in section 8). Use the panel to catch objections before Eric does, not as evidence of demand.

| ID | Parent | Teen | Main worry | Rejects |
| --- | --- | --- | --- | --- |
| P1 | US mum, two working parents | Daughter, 13 | Anxiety, phones, nightly arguments | "War" wording; blame |
| P2 | US single dad, raised strictly, parenting differently | Son, 15 | Standing up without fighting | Vague gentle-parenting; sneering at masculinity |
| P3 | UK mum, part-time work | Son, 13; won't read | Online misogyny; reading | Panic; long reads |
| P4 | AU dad on shifts, Stoic-curious | Daughter, 16, Year 11 | Exam stress, the future | Soft abstraction |
| P5 | NZ Chinese-heritage parents, English as a second language | Son, 12; quiet | Grades; social confidence | Slang, idioms, anything that dismisses study |
| P6 | NZ Samoan-heritage mum, three generations at home | Daughter, 16; part-time job, minds siblings | Respect, family, online safety | Individualism that ignores family duty; cost |
| P7 | Canadian stepmum, Indian-Canadian, blended family | Stepson, 14 | Influence without authority | Advice that assumes she sets the rules |
| P8 | US dad, works from home | Son, 13; ADHD | Starting tasks; being called lazy | Willpower talk; shame |

**How to run it:**

1. Score each parent 1–5 on one question: *would I click this at 11pm and read to the end?*
2. For every score of 2 or lower, write the objection in one line.
3. Fix the title, the examples or the framing, then re-score.
4. Go ahead only if the mean is 3.3 or higher and no more than two parents score 2 after fixes.
5. Record the scores and fixes in `CONTENT-CARD.yaml` under `persona_check`.

### 4.5 Book bridge rules and anchors

**The rule:** the teen's half is offered, never assigned. One short closing section, after the parent's half is complete, links to the book page excerpt. The guide must be fully useful without it.

**PUBLISH.json settings:**

- `book_relevance`: `{"status": "relevant", "id": "<social|war|discipline>", "reason": "<the teen's half of this moment, in one sentence>"}`
- `next_step`: use `kind: "guide"` with a real `target`, not `kind: "playbook"`. The renderer currently sends `playbook` next steps to the homepage grid (`/#series`), which loses the reader.
- **Until the platform fix in section 7 ships:** put the book link inside `ARTICLE.md` as the final section, using a root-relative Markdown link, for example `[Read the Discipline Playbook excerpt](/books/the-discipline-playbook#sample)`. Inline links are not click-tracked yet.

**Anchors Hermes may cite.** Situations come from the live book pages; chapter names come from the build configs and **must be checked against the published edition before quoting**.

| Playbook | Situations (live book page) | Chapters (confirm before quoting) |
| --- | --- | --- |
| Discipline (`discipline`) | The assignment is open but you still haven't started · A phone or video keeps taking the whole evening · You missed a day and feel like giving up the whole plan | Ch 1 "The Promise Nobody Heard"; sources: Marcus Aurelius, Epictetus, Franklin |
| War (`war`) | A vague accusation in a group chat makes you want to fire back · Someone keeps pushing a boundary · Choosing whether to answer, repair, leave or get help | "Don't Fight Blind", "The Trigger Map", "The Cost Meter", "Noise Is Not Power", "Smart Rebels Read the Rulebook", "Win Without Fighting", "Rage Is a Terrible General", "Aim at the Issue, Not the Ego", "Make Yes Easy", "Give Them an Exit", "Tiny Wins Stack Into Power", "Your Advantage Is Where You Stopped Comparing"; Part Five "Read People and Protect Position" |
| Social (`social`) | Speaking up without performing a different personality · A joke or criticism has made a conversation harder · Stronger friendships and a better way to disagree | "Don't Kick the Beehive", "The Magnetic Field" (be genuinely interested), "The Rizz Patch" (first impression), "The Name Tag Hack", "The FYP Hack" (talk in their interests), "The Self-Report Power Move" (admit when you're wrong), "The POV Switch" |

---

## 5. Topic examples

### 5.1 Priority slate: seeds for `CONTENT-CARD.yaml`

Copy a seed into a new card, then complete every field the existing card format requires (for example `possible_parent_impact`, `short_term_goal`, `pin_hooks`). `territory` is the v4 §11 test territory; `canonical_publish_territory` is the `PUBLISH.json` value.

#### S1 · Phone eats the whole evening (start here)

```yaml
slug: phone-takes-whole-evening
article_title: "When the Phone Takes the Whole Evening: Help Your Teen Take It Back Without Confiscating It"
seo_title: "Teen on Phone All Evening? What Works"          # 37 chars
territory: "<fill from v4 §11>"
canonical_publish_territory: confidence
stage: GUIDE
supports_stages: [REFLECT, RELEASE]
test_angle: LONG_TERM_CAPABILITY
teen_outcomes: [capability, ownership]
parent_observation: "Every evening the phone comes out after dinner and homework, chores and sleep slide. The parent ends up arguing or confiscating."
automatic_parent_interpretation: "If I don't take the phone, nothing will change."
possible_teen_perspective: "The teen may want the evening back too but has no plan for the first ten minutes after dinner, or uses the phone to decompress."
core_belief_shift:
  from: "If I don't take the phone away every night, nothing will change."
  to: "A plan for the first 30 minutes after dinner that my teen designs, and that we review once a week, can do more than nightly confiscation."
practical_parent_move: "Agree the evening start together; parent keeps shared-space and sleep rules and follows them too."
boundary_or_authority_note: "Sleep, safety and shared family rules stay with the adult. Re-enter if sleep or school attendance drops."
ownership_transfer: "Teen designs and runs the evening start and reviews it weekly."
book_relevance: DIRECT
teen_half: "Discipline Playbook — situation: 'A phone or video keeps taking the whole evening.'"
values_line: "Discipline without self-hatred."
search_language_patterns:
  - "teenager on phone all evening what to do"
  - "how to get my teen off their phone without fighting"
  - "should I take my teenager's phone at night"
evidence_required:
  - "About 4 in 10 parents and teens argue regularly about phone time (Pew 2024)."
  - "46% of teens say a parent is at least sometimes distracted by their own phone (Pew 2024)."
  - "Find a sleep-and-screens source (paediatric body) before claiming any sleep effect."
internal_link_to: [task-start-runway, should-i-check-my-teens-phone]
next_step: {kind: guide, target: task-start-runway}
portfolio_boundary: "Not a phone-monitoring guide (see should-i-check-my-teens-phone). Its single job is to hand the evening plan to the teen."
persona_watch: "P8 needs an ADHD note; P6 needs shared devices and shared rooms; P5 needs study time framed as the goal."
risk_class: standard
```

#### S2 · Restarting after a missed day

```yaml
slug: teen-gives-up-after-missed-day
article_title: "When One Missed Day Turns Into 'I Give Up': Teach Your Teen to Restart"
seo_title: "Teen Gives Up After a Missed Day?"              # 33 chars
canonical_publish_territory: confidence
stage: REFLECT
supports_stages: [GUIDE, RELEASE]
test_angle: REFLECT
teen_outcomes: [judgment, ownership, independence]
automatic_parent_interpretation: "Missing a day proves he isn't serious."
core_belief_shift:
  from: "When my teen misses one day, it proves they were never serious about the habit."
  to: "The skill worth building is the restart, and my reaction to the lapse decides whether my teen tries again."
practical_parent_move: "Ask one neutral question after a lapse instead of giving a verdict; the teen chooses a restart rule."
book_relevance: DIRECT
teen_half: "Discipline Playbook — situation: 'You missed a day and feel like giving up the whole plan.'"
values_line: "Discipline without self-hatred."
search_language_patterns:
  - "my son gives up on everything after one mistake"
  - "teenager all or nothing thinking habits"
  - "how to help teen stick with something"
evidence_required:
  - "VERIFY before citing: Lally et al. (2010), European Journal of Social Psychology, on missed days during habit formation."
internal_link_to: [reliability-signal, stop-reminding-homework]
next_step: {kind: guide, target: reliability-signal}
persona_watch: "Use sport training and game streaks as examples so P2 and P3 recognise their sons; P8 needs 'skill, not character'."
risk_class: standard
```

#### S3 · Teen says a teacher is unfair

```yaml
slug: teen-says-teacher-unfair
article_title: "Your Teen Says a Teacher Is Unfair: Help Them Raise It Respectfully"
seo_title: "Teen Says a Teacher Is Unfair?"                 # 30 chars
canonical_publish_territory: conflict
stage: GUIDE
supports_stages: [RELEASE]
test_angle: LONG_TERM_CAPABILITY
teen_outcomes: [judgment, capability, independence]
core_belief_shift:
  from: "If a teacher is being unfair to my teen, I need to step in and fix it myself."
  to: "My teen can check the rule, gather the facts and ask in a way that makes yes easy; I step in for safety, discrimination, or when the routine route fails."
boundary_or_authority_note: "Parent re-enters for safety, discrimination, a pattern after a fair attempt, or a formal complaint."
book_relevance: DIRECT
teen_half: "War Playbook — 'Smart Rebels Read the Rulebook', 'Make Yes Easy', 'Aim at the Issue, Not the Ego' (confirm titles)."
values_line: "Strength without cruelty."
internal_link_to: [teen-wont-ask-teacher-for-help, guide-teen-without-power-struggle]
next_step: {kind: guide, target: teen-wont-ask-teacher-for-help}
portfolio_boundary: "Not a routine help-asking guide (see teen-wont-ask-teacher-for-help). This one is about a perceived unfairness."
persona_watch: "'Respectfully' in the title keeps P5, who expects respect for teachers. P8's ADHD teen often clashes with rules."
risk_class: standard
```

#### S4 · Comparing themselves online

```yaml
slug: teen-compares-self-online
article_title: "When Your Teen Compares Themselves to Everyone Online"
seo_title: "Teen Comparing Themselves Online?"              # 33 chars
canonical_publish_territory: confidence
stage: UNDERSTAND
supports_stages: [GUIDE]
test_angle: SEE
teen_outcomes: [judgment, ownership]
core_belief_shift:
  from: "If I keep telling my daughter she is great, the comparing will stop."
  to: "Reassurance alone rarely holds; helping my teen choose what they measure themselves on does more."
book_relevance: DIRECT
teen_half: "War Playbook — 'Your Advantage Is Where You Stopped Comparing' (confirm title)."
values_line: "Confidence without arrogance."
evidence_required:
  - "Social media is the most-cited concern of Australian parents of 12–18s, at 59% (ReachOut 2024)."
  - "Find a peer-reviewed source on social comparison and adolescent wellbeing."
internal_link_to: [signs-of-real-teen-confidence, quiet-kids-and-confidence]
next_step: {kind: guide, target: signs-of-real-teen-confidence}
persona_watch: "Lead with a daughter (P1 lane, the hub has few); add boys' versions (gym, game rank). Name body image and eating concerns as a reason to get professional help."
risk_class: standard
```

#### S5 · Son watching "alpha" influencers

```yaml
slug: son-watching-alpha-influencers
article_title: "Your Son Is Watching 'Alpha' Influencers: What to Say Instead of Banning Them"
seo_title: "Son Watching Alpha Influencers?"                # 31 chars
canonical_publish_territory: influence
stage: UNDERSTAND
supports_stages: [REFLECT, GUIDE]
test_angle: REFLECT
teen_outcomes: [judgment, ownership]
core_belief_shift:
  from: "My son is being radicalised by these videos and I have to shut it down now."
  to: "My son is looking for a map of how to be strong; I can offer a better one and keep him talking."
book_relevance: DIRECT
teen_half: "War Playbook — 'Noise Is Not Power'; series rule: strength without cruelty, no alpha dominance language."
values_line: "Strength without cruelty."
evidence_required:
  - "33.2% of US boys aged 13–17 followed Andrew Tate at least a little (Scharrer, Ward & Volling, Psychology of Men & Masculinities; cite the journal article, not the news write-up)."
internal_link_to: [guide-teen-without-power-struggle, helpful-advice-sounds-like-criticism]
next_step: {kind: guide, target: guide-teen-without-power-struggle}
persona_watch: "P2 leaves if it sneers at wanting to be strong. Keep to behaviour and values; no claims about named people beyond the cited study."
risk_class: standard (politically charged; keep it evenhanded)
```

#### S6 · How manipulators hook teens online (high-stakes)

```yaml
slug: how-manipulators-target-teens-online
article_title: "How Manipulators Hook Teenagers Online: A Cybersecurity Dad's Field Guide"
seo_title: "How Manipulators Target Teens Online"           # 36 chars
canonical_publish_territory: reading
stage: SEE
supports_stages: [GUIDE]
test_angle: SEE
teen_outcomes: [judgment, independence]
core_belief_shift:
  from: "If I monitor everything on my teen's phone, I will catch any danger in time."
  to: "A teen who knows the pressure patterns (urgency, secrecy, flattery, isolation) and knows they won't be shamed for asking is better placed to spot what monitoring misses."
ownership_transfer: "Parent keeps a no-shame reporting promise and the emergency steps; teen owns spotting the pattern."
book_relevance: DIRECT
teen_half: "War Playbook Part Five 'Read People and Protect Position'; the Social Playbook's Empathy Test separates influence from manipulation."
values_line: "Influence without manipulation."
evidence_required:
  - "FBI: 13,000+ reports of financial sextortion of minors, at least 12,600 victims, mostly boys 14–17, Oct 2021–Mar 2023 (FBI Sacramento, Jan 2024)."
  - "Netsafe: 21% of NZ adults were personally targeted by sextortion or know someone who was (Netsafe, Oct 2025)."
  - "VERIFY each reporting route when drafting: US (FBI tips; NCMEC), UK (CEOP; Report Remove), AU (eSafety Commissioner), NZ (Netsafe)."
internal_link_to: [should-i-check-my-teens-phone, ai-fake-nude-response]
next_step: {kind: guide, target: should-i-check-my-teens-phone}
persona_watch: "P1 and P3 need a calm opening, not fear."
risk_class: high-stakes — safety gate in section 6.7 before review
```

### 5.2 Backlog examples

Run each through the gates (section 4.1) and the score (section 4.2) before opening a bundle.

| # | Working title | Parent moment | Stage | Teen's half | Panel lanes | Timing |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | Summer Holidays Without Screens All Day | "School's out for six weeks and he'll be on the console from noon." | GUIDE | Discipline: phone and evening situation | P5, P6, P8 | Publish by 10 Dec (NZ/AU) |
| B2 | Starting a New School: The First Two Weeks | "My daughter starts at a new high school in February and knows nobody." | GUIDE | Social: "The Rizz Patch", "The Name Tag Hack" | P5, P6, P7 | First week of Jan |
| B3 | "I'll Do It Later": When Your Teen Puts Everything Off | "Every night he says later, and later never comes." | UNDERSTAND | Discipline Ch 1 "The Promise Nobody Heard" | P5, P8 | Any |
| B4 | Your Teen Wants to Quit After One Bad Week | "She wants to quit netball after one bad game." | REFLECT | Discipline restart; War "Tiny Wins Stack Into Power" | P2, P4 | Start of a sport season |
| B5 | Sibling Fights: Let Them Settle It Without You Refereeing | "Every evening I'm the judge between my 15- and 12-year-old." | GUIDE | War "Give Them an Exit", "Win Without Fighting" | P6, P7 | Any |
| B6 | When Your Teen Is Pressured to Join In on Teasing | "His friends are mocking a kid and he went along with it." | GUIDE | War Part Five; Social "Don't Kick the Beehive" | P1, P2 | Any |
| B7 | Why Some Teens Avoid Conflict Until They Explode | already in `content-queue.md` | REFLECT | War "Rage Is a Terrible General", "The Trigger Map" | P2, P8 | Any |
| B8 | What a Teen Can Say When a Group Chat Turns on Them | already in `content-queue.md` | GUIDE | War "Don't Fight Blind" (live excerpt) | P1, P3 | Any |
| B9 | Exam Weeks Without Taking Over | "Exams in two weeks and he hasn't opened a book." | GUIDE | Discipline (control what you can); War "Confidence Is Preparation…" | P4, P5 | Before mid-year exams |
| B10 | When Your Teen Never Admits They're Wrong | "She'll argue for an hour rather than say sorry." | REFLECT | Social "The Self-Report Power Move" | P2, P7 | Check overlap with `teen-apologize-without-writing-it` |
| B11 | Stepparent? How to Lead Without Being the Rule-Maker | "I'm not his mum, so every rule I set starts a fight." | REFLECT | None (book_relevance none) | P7 | Any |
| B12 | When Grandparents and Parents Set Different Rules | "Grandma lets her stay up; I don't." | UNDERSTAND | None | P5, P6 | Any |

### 5.3 Copy handoffs (Hermes writes, a developer places)

| Item | Where it goes | Brief |
| --- | --- | --- |
| Gift page | `/books/books-for-teens-who-dont-like-reading` | How to choose a book a reluctant reader finishes; the three Playbooks, each with "fits / doesn't fit"; 4–6 books by other authors **that Eric has actually read** (Eric supplies the list); a plain line saying Eric wrote three of them. Hook: UK reading enjoyment among 8–18s is 32.7%, a 20-year low (National Literacy Trust 2025). No invented praise or reviews. |
| War page FAQ | `/books/the-war-playbook` | "Is The Art of War OK for a 12-year-old?" Answer first: what the book teaches (composure, boundaries, choosing which fights not to enter) and what it does not (violence, domination). |
| Discipline page FAQ | `/books/the-discipline-playbook` | "What does Stoicism have to do with my teen's habits?" Plain English: control what you can, restart after a lapse. |
| Discipline cluster intro | Parent Hub | One paragraph plus the ordered guide list (task H13). |
| Start-here block | `/parents/` | "Lead, don't manage" in one screen: managing means carrying the teen's tasks; leading means setting conditions, modelling and handing decisions back. For P5 and P6 it must read as leading with authority, not giving it up. Then one first guide per book. |

---

## 6. Structure guides

### 6.1 Bundle layout

Follow `docs/OWR_OPERATING_WORKFLOW.md` exactly. Per guide:

```text
content/production/<YYYY-MM-DD>-<slug>/
  CONTENT-CARD.yaml   # planning card (intake), filled before any writing
  SOURCES.md          # claim-level evidence, written before ARTICLE.md
  ARTICLE.md          # editorial source
  PUBLISH.json        # renderer contract, schema_version 2
  ARTICLE-QA.md       # v4 score, SEO, bridge, persona and safety checks
  RELEASE.json        # article / pinterest / email truth
  HERO-BRIEF.md       # optional until the article is approved
  media/              # hero, responsive variants, social image only
```

Pins, Shorts, YouTube scripts and email live in `oldwisdomretold-social\article_pins\<bundle>\`, never in the site bundle.

### 6.2 New `CONTENT-CARD.yaml` fields

Keep every existing field. Add these four:

```yaml
teen_half: "<Playbook> — <situation or confirmed chapter title>"
values_line: "<one line from the series moral rule>"
persona_check:
  scores: {P1: 0, P2: 0, P3: 0, P4: 0, P5: 0, P6: 0, P7: 0, P8: 0}
  objections: ["<P# — one-line objection — fix applied>"]
  mean: 0.0
risk_class: standard | high-stakes
```

### 6.3 `ARTICLE.md` skeleton

Target 1,100–1,600 words (the SEO gate allows 700–2,500).

```markdown
<!-- AUDIENCE: PARENT -->

# <article_title>

<Opening, 2–3 short paragraphs. Sentence 1 answers the reader's question
directly. Name the moment in concrete detail, the automatic interpretation
in italics, then the belief shift in italics. Put the search phrase in the
first 200 words.>

<One line naming the method, in bold, e.g. **Ownership Handoff**:
what the parent owns, what the teen owns.>

## <Parent question as a heading: "What is actually going on?">
<UNDERSTAND content: possible teen perspectives, without deciding which.
One named source.>

## <The method, as a heading>
### 1. <What the parent owns>
### 2. <What the teen owns>
### 3. <How you review it, weekly and briefly>

## What to say
<One short script for tonight.>
> "<Exact words, plain English, no idioms.>"

## When to step back in
<Three re-entry thresholds: safety, a pattern after a fair attempt, a
skill or access problem. Name ADHD, anxiety or other needs as reasons to
adjust, and say when to get professional support.>

## The bottom line
<Three sentences maximum. Repeat the shift. Include the values line.>

## Your teen's half
<Two or three sentences: the teen can practise the same moment from their
side. Offer it; do not assign it. One root-relative link:
[Read the <Title> Playbook excerpt](/books/the-<id>-playbook#sample)>
```

Heading rules: the title is the only H1; at least three H2s; no skipped levels (H2 then H3); headings phrased the way a parent would ask.

The renderer supports `##`–`######` headings, `-` and `1.` lists, `>` quotes, `**bold**`, `*italic*`, and `[text](https://…)` or `[text](/path)` links. Nothing else renders, so no tables, images or HTML inside `ARTICLE.md`.

### 6.4 Titles and metadata

| Field | Rule | Why |
| --- | --- | --- |
| `title` (H1) | The situation in the parent's words; colon plus promise allowed | Shown on page and in Parent Hub |
| `seo_title` | **30–40 characters** | The site appends " \| Old Wisdom Retold" (20 characters); the SEO gate wants 50–60 in total |
| `seo_description` | **150–160 characters**; includes the search phrase | SEO gate |
| `summary` | One sentence; used in Article schema and `llms.txt` | Must stand alone as an answer |
| `slug` | lowercase kebab-case, 3–6 words, search words first | Validator |
| Search phrase | Every token appears in the title, description, H1 or first 200 words | `KEYWORD_PLACEMENT` check |
| Links | 2 or more internal guide links and 1 or more external authority links | `INTERNAL_LINKS`, `AUTHORITY_LINK` |
| Pronouns | Neutral ("your teen", "they") unless the topic is specific to sons or daughters | Half of parents read "him" as not for them |
| Banned in titles | "war", doctrine words (Release, capability, ownership), slang, gaming vocabulary | Parent register; firewall |

### 6.5 `PUBLISH.json` template

The validator rejects missing fields, wrong values and short strings (`release_move` and each `core_belief_shift` line need 20+ characters; `qa_score` is an integer from 16 to 20).

```json
{
  "schema_version": 2,
  "status": "draft",
  "audience": "parent",
  "slug": "phone-takes-whole-evening",
  "title": "When the Phone Takes the Whole Evening: Help Your Teen Take It Back Without Confiscating It",
  "summary": "<one-sentence answer>",
  "seo_title": "Teen on Phone All Evening? What Works",
  "seo_description": "<150–160 characters with the search phrase>",
  "journey_stage": "GUIDE",
  "supports_stages": ["REFLECT", "RELEASE"],
  "teen_outcomes": ["capability", "ownership"],
  "release_move": "<what the parent keeps; what the teen carries>",
  "qa_score": 16,
  "territory": "confidence",
  "v4_test_territory": "<v4 §11 territory>",
  "test_angle": "LONG_TERM_CAPABILITY",
  "core_belief_shift": {"from": "<20+ chars>", "to": "<20+ chars>"},
  "book_relevance": {
    "status": "relevant",
    "id": "discipline",
    "reason": "The Discipline Playbook gives the teen their own side of the same evening: taking back a night the phone keeps taking."
  },
  "next_step": {
    "kind": "guide",
    "target": "task-start-runway",
    "label": "Help your teen start tomorrow's work",
    "reason": "Use this next once the evening has a start."
  }
}
```

Allowed values: `journey_stage` and `supports_stages` SEE, UNDERSTAND, REFLECT, GUIDE, RELEASE · `teen_outcomes` judgment, capability, ownership, independence · `territory` connection, reading, influence, conflict, confidence · `test_angle` SEE, REFLECT, LONG_TERM_CAPABILITY · `next_step.kind` guide, reflection, quiz, download, playbook, none · `status` draft, review, published. Add `published`, `hero` and `social_image` at release, following existing bundles.

### 6.6 `SOURCES.md` format

```markdown
# Sources and Claim Audit

**Research date:** YYYY-MM-DD
**Status:** `DRAFT_RESEARCHED`

## Sources

1. **<Author/organisation> (<year>), "<title>."**
   <URL>
   **Claim-safe use:** <the exact claim the guide may make, with the number>
   **Limit:** <what this source cannot support>
```

Primary sources over news write-ups. Every number in the article appears here with its limit. Label the article's own method as "OWR editorial synthesis, not a validated intervention".

### 6.7 Voice, safety and QA

**Voice:**

- Calm older brother or dad. Direct, specific, respectful of parent and teen.
- Parent register only: no Cheat Code, Side Quest, Noob Move, gaming vocabulary or teen slang.
- Plain English: short sentences, no idioms, for parents reading in a second language.
- Examples include family duties (sibling care, part-time work, grandparents at home), daughters as well as sons, and blended families.
- No fear, no guaranteed outcomes, no diagnosis, no invented testimonials or statistics.

**Safety gate** (high-stakes topics; S6 now):

- Show no method detail that could help an offender.
- Victims are supported, never shamed; the no-shame promise is explicit.
- Follow suicide-safe messaging: no link to suicide in the title, summary or opening; include crisis lines for each country.
- Verify each reporting route on its official site on the drafting date and record it in `SOURCES.md`.
- Eric signs off in `ARTICLE-QA.md` before `status: review`.

**`ARTICLE-QA.md` must show:**

1. `python scripts/site.py check content/production/<bundle>` → PASS
2. v4 scorecard, 10 dimensions, score of 16 or higher, no hard fails
3. SEO rules from section 6.4 checked by hand before build; after release run `python scripts/seo_article_qa.py articles/<slug>.html --canonical 'https://oldwisdomretold.com/articles/<slug>' --keyword '<phrase>'`
4. Bridge check: guide fully useful without the book; teen's half offered, not assigned; correct `book_relevance.id`; link goes to `#sample`
5. Persona check: mean of 3.3 or higher and objections fixed
6. Safety gate signed off (high-stakes only)

---

## 7. Platform dependencies (not Hermes: Eric or a developer)

| # | Issue found in the repo | Fix | Why it matters |
| --- | --- | --- | --- |
| P1 | `destination()` in `scripts/site.py` sends `next_step.kind: playbook` to `/#series`; `book_sample_companion()` is hard-coded to 3 slugs | Link `playbook` next steps to `/books/the-<id>-playbook#sample`; render the "A tool your teen can choose" block from `book_relevance` for any relevant guide; add `data-event="sample_opened"` | Bridges reach the matching book, and clicks are counted |
| P2 | No analytics collector installed | Connect one (site audit, week 1) | The week-4 gate needs click data |
| P3 | 9 live guides render titles outside 50–60 characters | Approve Hermes's `seo_title` list (task H6) | SEO gate and search snippets |
| P4 | Gift page, book page FAQs, Discipline cluster and start-here block need template or page edits | Implement Hermes's copy handoffs | Hermes cannot edit pages |

Once P1 ships, Hermes stops adding the inline book link and uses the renderer block instead.

---

## 8. Sources behind the numbers in this plan

- [Parenting in America Today](https://www.pewresearch.org/social-trends/2023/01/24/parenting-in-america-today/), Pew Research Center, Jan 2023 (P1, P2, P5)
- [How Teens and Parents Approach Screen Time](https://www.benton.org/headlines/how-teens-and-parents-approach-screen-time), Pew Research Center via Benton Institute, Mar 2024 (S1, P1)
- [Children and young people's reading in 2025](https://literacytrust.org.uk/research-services/research-reports/children-and-young-peoples-reading-in-2025), National Literacy Trust, Jun 2025 (gift page, P3)
- ["Parents feel out of their depth"](https://bps.org.uk/news/parents-feel-out-their-depth-and-dealing-something-outside-their-knowledge-and-control), British Psychological Society, Apr 2025 (P3)
- [What parents and carers worry about](https://about.au.reachout.com/blog/new-research-on-what-parents-and-carers-worry-about-by-reachout), ReachOut Australia, Apr 2024 (S4, P4)
- [Auckland 2023 Census summary](https://knowledgeauckland.org.nz/media/rfvp03sv/auckland-2023-census-summary.pdf), Knowledge Auckland (P5, P6)
- [Pacific housing report coverage](https://www.1news.co.nz/2023/01/18/40-of-pasifika-living-in-home-not-big-enough-for-family), 1News reporting Stats NZ, Jan 2023 (P6)
- [Children in stepfamilies, 2021 Census](https://www150.statcan.gc.ca/n1/daily-quotidien/220713/g-a008-eng.htm), Statistics Canada (P7)
- [ADHD data](https://cdc.gov/adhd/data), US CDC (P8)
- [One in three teen boys follows Andrew Tate at least a little](https://www.psypost.org/one-in-three-teen-boys-follows-andrew-tate-at-least-a-little-and-those-who-do-hold-more-rigid-views-of-manhood/), PsyPost, Oct 2026, reporting Scharrer, Ward and Volling (S5)
- [Sextortion: a growing threat preying upon our nation's teens](https://www.fbi.gov/contact-us/field-offices/sacramento/news/sextortion-a-growing-threat-preying-upon-our-nations-teens), FBI Sacramento, Jan 2024 (S6)
- [Netsafe Sextortion Report](https://resource.netsafe.org.nz/Netsafe-Sextortion-Report-October-2025.pdf), Netsafe, Oct 2025 (S6)
- Repo: `docs/OWR_OPERATING_WORKFLOW.md`, `scripts/site.py`, `scripts/seo_article_qa.py`, `content/books.json`, existing bundles (commit 8abf511)
