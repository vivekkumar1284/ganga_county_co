#!/usr/bin/env python3
"""Update site URL placeholders across docs/*.html and docs/site-config.js

Usage:
  python3 scripts/set-site-url.py https://yourusername.github.io/ganga_county
  python3 scripts/set-site-url.py https://www.yourdomain.com
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PLACEHOLDER = "https://YOUR_USERNAME.github.io/ganga_county"


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    new_url = sys.argv[1].rstrip("/")
    updated = 0
    for path in list(DOCS.glob("*.html")) + [DOCS / "site-config.js"]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if PLACEHOLDER not in text and "YOUR_USERNAME.github.io" not in text:
            continue
        text2 = text.replace(PLACEHOLDER, new_url)
        text2 = re.sub(
            r"https://YOUR_USERNAME\.github\.io/ganga_county",
            new_url,
            text2,
        )
        if text2 != text:
            path.write_text(text2, encoding="utf-8")
            updated += 1
            print(f"updated {path.relative_to(ROOT)}")
    print(f"Done. Files updated: {updated}")


if __name__ == "__main__":
    main()
