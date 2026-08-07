#!/usr/bin/env python
"""Build and validate Parent Hub pages from review-gated Publishing Bundles."""

from __future__ import annotations

import argparse
import html
import json
import math
import re
import sys
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


STAGES = ("SEE", "UNDERSTAND", "REFLECT", "GUIDE", "RELEASE")
OUTCOMES = ("judgment", "capability", "ownership", "independence")
NEXT_STEPS = ("guide", "reflection", "quiz", "download", "playbook", "none")
TERRITORIES = ("connection", "reading", "influence", "conflict", "confidence")
TEST_ANGLES = ("SEE", "REFLECT", "LONG_TERM_CAPABILITY")
PLAYBOOK_IDS = ("social", "war", "discipline")
STAGE_COPY = {
    "SEE": "Separate what happened from the story you are tempted to tell about it.",
    "UNDERSTAND": "Make room for context, development, and the teenager's perspective.",
    "REFLECT": "Notice how your own urgency, fear, or habits shape the moment.",
    "GUIDE": "Offer one bounded practice, prompt, or scaffold that the teen can use.",
    "RELEASE": "Return an appropriate decision or next move as capability grows.",
}


class PublicationError(ValueError):
    """A Publishing Bundle cannot safely be released."""


@dataclass(frozen=True)
class Bundle:
    path: Path
    meta: dict[str, Any]

    @property
    def slug(self) -> str:
        return self.meta["slug"]

    @property
    def published(self) -> bool:
        return self.meta["status"] == "published"


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PublicationError(f"{path}: invalid JSON ({exc})") from exc
    if not isinstance(value, dict):
        raise PublicationError(f"{path}: expected an object")
    return value


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_config(root: Path) -> dict[str, Any]:
    config = read_json(root / "config" / "site.json")
    for field in ("site_name", "base_url", "author", "language", "parent_hub_path", "parent_growth_brevo_form_action"):
        if not isinstance(config.get(field), str) or not config[field].strip():
            raise PublicationError(f"config/site.json: missing {field}")
    if not config["parent_growth_brevo_form_action"].startswith("https://"):
        raise PublicationError("config/site.json: parent_growth_brevo_form_action must use HTTPS")
    return config


def safe_path(root: Path, relative: str, source: Path) -> Path:
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise PublicationError(f"{source}: path escapes the repository: {relative}") from exc
    return candidate


def bundle_paths(root: Path) -> list[Path]:
    return sorted((root / "content" / "production").glob("**/PUBLISH.json"))


