# Evergreen Production Batches

The Codex automation `Old Wisdom weekly evergreen content batch` writes one
dated, topic-specific folder here each Monday.

Each batch should contain:

- `PUBLISH.json`, the machine-readable Parent Guide publishing contract;
- long-form YouTube script;
- companion article draft;
- two short-video scripts;
- five Pinterest pin titles and descriptions;
- search, thumbnail, chapter, description, and UTM metadata;
- `SOURCES.md` with source links and a claim audit.

## Publishing contract

Hermes edits the bundle, never site templates or generated output. `PUBLISH.json`
declares the title, journey stage, teen outcomes, release move, optional next
step, and publication status. A published non-legacy guide also supplies
`ARTICLE.md`, responsive hero assets, and an optional social image in `media/`.

Run `python scripts/site.py check content/production/<bundle>` before review.
After approval, run `python scripts/site.py build`; it creates the Parent Hub,
the guide page where applicable, and the managed Parent Hub entries in the
sitemap and `llms.txt`.

## Human review gate

Nothing in this directory is automatically published, uploaded, emailed,
committed, or pushed. Before publication, a person must confirm:

- the content is genuinely useful and not a shallow template variation;
- any current facts still match the linked primary sources;
- no clinical diagnosis, invented testimonial, or guaranteed result appears;
- the CTA and campaign link match the actual topic;
- the voice sounds like Old Wisdom // Retold rather than generic AI copy;
- platform formatting, visuals, captions, and accessibility are complete.

After publishing, add the live URL and date to the production log in
`automation/content-queue.md`.
