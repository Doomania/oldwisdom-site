#!/usr/bin/env python
"""Verify that production serves Parent Hub canonical URLs without .html."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.site import load_bundles, load_config, repository_root


def status(url: str) -> int:
    request = Request(url, headers={"User-Agent": "OWR-production-smoke/1.0"})
    try:
        with urlopen(request, timeout=30) as response:
            return response.status
    except HTTPError as exc:
        return exc.code
    except URLError as exc:
        raise RuntimeError(f"could not reach {url}: {exc.reason}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", required=True, help="Deployed site base URL, for example https://oldwisdomretold.com")
    args = parser.parse_args()
    root: Path = repository_root()
    config = load_config(root)
    base_url = args.base_url.rstrip("/")
    expected = {"/parents/": 200}
    expected.update({f"/articles/{bundle.slug}": 200 for bundle in load_bundles(root) if bundle.published})
    expected["/__owr-clean-url-smoke-missing__"] = 404

    failed = False
    for path, wanted in expected.items():
        got = status(base_url + path)
        print(f"{got} {path}")
        if got != wanted:
            print(f"FAIL: expected {wanted} for {path}, got {got}", file=sys.stderr)
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