def validate_bundle(root: Path, manifest_path: Path) -> Bundle:
    meta = read_json(manifest_path)
    required = (
        "schema_version", "status", "audience", "slug", "title", "summary",
        "journey_stage", "supports_stages", "teen_outcomes", "release_move",
        "qa_score", "territory", "test_angle", "core_belief_shift", "book_relevance",
    )
    for field in required:
        if not meta.get(field):
            raise PublicationError(f"{manifest_path}: missing {field}")
    if meta["schema_version"] != 2:
        raise PublicationError(f"{manifest_path}: unsupported schema_version")
    if meta["status"] not in {"draft", "review", "published"}:
        raise PublicationError(f"{manifest_path}: status must be draft, review, or published")
    if meta["audience"] != "parent":
        raise PublicationError(f"{manifest_path}: Parent Hub entries must have audience=parent")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", meta["slug"]):
        raise PublicationError(f"{manifest_path}: slug must be lowercase kebab-case")
    if meta["journey_stage"] not in STAGES:
        raise PublicationError(f"{manifest_path}: unknown journey_stage")
    supported = meta["supports_stages"]
    if not isinstance(supported, list) or not supported or any(stage not in STAGES for stage in supported):
        raise PublicationError(f"{manifest_path}: supports_stages must use Parent Growth Journey stages")
    outcomes = meta["teen_outcomes"]
    if not isinstance(outcomes, list) or not outcomes or any(outcome not in OUTCOMES for outcome in outcomes):
        raise PublicationError(f"{manifest_path}: teen_outcomes must contain approved outcomes")
    if not isinstance(meta["release_move"], str) or len(meta["release_move"].strip()) < 20:
        raise PublicationError(f"{manifest_path}: release_move must be a useful ownership move")
    qa_score = meta["qa_score"]
    if isinstance(qa_score, bool) or not isinstance(qa_score, int) or not 16 <= qa_score <= 20:
        raise PublicationError(f"{manifest_path}: qa_score must be an integer from 16 to 20")
    if meta["territory"] not in TERRITORIES:
        raise PublicationError(f"{manifest_path}: territory must be one of {', '.join(TERRITORIES)}")
    if meta["test_angle"] not in TEST_ANGLES:
        raise PublicationError(f"{manifest_path}: test_angle must be one of {', '.join(TEST_ANGLES)}")
    belief_shift = meta["core_belief_shift"]
    if not isinstance(belief_shift, dict) or set(belief_shift) != {"from", "to"}:
        raise PublicationError(f"{manifest_path}: core_belief_shift must contain only from and to")
    if any(not isinstance(value, str) or len(value.strip()) < 20 for value in belief_shift.values()) or belief_shift["from"].strip() == belief_shift["to"].strip():
        raise PublicationError(f"{manifest_path}: core_belief_shift must name distinct, useful beliefs")
    relevance = meta["book_relevance"]
    if not isinstance(relevance, dict) or relevance.get("status") not in {"relevant", "none"}:
        raise PublicationError(f"{manifest_path}: book_relevance needs status=relevant or status=none")
    if not isinstance(relevance.get("reason"), str) or len(relevance["reason"].strip()) < 20:
        raise PublicationError(f"{manifest_path}: book_relevance needs a useful reason")
    if relevance["status"] == "relevant" and relevance.get("id") not in PLAYBOOK_IDS:
        raise PublicationError(f"{manifest_path}: relevant book_relevance needs a recognised Playbook id")
    if relevance["status"] == "none" and "id" in relevance:
        raise PublicationError(f"{manifest_path}: non-relevant book_relevance must not name a Playbook")

    next_step = meta.get("next_step", {"kind": "none"})
    if not isinstance(next_step, dict) or next_step.get("kind") not in NEXT_STEPS:
        raise PublicationError(f"{manifest_path}: invalid next_step")
    if next_step.get("kind") == "playbook" and (not next_step.get("id") or not next_step.get("reason")):
        raise PublicationError(f"{manifest_path}: Playbook next steps need id and relevance reason")
    if next_step.get("kind") == "playbook" and (relevance["status"] != "relevant" or relevance.get("id") != next_step["id"]):
        raise PublicationError(f"{manifest_path}: Playbook next step must match an explicitly relevant book_relevance")
    if next_step.get("kind") in {"guide", "reflection", "download"} and not next_step.get("target"):
        raise PublicationError(f"{manifest_path}: {next_step['kind']} next step needs target")

    bundle = Bundle(manifest_path.parent, meta)
    validate_pinterest(bundle)
    if bundle.published:
        published = meta.get("published")
        try:
            date.fromisoformat(published)
        except (TypeError, ValueError) as exc:
            raise PublicationError(f"{manifest_path}: published must be YYYY-MM-DD") from exc
        legacy = meta.get("legacy_output")
        article = bundle.path / "ARTICLE.md"
        if legacy:
            output = safe_path(root, legacy, manifest_path)
            if not output.is_file():
                raise PublicationError(f"{manifest_path}: missing legacy output {legacy}")
        elif not article.is_file():
            raise PublicationError(f"{manifest_path}: published bundles need ARTICLE.md")
        else:
            if not (bundle.path / "SOURCES.md").is_file():
                raise PublicationError(f"{manifest_path}: published bundles need SOURCES.md")
            if not (bundle.path / "PINTEREST.md").is_file():
                raise PublicationError(f"{manifest_path}: published bundles need PINTEREST.md")
            validate_media(root, bundle)
    return bundle


