#!/usr/bin/env python
"""Repeatable on-page SEO gate for Old Wisdom Retold static articles."""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen


class AuditParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title: list[str] = []
        self.headings: list[tuple[int, str]] = []
        self.metas: list[dict[str, str]] = []
        self.links: list[dict[str, str]] = []
        self.images: list[dict[str, str]] = []
        self.ids: set[str] = set()
        self.visible: list[str] = []
        self.jsonld: list[str] = []
        self._capture: str | None = None
        self._buffer: list[str] = []
        self._ignored_depth = 0
        self._jsonld_active = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value or "" for key, value in attrs}
        if data.get("id"):
            self.ids.add(data["id"])
        if tag in {"style", "script"}:
            self._ignored_depth += 1
        if tag == "script" and data.get("type") == "application/ld+json":
            self._jsonld_active = True
            self._buffer = []
        elif tag in {"title", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self._capture = tag
            self._buffer = []
        elif tag == "meta":
            self.metas.append(data)
        elif tag == "a":
            self.links.append(data)
        elif tag == "img":
            self.images.append(data)

    def handle_data(self, data: str) -> None:
        if self._jsonld_active:
            self._buffer.append(data)
        elif self._capture:
            self._buffer.append(data)
        if not self._ignored_depth and data.strip():
            self.visible.append(data.strip())

    def handle_endtag(self, tag: str) -> None:
        if self._jsonld_active and tag == "script":
            self.jsonld.append("".join(self._buffer).strip())
            self._jsonld_active = False
            self._buffer = []
        elif self._capture == tag:
            text = " ".join("".join(self._buffer).split())
            if tag == "title":
                self.title.append(text)
            else:
                self.headings.append((int(tag[1]), text))
            self._capture = None
            self._buffer = []
        if tag in {"style", "script"} and self._ignored_depth:
            self._ignored_depth -= 1


def load_source(source: str) -> tuple[str, str]:
    if source.startswith(("http://", "https://")):
        request = Request(source, headers={"User-Agent": "OWR-SEO-QA/1.0"})
        with urlopen(request, timeout=30) as response:
            if response.status != 200:
                raise RuntimeError(f"HTTP status {response.status}")
            return response.read().decode("utf-8"), response.geturl()
    path = Path(source)
    return path.read_text(encoding="utf-8"), str(path.resolve())


def first_meta(metas: list[dict[str, str]], key: str, value: str) -> str:
    for meta in metas:
        if meta.get(key, "").lower() == value.lower():
            return meta.get("content", "").strip()
    return ""


def run(source: str, canonical_expected: str, keyword: str) -> int:
    html, resolved_source = load_source(source)
    parser = AuditParser()
    parser.feed(html)
    passes: list[str] = []
    failures: list[str] = []

    def check(label: str, condition: bool, detail: str) -> None:
        (passes if condition else failures).append(f"{label}: {detail}")

    title = parser.title[0] if len(parser.title) == 1 else ""
    description = first_meta(parser.metas, "name", "description")
    robots = first_meta(parser.metas, "name", "robots").lower()
    canonical_match = re.findall(r'<link\b[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', html, re.I)
    canonical = canonical_match[0] if len(canonical_match) == 1 else ""
    og_url = first_meta(parser.metas, "property", "og:url")
    og_image = first_meta(parser.metas, "property", "og:image")
    og_alt = first_meta(parser.metas, "property", "og:image:alt")
    h1s = [text for level, text in parser.headings if level == 1]
    h2s = [text for level, text in parser.headings if level == 2]
    visible_text = " ".join(parser.visible)
    words = re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)?", visible_text)

    check("TITLE_COUNT", len(parser.title) == 1, f"found {len(parser.title)}")
    check("TITLE_LENGTH", 50 <= len(title) <= 60, f"{len(title)} chars — {title}")
    check("META_DESCRIPTION", 150 <= len(description) <= 160, f"{len(description)} chars")
    check("ROBOTS", "index" in robots and "follow" in robots and "noindex" not in robots, robots or "missing")
    check("CANONICAL", canonical == canonical_expected and not canonical.endswith(".html"), canonical or "missing")
    check("OG_URL", og_url == canonical, og_url or "missing")
    check("OG_IMAGE", bool(og_image and og_alt), f"image={bool(og_image)} alt={bool(og_alt)}")
    check("H1_COUNT", len(h1s) == 1, f"found {len(h1s)}")
    check("H2_COVERAGE", len(h2s) >= 3, f"found {len(h2s)}")
    levels = [level for level, _ in parser.headings]
    no_skips = all(current <= previous + 1 for previous, current in zip(levels, levels[1:]))
    check("HEADING_ORDER", no_skips, "no skipped heading levels" if no_skips else str(levels))
    check("CONTENT_DEPTH", 700 <= len(words) <= 2500, f"{len(words)} visible words")

    keyword_tokens = [token.lower() for token in re.findall(r"[A-Za-z]+", keyword)]
    first_words = " ".join(words[:200]).lower()
    search_zone = " ".join([title, description, " ".join(h1s), first_words]).lower()
    missing_tokens = [token for token in keyword_tokens if token not in search_zone]
    check("KEYWORD_PLACEMENT", not missing_tokens, "all tokens present" if not missing_tokens else f"missing {missing_tokens}")

    internal = {link.get("href", "").split("#")[0] for link in parser.links if link.get("href") and not link["href"].startswith(("http://", "https://", "mailto:", "#"))}
    canonical_host = urlparse(canonical_expected).netloc
    external = [link.get("href", "") for link in parser.links if link.get("href", "").startswith(("http://", "https://")) and urlparse(link["href"]).netloc != canonical_host]
    check("INTERNAL_LINKS", len(internal) >= 2, f"{len(internal)} unique internal destinations")
    check("AUTHORITY_LINK", len(external) >= 1, f"{len(external)} external authority links")

    image_issues = []
    for image in parser.images:
        if not image.get("alt") or not image.get("width") or not image.get("height"):
            image_issues.append(image.get("src", "unnamed"))
        if Path(image.get("src", "")).suffix.lower() not in {".webp", ".avif"}:
            image_issues.append(f"non-modern:{image.get('src', '')}")
    check("IMAGES", bool(parser.images) and not image_issues, "optimized" if not image_issues else ", ".join(image_issues))
    hero = next((image for image in parser.images if "hero-image" in image.get("class", "")), {})
    check("HERO_PRIORITY", hero.get("fetchpriority") == "high" and hero.get("decoding") == "async", str(hero))

    schema_docs: list[dict] = []
    try:
        for raw in parser.jsonld:
            doc = json.loads(raw)
            schema_docs.extend(doc if isinstance(doc, list) else [doc])
    except json.JSONDecodeError as exc:
        failures.append(f"SCHEMA_PARSE: {exc}")
    article = next((doc for doc in schema_docs if doc.get("@type") in {"Article", "BlogPosting"}), {})
    required = {"headline", "description", "author", "publisher", "mainEntityOfPage", "image", "datePublished", "dateModified", "inLanguage", "articleSection", "keywords", "timeRequired", "wordCount"}
    missing_schema = sorted(required - set(article))
    check("ARTICLE_SCHEMA", bool(article) and not missing_schema, "complete" if not missing_schema else f"missing {missing_schema}")
    check("SCHEMA_CANONICAL", article.get("mainEntityOfPage") == canonical, str(article.get("mainEntityOfPage", "missing")))
    check("AUTHOR_ENTITY", "author" in parser.ids and "Eric Han" in visible_text, "visible author entity")
    check("VISIBLE_PUBLICATION", bool(re.search(r"By Eric Han\s*·\s*5 August 2026\s*·\s*6 min read", visible_text)), "author/date/read time")

    print(f"SEO_QA source={resolved_source}")
    print(f"keyword={keyword!r} score={len(passes)}/{len(passes) + len(failures)}")
    for item in passes:
        print(f"PASS {item}")
    for item in failures:
        print(f"FAIL {item}")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="HTML file path or live URL")
    parser.add_argument("--canonical", required=True)
    parser.add_argument("--keyword", required=True)
    args = parser.parse_args()
    return run(args.source, args.canonical, args.keyword)


if __name__ == "__main__":
    sys.exit(main())
