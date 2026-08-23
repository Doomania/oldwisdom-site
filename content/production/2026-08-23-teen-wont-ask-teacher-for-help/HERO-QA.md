# Hero QA — Teen Won’t Ask the Teacher for Help

**Status:** `PASS_FOR_RELEASE_APPROVAL`  
**Model:** GPT Image 2, full generation  
**Public action:** None

## Visual gates

| Gate | Result |
|---|---|
| Emotional match | PASS — teen is visibly stuck between an assignment and an unfinished teacher email |
| Parent role | PASS — concerned, nearby, and visibly not taking over |
| Email-contact cue | PASS — recognisable recipient/subject/body/send structure without readable text |
| Tone | PASS — serious ordinary uncertainty; not cheerful, melodramatic, or staged as a tutoring success |
| Anatomy and realism | PASS — no malformed hands, faces, furniture, laptop, or paper |
| Text/logo/watermark | PASS — none readable or present |
| Full hero | PASS — 1536×1024 WebP; metadata exact |
| Responsive variants | PASS — 800×533 and 480×320 WebP |
| Social crop | PASS — 1200×630 WebP; both faces, assignment, and email-compose cue retained |
| Alt text | PASS — literal and emotionally accurate |

## QA history

- First generation rejected because its laptop screen did not communicate teacher-contact hesitation and social dimensions were absent from metadata.
- Replacement regenerated in full with a clear text-free compose interface.
- Social dimensions added to `PUBLISH.json`.
- Direct visual inspection and independent replacement re-QA both passed.

**Verdict:** PASS for final release approval. No build, publication, Pinterest, or email action is authorised by this QA record.