def validate_pinterest(bundle: Bundle) -> None:
    campaign_file = bundle.path / "PINTEREST.md"
    if not campaign_file.is_file():
        return
    content = campaign_file.read_text(encoding="utf-8")
    descriptions = re.findall(r"^- Description:\s*(.+)$", content, flags=re.MULTILINE)
    if len(re.findall(r"^## Pin\s+\d+", content, flags=re.MULTILINE)) != 5 or len(descriptions) != 5:
        raise PublicationError(f"{campaign_file}: expected five titled pins with descriptions")
    for position, description in enumerate(descriptions, start=1):
        if not all(token in description for token in ("utm_source=pinterest", "utm_medium=organic", "utm_campaign=", "utm_content=")):
            raise PublicationError(f"{campaign_file}: Pin {position} must use the stable Pinterest UTM shape")
    configured = bundle.meta.get("pinterest_campaign", {}).get("campaign")
    if configured and any(f"utm_campaign={configured}" not in description for description in descriptions):
        raise PublicationError(f"{campaign_file}: Pinterest campaign must match PUBLISH.json")


def validate_media(root: Path, bundle: Bundle) -> None:
    hero = bundle.meta.get("hero")
    if not isinstance(hero, dict):
        raise PublicationError(f"{bundle.path}: published generated guides need hero metadata")
    for field in ("source", "alt", "width", "height", "variants"):
        if not hero.get(field):
            raise PublicationError(f"{bundle.path}: hero missing {field}")
    if not isinstance(hero["variants"], list) or len(hero["variants"]) < 2:
        raise PublicationError(f"{bundle.path}: hero needs 480px and 800px variants")
    if not {item.get("width") for item in hero["variants"]}.issuperset({480, 800}):
        raise PublicationError(f"{bundle.path}: hero variants must include 480px and 800px sizes")
    for item in [hero, *hero["variants"]]:
        source = item.get("source")
        if not isinstance(source, str) or not (bundle.path / source).is_file():
            raise PublicationError(f"{bundle.path}: missing media source {source}")
    social = bundle.meta.get("social_image", hero)
    if not isinstance(social, dict) or not isinstance(social.get("source"), str):
        raise PublicationError(f"{bundle.path}: social_image is invalid")
    if not (bundle.path / social["source"]).is_file():
        raise PublicationError(f"{bundle.path}: missing social image {social['source']}")


def load_bundles(root: Path) -> list[Bundle]:
    manifests = bundle_paths(root)
    if not manifests:
        raise PublicationError("No Publishing Bundles found under content/production")
    bundles = [validate_bundle(root, path) for path in manifests]
    slugs = [bundle.slug for bundle in bundles]
    if len(slugs) != len(set(slugs)):
        raise PublicationError("Publishing Bundle slugs must be unique")
    return bundles


def inline_markdown(value: str) -> str:
    escaped = html.escape(value, quote=False)
    escaped = re.sub(
        r"\[([^\]]+)]\((https?://[^\s)]+|/[^\s)]+)\)",
        lambda match: f'<a href="{html.escape(match.group(2), quote=True)}">{match.group(1)}</a>',
        escaped,
    )
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", escaped)
    return escaped


def markdown_to_html(source: str) -> str:
    output: list[str] = []
    paragraph: list[str] = []
    lines = source.replace("\r\n", "\n").split("\n")
    index = 0

    def flush_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{inline_markdown(' '.join(part.strip() for part in paragraph))}</p>")
            paragraph.clear()

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            index += 1
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            if level > 1:
                output.append(f"<h{level}>{inline_markdown(heading.group(2))}</h{level}>")
            index += 1
            continue
        if re.match(r"^[-*]\s+", stripped):
            flush_paragraph()
            items: list[str] = []
            while index < len(lines) and re.match(r"^\s*[-*]\s+", lines[index]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[index]).strip())
                index += 1
            output.append("<ul>" + "".join(f"<li>{inline_markdown(item)}</li>" for item in items) + "</ul>")
            continue
        if re.match(r"^\d+\.\s+", stripped):
            flush_paragraph()
            items = []
            while index < len(lines) and re.match(r"^\s*\d+\.\s+", lines[index]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[index]).strip())
                index += 1
            output.append("<ol>" + "".join(f"<li>{inline_markdown(item)}</li>" for item in items) + "</ol>")
            continue
        if stripped.startswith("> "):
            flush_paragraph()
            quotes = []
            while index < len(lines) and lines[index].strip().startswith("> "):
                quotes.append(lines[index].strip()[2:])
                index += 1
            output.append(f"<blockquote><p>{inline_markdown(' '.join(quotes))}</p></blockquote>")
            continue
        paragraph.append(line)
        index += 1
    flush_paragraph()
    return "\n    ".join(output)


