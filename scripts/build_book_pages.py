"""Build the three public book pages from reviewed content/books.json."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build():
    books = json.loads((ROOT / 'content/books.json').read_text(encoding='utf-8'))
    for book in books:
        slug = book['slug']
        url = f'https://oldwisdomretold.com/books/the-{slug}-playbook'
        title = f"The {slug.title()} Playbook"
        e = html.escape
        schema = {'@context': 'https://schema.org', '@graph': [
            {'@type': 'Book', '@id': url + '#book', 'name': title,
             'author': {'@type': 'Person', 'name': 'Eric Han', 'url': 'https://oldwisdomretold.com/#author'},
             'url': url, 'sameAs': book['amazon'], 'inLanguage': 'en',
             'description': book['description'], 'image': 'https://oldwisdomretold.com/assets/' + book['cover'],
             'isPartOf': {'@type': 'BookSeries', 'name': 'Old Wisdom Retold', 'url': 'https://oldwisdomretold.com/#series'}},
            {'@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://oldwisdomretold.com/'},
                {'@type': 'ListItem', 'position': 2, 'name': title, 'item': url}]}]}
        situations = ''.join(f'<li>{e(s)}</li>' for s in book['situations'])
        excerpt = ''.join(f'<p>{e(p)}</p>' for p in book['excerpt'])
        related = ''.join(f'<a class="button secondary" href="/books/the-{b["slug"]}-playbook">{e(b["name"])}</a>' for b in books if b['slug'] != slug)
        page = f'''<!doctype html>
<html lang="en-NZ"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} by Eric Han | {e(book['search_label'])}</title>
<meta name="description" content="{e(book['description'], quote=True)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="book"><meta property="og:title" content="{title} by Eric Han">
<meta property="og:description" content="{e(book['description'], quote=True)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="https://oldwisdomretold.com/assets/{book['cover']}">
<link rel="icon" href="/assets/favicon.svg"><link rel="stylesheet" href="/assets/book-pages.css">
<link rel="stylesheet" href="/assets/site-tools.css"><script src="/assets/site-tools.js" defer></script>
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script></head>
<body><a class="skip-link" href="#main">Skip to book</a>
<nav><a class="brand" href="/">OLD WISDOM // RETOLD</a><div><a href="/#series">All books</a><a href="/parents/">Free Parent Hub</a><a href="/quiz.html">Free quiz</a></div></nav>
<main id="main"><header class="book-hero" style="--accent:{book['accent']}">
<img src="/assets/{book['cover']}" width="825" height="1275" alt="{title} cover" fetchpriority="high">
<div><p class="eyebrow">BOOK {book['code']} · 30 STRATEGIES · FOR TEENS</p><h1>{title}</h1>
<p class="subtitle">{e(book['subtitle'])}</p><p>{e(book['description'])}</p>
<a class="button" href="{book['amazon']}" target="_blank" rel="noopener noreferrer" data-event="amazon_purchase_clicked" data-event-label="{slug} book page">GET IT ON AMAZON ↗</a>
<a class="button secondary" href="#sample" data-event="sample_opened" data-event-label="{slug}">READ A REAL EXCERPT ↓</a></div></header>
<section><p class="eyebrow">IS THIS YOUR SITUATION?</p><h2>{e(book['promise'])}</h2><ul>{situations}</ul>
<p>{e(book['fit'])}</p></section>
<section><p class="eyebrow">THE WISDOM BEHIND THE PRACTICE</p><h2>{e(book['source_heading'])}</h2><p>{e(book['source_note'])}</p>
<p>Eric Han adapts the ideas through contemporary situations and practical exercises. The excerpt below is his writing from the manuscript.</p></section>
<section id="sample" data-sample="{slug}"><p class="eyebrow">READ BEFORE YOU BUY · SELECTED EXCERPT</p><h2>{e(book['chapter'])}</h2>
<blockquote>{excerpt}</blockquote><p class="source-note">Selected passages from {title}, {e(book['chapter'])}. Gaps between selected passages are marked with […].</p>
<h3>Try the idea today</h3><p>{e(book['practice'])}</p><p class="source-note">The practice above is a website introduction to the idea. The book contains the full chapter and its exercises.</p>
<a class="button" href="{book['amazon']}" target="_blank" rel="noopener noreferrer" data-event="amazon_purchase_clicked" data-event-label="{slug} after sample">GET THE FULL PLAYBOOK ↗</a>
<a class="button secondary" href="/#capture" data-event="sample_signup_clicked" data-event-label="{slug}">GET THE SOCIAL PLAYBOOK'S CHAPTER 1 BY EMAIL</a></section>
<section class="parent-companion"><p class="eyebrow">FREE COMPANION FOR PARENTS</p><h2>{e(book['parent_heading'])}</h2>
<p>{e(book['parent_note'])} The Parent Hub is free to read, including for families who have not bought a book.</p>
<a class="button secondary" href="/articles/{book['guide']}" data-event="parent_guide_opened" data-event-label="{slug} companion">TRY THE FREE PARENT GUIDE →</a></section>
<section><h2>Choose the book that fits this week</h2>{related}<p>Each book stands on its own. Start with the situation you want to handle better.</p></section>
<section><h2>About Eric Han</h2><p>Eric Han is an Auckland-based father and cybersecurity professional. He writes practical books that connect classic ideas with the situations young people face.</p><a href="/#author">Read why Eric started the series</a></section>
</main><footer><a href="/parents/">Free Parent Hub</a> · <a href="/privacy.html">Privacy</a> · © Eric Han</footer></body></html>'''
        target = ROOT / 'books' / f'the-{slug}-playbook.html'
        target.parent.mkdir(exist_ok=True)
        target.write_text(page, encoding='utf-8')
        print(target.relative_to(ROOT))


if __name__ == '__main__':
    build()
