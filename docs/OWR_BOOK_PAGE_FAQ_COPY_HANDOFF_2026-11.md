# Book-page FAQs — release record

**Status:** LIVE — independently QA'd and verified on both book pages 2026-11-07 22:56 NZDT (Eric: “yea apply”; release commit `8d7c1c5e585b7ed7f14aa0b0e44fc6daf3202cb3`).
**Scope:** H5 in `docs/OWR_HERMES_ACTION_PLAN_2026-11.md`. Approved copy is applied to the existing War and Discipline book pages; the Playbooks themselves are unchanged.
**Reader job:** Answer a parent's buyer question in plain language, without turning age suitability or a habit method into a promise. Each first answer sentence stays under 300 characters.

## The War Playbook

**Placement:** FAQ on `/books/the-war-playbook`, near the existing real excerpt and purchase choice.

**Question:** Is The Art of War OK for a 12-year-old?

**First answer sentence:** There is no blanket yes for a 12-year-old: the original *Art of War* is a military text, while Eric Han's War Playbook adapts its ideas for teen choices about composure, boundaries and avoiding needless fights.

**Detail:** This is Eric Han's modern adaptation for everyday pressure and conflict, not a copy of the original. Its public Chapter 1 excerpt, “Don't Fight Blind,” starts with an uncertain accusation in a message and shows a teen asking what was actually said before reacting. Read the excerpt together and judge the language and examples against *your* 12-year-old's maturity and interests; no single age recommendation fits every reader. For threats or a serious safety concern, seek adult help rather than asking a child to handle it with a book.

**Next action (existing destination):** Read the real Chapter 1 excerpt at `/books/the-war-playbook#sample` before deciding whether to buy.

## The Discipline Playbook

**Placement:** FAQ on `/books/the-discipline-playbook`, near the existing real excerpt and purchase choice.

**Question:** What does Stoicism have to do with my teen's habits?

**First answer sentence:** Here it means looking at what your teen can choose next, not calling them lazy when a plan slips; The Discipline Playbook turns that idea into one small first action and a rough time to try it.

**Detail:** The book draws on Marcus Aurelius and Epictetus alongside practical habit research; it does not claim an ancient quote proves a modern method. In the public Chapter 1 excerpt, “The Promise Nobody Heard,” Tane makes a detailed plan only in his head while standing at the dishwasher. The selected passages then turn to naming one first action and a rough time; the full chapter's exercise also asks who or what will notice. A missed day can invite a different plan, not a character judgment. A parent can offer the excerpt, while the teen decides whether to use it; adjust expectations for access, workload or additional support needs.

**Next action (existing destination):** Read the real Chapter 1 excerpt at `/books/the-discipline-playbook#sample` before deciding whether to buy.

## Source and approval checks

- Live War and Discipline book pages returned HTTP 200 on 2026-11-07 NZDT; both have a public `#sample` section. Book descriptions, situations, Chapter 1 titles and excerpts match `content/books.json`.
- Checked chapter headings and relevant passages against `D:/Claude/Projects/owr-content-engine/01_BOOKS/war_playbook/The_War_Playbook_KDP_v5_final.docx` (chapters “Don't Fight Blind,” “Smart Rebels Read the Rulebook,” “Aim at the Issue, Not the Ego,” “Make Yes Easy”) and `C:/Users/wen12/Downloads/The_Discipline_Playbook_KDP.docx` (Chapter 1 and sources notes). This handoff does not claim a separate age rating or tested outcome.
- Independent editorial QA passed on the revised handoff before Eric's separate page-change approval. Approval extends to these two FAQs, not H4 or other channels.
- Live verification: `https://oldwisdomretold.com/books/the-war-playbook` and `https://oldwisdomretold.com/books/the-discipline-playbook` both returned HTTP 200 with FAQ sections matching the released local HTML and live `#sample` anchors. Both FAQs passed 390px mobile render checks without horizontal overflow. A post-approval factual correction to the Discipline sample description was independently rechecked before release.