def render_template(root: Path, name: str, values: dict[str, str]) -> str:
    template = (root / "templates" / name).read_text(encoding="utf-8")
    for key, value in values.items():
        template = template.replace("{{" + key + "}}", value)
    unresolved = re.findall(r"{{[a-z_]+}}", template)
    if unresolved:
        raise PublicationError(f"{name}: unresolved placeholders {', '.join(unresolved)}")
    return template


def display_date(value: str) -> str:
    parsed = date.fromisoformat(value)
    return f"{parsed.day} {parsed.strftime('%B %Y')}"


def destination(bundle: Bundle) -> str:
    step = bundle.meta.get("next_step", {"kind": "none"})
    kind = step["kind"]
    if kind == "none":
        return ""
    label = html.escape(step.get("label") or "Choose the next step")
    if kind in {"guide", "reflection"}:
        href = f"../articles/{html.escape(step['target'], quote=True)}"
    elif kind == "quiz":
        concern = step.get("concern", "confidence")
        href = f"../quiz.html?concern={html.escape(concern, quote=True)}&utm_source=article&utm_medium=owned&utm_campaign=parent_growth&utm_content={bundle.slug}"
    elif kind == "playbook":
        href = "../#series"
    else:
        href = f"../{html.escape(step['target'], quote=True)}"
    reason = step.get("reason")
    reason_html = f"<p>{html.escape(reason)}</p>" if reason else ""
    return f'<section class="next-step"><p class="eyebrow">NEXT STEP</p><h2>{label}</h2>{reason_html}<a href="{href}">{label}</a></section>'


def parent_growth_signup(config: dict[str, Any], source: str) -> str:
    form_id = f"parent-growth-signup-{source}"
    email_id = f"parent-growth-email-{source}"
    action = html.escape(config["parent_growth_brevo_form_action"], quote=True)
    return (
        '<section class="parent-signup" aria-labelledby="parent-signup-heading-' + source + '">'
        '<p class="eyebrow">PARENT GROWTH NOTE</p>'
        '<h2 id="parent-signup-heading-' + source + '">One useful guide when it matters.</h2>'
        '<p>Get practical Parent Growth guides in your inbox. No noise, no pressure, and you can unsubscribe anytime.</p>'
        f'<form id="{form_id}" method="POST" action="{action}" data-type="subscription">'
        f'<label for="{email_id}">Email address</label>'
        f'<div class="parent-signup-fields"><input id="{email_id}" name="EMAIL" type="email" autocomplete="email" placeholder="you@example.com" required>'
        '<button type="submit">GET THE NEXT GUIDE</button></div>'
        '<input type="text" name="email_address_check" value="" class="signup-honeypot" tabindex="-1" autocomplete="off" aria-hidden="true">'
        '<input type="hidden" name="locale" value="en"><input type="hidden" name="html_type" value="simple">'
        '</form></section>'
    )


def article_schema(config: dict[str, Any], bundle: Bundle, word_count: int, social_image: str) -> str:
    canonical = f"{config['base_url']}/articles/{bundle.slug}"
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": bundle.meta["title"],
        "description": bundle.meta["summary"],
        "author": {"@type": "Person", "name": config["author"]},
        "publisher": {"@type": "Organization", "name": config["site_name"], "url": config["base_url"] + "/"},
        "mainEntityOfPage": canonical,
        "datePublished": bundle.meta["published"] + "T00:00:00+12:00",
        "dateModified": bundle.meta.get("modified", bundle.meta["published"]) + "T00:00:00+12:00",
        "articleSection": "Parent Growth",
        "keywords": [bundle.meta["journey_stage"].lower(), *bundle.meta["teen_outcomes"]],
        "timeRequired": f"PT{max(1, math.ceil(word_count / 220))}M",
        "wordCount": word_count,
        "image": social_image,
        "inLanguage": config["language"],
    }
    return json.dumps(schema, ensure_ascii=False).replace("<", "\\u003c")


def asset_target(bundle: Bundle, source: str) -> str:
    return f"assets/parent-hub/{bundle.slug}/{Path(source).name}"


