#!/usr/bin/env python
"""Generate OWR's central content, destination, and Pinterest-card register.

Bundle PUBLISH.json/RELEASE.json are source-of-truth. This report also indexes
legacy Pinterest JSON evidence so no historical Pin record is silently lost.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PRODUCTION = ROOT / "content" / "production"
# Channel-only historical creative is deliberately outside the static-site checkout.
# It feeds audit reports but is never needed for a website build or release check.
PINTEREST_ARCHIVE = Path("D:/Claude/Projects/oldwisdomretold-social")
LEGACY_PINTEREST = PINTEREST_ARCHIVE / "legacy_pinterest_assets"
OUTPUT = ROOT / "docs" / "OWR_CONTENT_REGISTER.md"
SITE = "https://oldwisdomretold.com"
PIN_KEYS = {"pin_url", "permalink", "scheduled_pin_url", "href"}


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def esc(value: object) -> str:
    return str(value or "—").replace("|", "\\|").replace("\n", " ").strip()


def source_label(path: Path) -> str:
    """Use repo-relative paths where possible; preserve exact external archive paths."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def verify_live(url: str) -> str:
    if not url:
        return "missing URL"
    try:
        with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/123 Safari/537.36"}), timeout=15) as response:
            return str(response.status)
    except HTTPError as exc:
        return f"HTTP {exc.code}"
    except URLError as exc:
        return f"network error: {exc.reason}"