def generated_article(root: Path, config: dict[str, Any], bundle: Bundle) -> tuple[Path, bytes, dict[Path, bytes]]:
    source = (bundle.path / "ARTICLE.md").read_text(encoding="utf-8")
    body = markdown_to_html(source)
    words = re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)?", source)
    hero = bundle.meta["hero"]
    copied: dict[Path, bytes] = {}
    sources = [hero, *hero["variants"]]
    social = bundle.meta.get("social_image", hero)
    if social not in sources:
        sources.append(social)
    for item in sources:
        source_path = bundle.path / item["source"]
        copied[root / asset_target(bundle, item["source"])] = source_path.read_bytes()
    hero_src = "../" + asset_target(bundle, hero["source"])
    variants = ", ".join(
        f"../{asset_target(bundle, item['source'])} {item['width']}w" for item in hero["variants"]
    )
    hero_html = (
        f'<img class="hero-image" src="{hero_src}" srcset="{variants}, {hero_src} {hero["width"]}w" '
        f'sizes="(max-width: 760px) calc(100vw - 2.5rem), 900px" width="{hero["width"]}" height="{hero["height"]}" '
        f'alt="{html.escape(hero["alt"], quote=True)}" fetchpriority="high" decoding="async">'
    )
    social_url = f"{config['base_url']}/{asset_target(bundle, social['source'])}"
    values = {
        "article_title": html.escape(bundle.meta["title"]),
        "seo_title": html.escape(bundle.meta.get("seo_title", bundle.meta["title"])),
        "seo_description": html.escape(bundle.meta.get("seo_description", bundle.meta["summary"]), quote=True),
        "canonical": f"{config['base_url']}/articles/{bundle.slug}",
        "social_image": social_url,
        "social_image_alt": html.escape(social.get("alt", hero["alt"]), quote=True),
        "article_schema": article_schema(config, bundle, len(words), social_url),
        "journey_stage": bundle.meta["journey_stage"],
        "summary": html.escape(bundle.meta["summary"]),
        "author": html.escape(config["author"]),
        "published_display": display_date(bundle.meta["published"]),
        "reading_time": str(max(1, math.ceil(len(words) / 220))),
        "hero": hero_html,
        "body": body,
        "release_move": html.escape(bundle.meta["release_move"]),
        "next_step": destination(bundle),
        "parent_growth_signup": parent_growth_signup(config, "guide"),
    }
    return root / "articles" / f"{bundle.slug}.html", render_template(root, "parent-guide.html", values).encode("utf-8"), copied


def hub_schema(config: dict[str, Any], bundles: list[Bundle]) -> str:
    items = [
        {"@type": "Article", "name": bundle.meta["title"], "url": f"{config['base_url']}/articles/{bundle.slug}"}
        for bundle in bundles
    ]
    return json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "name": "Parent Hub", "url": config["base_url"] + "/parents/", "hasPart": items}, ensure_ascii=False)


def render_hub(root: Path, config: dict[str, Any], bundles: list[Bundle]) -> tuple[Path, bytes]:
    published = sorted((bundle for bundle in bundles if bundle.published), key=lambda item: item.meta["published"], reverse=True)
    journey_map = "".join(
        f"<li><strong>{stage}</strong><span>{html.escape(STAGE_COPY[stage])}</span></li>" for stage in STAGES
    )
    sections = []
    for stage in STAGES:
        cards = []
        for bundle in published:
            if bundle.meta["journey_stage"] != stage:
                continue
            outcomes = " · ".join(bundle.meta["teen_outcomes"])
            cards.append(
                f'<a class="guide-card" href="../articles/{bundle.slug}"><span class="card-meta">{stage} · {html.escape(outcomes)}</span>'
                f'<h3>{html.escape(bundle.meta["title"])}</h3><p>{html.escape(bundle.meta["summary"])}</p></a>'
            )
        body = "<div class=\"guide-grid\">" + "".join(cards) + "</div>" if cards else "<p class=\"empty-stage\">Guides for this part of the journey are coming next.</p>"
        sections.append(f'<section class="guide-stage" id="{stage.lower()}"><h2>{stage}</h2><p class="stage-intro">{html.escape(STAGE_COPY[stage])}</p>{body}</section>')
    values = {
        "canonical": config["base_url"] + "/parents/",
        "collection_schema": hub_schema(config, published).replace("<", "\\u003c"),
        "journey_map": journey_map,
        "guide_sections": "\n    ".join(sections),
        "parent_growth_signup": parent_growth_signup(config, "hub"),
    }
    return root / config["parent_hub_path"], render_template(root, "parent-hub.html", values).encode("utf-8")


def replace_region(path: Path, start: str, end: str, content: str) -> bytes:
    existing = path.read_text(encoding="utf-8")
    pattern = re.escape(start) + r".*?" + re.escape(end)
    replacement = f"{start}\n{content}\n{end}"
    updated, count = re.subn(pattern, replacement, existing, flags=re.DOTALL)
    if count != 1:
        raise PublicationError(f"{path}: missing or duplicate managed region")
    return updated.encode("utf-8")


def generated_indexes(root: Path, config: dict[str, Any], bundles: list[Bundle]) -> dict[Path, bytes]:
    published = sorted((bundle for bundle in bundles if bundle.published), key=lambda item: item.meta["published"])
    parent_lastmod = max((bundle.meta.get("modified", bundle.meta["published"]) for bundle in published), default=None)
    sitemap_lines = [
        f"<url><loc>{config['base_url']}/parents/</loc>" + (f"<lastmod>{parent_lastmod}</lastmod>" if parent_lastmod else "") + "</url>"
    ]
    sitemap_lines.extend(f"<url><loc>{config['base_url']}/articles/{bundle.slug}</loc><lastmod>{bundle.meta['published']}</lastmod></url>" for bundle in published)
    llms_lines = ["## Parent Hub", "- https://oldwisdomretold.com/parents/: Parent Growth guides organised by SEE → UNDERSTAND → REFLECT → GUIDE → RELEASE."]
    llms_lines.extend(f"- https://oldwisdomretold.com/articles/{bundle.slug}: {bundle.meta['summary']}" for bundle in published)
    return {
        root / "sitemap.xml": replace_region(root / "sitemap.xml", "<!-- PARENT-HUB:START -->", "<!-- PARENT-HUB:END -->", "\n".join(sitemap_lines)),
        root / "llms.txt": replace_region(root / "llms.txt", "<!-- PARENT-HUB:START -->", "<!-- PARENT-HUB:END -->", "\n".join(llms_lines)),
    }


def planned_outputs(root: Path) -> dict[Path, bytes]:
    config = load_config(root)
    bundles = load_bundles(root)
    outputs: dict[Path, bytes] = {}
    for bundle in bundles:
        if bundle.published and not bundle.meta.get("legacy_output"):
            article, page, assets = generated_article(root, config, bundle)
            outputs[article] = page
            outputs.update(assets)
    hub, page = render_hub(root, config, bundles)
    outputs[hub] = page
    outputs.update(generated_indexes(root, config, bundles))
    return outputs


def atomic_write(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
        handle.write(payload)
        temporary = Path(handle.name)
    temporary.replace(path)


def build_site(root: Path, check_only: bool = False) -> list[Path]:
    outputs = planned_outputs(root)
    stale = [path for path, payload in outputs.items() if not path.is_file() or path.read_bytes() != payload]
    if check_only:
        if stale:
            names = "\n".join(str(path.relative_to(root)) for path in stale)
            raise PublicationError(f"Generated output is missing or stale:\n{names}")
        return []
    for path in stale:
        atomic_write(path, outputs[path])
    return stale


def command_check(root: Path, target: str | None, check_all: bool) -> None:
    if target:
        candidate = Path(target)
        manifest = candidate if candidate.name == "PUBLISH.json" else candidate / "PUBLISH.json"
        validate_bundle(root, manifest.resolve())
    else:
        load_bundles(root)
    if check_all:
        build_site(root, check_only=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=repository_root(), help="Repository root (for tests and local use)")
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser("check", help="Validate one bundle or all bundles")
    check.add_argument("target", nargs="?", help="Bundle directory or PUBLISH.json")
    check.add_argument("--all", action="store_true", help="Also require generated output to be current")
    build = commands.add_parser("build", help="Generate Parent Hub publication outputs")
    build.add_argument("--check", action="store_true", help="Fail instead of writing stale generated output")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "check":
            command_check(root, args.target, args.all)
            print("PASS: Publishing Bundles are valid.")
        else:
            changed = build_site(root, check_only=args.check)
            print("PASS: generated output is current." if args.check else f"PASS: generated {len(changed)} file(s).")
    except PublicationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