def pinterest_cards(path: Path, document: dict) -> list[dict]:
    """Extract exact card/permalink URLs with their nearest available context."""
    found: list[dict] = []

    def walk(value: object, context: dict) -> None:
        if isinstance(value, dict):
            local = context.copy()
            for key in ("destination", "destination_url", "url"):
                candidate = value.get(key)
                if isinstance(candidate, str) and "oldwisdomretold.com/" in candidate:
                    local["destination"] = candidate
            for key in ("id", "title", "status", "scheduled_date", "scheduled_time"):
                if value.get(key) not in (None, ""):
                    local[key] = value[key]
            for key, candidate in value.items():
                if (key in PIN_KEYS or key == "url") and isinstance(candidate, str) and ("pinterest.com/pin/" in candidate or "pinterest.com/oldwisdomretold/scheduled-pin/" in candidate):
                    found.append({
                        "url": candidate,
                        "kind": "live permalink" if "/pin/" in candidate else "scheduled card",
                        "destination": local.get("destination", ""),
                        "id": local.get("id", ""),
                        "title": local.get("title", ""),
                        "status": local.get("status", ""),
                        "when": " ".join(str(local.get(k, "")) for k in ("scheduled_date", "scheduled_time")).strip(),
                        "source": source_label(path),
                    })
                walk(candidate, local)
        elif isinstance(value, list):
            for item in value:
                walk(item, context)

    walk(document, {})
    return found


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the OWR audit register.")
    parser.add_argument("--verify-live", action="store_true", help="GET published article destinations and record HTTP status.")
    parser.add_argument("--verify-pins", action="store_true", help="GET stored public Pinterest permalinks and record HTTP status.")
    args = parser.parse_args()
    records, parse_errors = [], []
    for publish_path in sorted(PRODUCTION.glob("*/PUBLISH.json")):
        publish = load_json(publish_path)
        if not publish:
            parse_errors.append(str(publish_path.relative_to(ROOT)))
            continue
        bundle, release = publish_path.parent, load_json(publish_path.parent / "RELEASE.json")
        article = release.get("article", {}) if isinstance(release.get("article"), dict) else {}
        pinterest = release.get("pinterest", {}) if isinstance(release.get("pinterest"), dict) else {}
        email = release.get("email", {}) if isinstance(release.get("email"), dict) else {}
        slug = str(publish.get("slug", ""))
        destination = str(article.get("url") or (f"{SITE}/articles/{slug}" if slug else ""))
        status = str(publish.get("status", ""))
        records.append({
            "bundle": bundle.name, "slug": slug, "title": str(publish.get("title", "")),
            "status": status, "published": str(publish.get("published", "")),
            "article_state": str(article.get("state", "")), "destination": destination,
            "has_release": (bundle / "RELEASE.json").is_file(),
            "live_status": verify_live(destination) if args.verify_live and status == "published" else "not checked",
            "page_exists": (ROOT / "articles" / f"{slug}.html").exists(),
            "pinterest_state": str(pinterest.get("state", "")), "email_state": str(email.get("state", "")),
        })

    cards: list[dict] = []
    for root in (PRODUCTION, LEGACY_PINTEREST):
        if root.exists():
            for path in root.rglob("*.json"):
                document = load_json(path)
                if document:
                    cards.extend(pinterest_cards(path, document))
    # One Pin/card can appear in a queue, a verification snapshot, and a release
    # record. Collapse exact URLs while retaining the richest evidence record.
    unique_cards: dict[str, dict] = {}
    for card in cards:
        prior = unique_cards.get(card["url"])
        if prior is None or (not prior["destination"] and card["destination"]):
            unique_cards[card["url"]] = card
    cards = sorted(unique_cards.values(), key=lambda card: (card["kind"], card["source"], card["url"]))
    # Legacy scheduler cards predate permalink capture. Match only an exact, unique
    # live title from the authenticated profile audit; never guess from a near match.
    def title_key(value: str) -> str:
        return " ".join(re.sub(r"[^a-z0-9]+", " ", (value or "").casefold()).split())
    live_destinations: dict[str, set[str]] = {}
    for card in cards:
        if card["kind"] == "live permalink" and card["destination"] and card["title"]:
            live_destinations.setdefault(title_key(card["title"]), set()).add(card["destination"])
    for card in cards:
        key = title_key(card["title"])
        candidates = set()
        for live_title, destinations in live_destinations.items():
            # Pinterest's scheduled surface appends the board title; preserve a
            # match only when the original Pin title is otherwise exact.
            if key == live_title or key.startswith(live_title + " ") or live_title.startswith(key + " "):
                candidates.update(destinations)
        if card["kind"] == "scheduled card" and not card["destination"] and len(candidates) == 1:
            card["destination"] = next(iter(candidates))
    cdp_confirmed_urls = {card["url"] for card in cards if "live_profile_audit" in card["source"]}
    for card in cards:
        if args.verify_pins and card["kind"] == "live permalink":
            card["url_status"] = "CDP confirmed" if card["url"] in cdp_confirmed_urls else verify_live(card["url"])
        else:
            card["url_status"] = "not checked"
    records.sort(key=lambda row: (row["published"] or "9999-99-99", row["bundle"]))
    published = [row for row in records if row["status"] == "published"]
    missing_pages = [row for row in published if not row["page_exists"]]
    missing_releases = [row for row in published if not row["has_release"]]
    failing_live = [row for row in published if args.verify_live and row["live_status"] != "200"]
    live_permalinks = [card for card in cards if card["kind"] == "live permalink"]
    rate_limited_pins = [card for card in live_permalinks if args.verify_pins and card["url_status"] == "HTTP 429"]
    failing_pins = [card for card in live_permalinks if args.verify_pins and card["url_status"] not in {"200", "CDP confirmed", "HTTP 429"}]
    scheduled_cards = [card for card in cards if card["kind"] == "scheduled card"]
    unlinked_cards = [card for card in cards if not card["destination"]]

    lines = [
        "# OWR Content & Destination Register", "",
        "> Generated by `python scripts/owr_content_register.py` from bundle source records plus legacy Pinterest JSON evidence. Do not edit manually.",
        "> `PUBLISH.json` and `RELEASE.json` remain the operational source of truth. Legacy evidence is indexed here until reconciled into its owning release record.", "",
        f"**Generated:** {date.today().isoformat()}",
        f"**Bundles:** {len(records)} · **Published:** {len(published)} · **Recorded live Pinterest permalinks:** {len(live_permalinks)} · **Recorded scheduled Pinterest cards:** {len(scheduled_cards)}", "",
        "## Guide register", "",
        "| Bundle | Status | Article state | Canonical destination | Live check | Pinterest | Email |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in records:
        lines.append(f"| `{esc(row['bundle'])}` | {esc(row['status'])} | {esc(row['article_state'])} | {esc(row['destination'])} | {esc(row['live_status'])} | {esc(row['pinterest_state'])} | {esc(row['email_state'])} |")
    lines += ["", "## Pinterest card register", "", "| Type | Card / permalink | URL check | Canonical destination | ID/title | Scheduled | Evidence source |", "|---|---|---|---|---|---|---|"]
    for card in cards:
        label = card["id"] or card["title"] or "—"
        lines.append(f"| {esc(card['kind'])} | {esc(card['url'])} | {esc(card['url_status'])} | {esc(card['destination'])} | {esc(label)} | {esc(card['when'])} | `{esc(card['source'])}` |")
    lines += ["", "## Integrity snapshot", ""]
    lines.append(f"- {'BLOCKER' if missing_pages else 'PASS'} — published bundles missing generated article file: {len(missing_pages)}.")
    lines.append(f"- {'BLOCKER' if missing_releases else 'PASS'} — published bundles missing RELEASE.json: {len(missing_releases)}.")
    lines.append(f"- {'BLOCKER' if failing_live else 'PASS'} — failed/non-200 published live checks: {len(failing_live)}." if args.verify_live else "- Live URL GET checks not run (use `--verify-live`).")
    lines.append(f"- {'BLOCKER' if failing_pins else 'PASS'} — failed/non-200 recorded public Pinterest permalinks (excluding provider rate limits): {len(failing_pins)}." if args.verify_pins else "- Public Pinterest permalink GET checks not run (use `--verify-pins`).")
    lines.append(f"- {'NOTABLE' if rate_limited_pins else 'PASS'} — public Pinterest checks rate-limited by provider (HTTP 429): {len(rate_limited_pins)}; CDP feed membership remains source of truth.") if args.verify_pins else None
    lines.append(f"- NOTABLE — Pinterest records without a nearby stored canonical destination: {len(unlinked_cards)}. Reconcile before deleting legacy evidence.")
    lines.append(f"- {'BLOCKER' if parse_errors else 'PASS'} — malformed PUBLISH.json files: {len(parse_errors)}.")
    if missing_pages:
        lines += [f"  - `{row['bundle']}` → expected `articles/{row['slug']}.html`" for row in missing_pages]
    lines += ["", "## Audit procedure", "", "1. Run `python scripts/owr_content_register.py --verify-live --verify-pins` after a release, scheduling update, or housekeeping change.", "2. Reconcile every legacy scheduled/live card into its owning bundle `RELEASE.json`; do not delete its legacy evidence first.", "3. Run `python scripts/site.py check --all`; do not commit regenerated live output without approval if it changes the deployed site.", "4. The weekly audit is report-only: it must never delete, deploy, reschedule, or change social destinations."]
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"PASS: wrote {OUTPUT.relative_to(ROOT)} ({len(records)} bundles; {len(live_permalinks)} permalinks; {len(scheduled_cards)} scheduled cards)")


if __name__ == "__main__":
    main()
