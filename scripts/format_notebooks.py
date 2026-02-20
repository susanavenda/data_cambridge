#!/usr/bin/env python3
"""
Pretty-print .ipynb files in-place.

Some downloads (e.g., from Google Drive / Colab export) are valid notebooks but
stored as minified one-line JSON, which can look "broken" in some editors.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def format_ipynb(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8", errors="strict")
    nb = json.loads(raw)
    formatted = json.dumps(nb, ensure_ascii=False, indent=2) + "\n"
    if formatted == raw or formatted == raw + "\n":
        return False
    path.write_text(formatted, encoding="utf-8")
    return True


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else (Path(__file__).resolve().parent.parent / "notebooks")
    if not root.exists():
        print(f"Path not found: {root}", file=sys.stderr)
        return 2

    files = sorted(root.rglob("*.ipynb"))
    changed = 0
    failed: list[tuple[Path, str]] = []

    for p in files:
        try:
            if format_ipynb(p):
                changed += 1
        except Exception as e:
            failed.append((p, str(e)))

    print(f"Scanned: {len(files)} notebooks")
    print(f"Reformatted: {changed}")
    if failed:
        print(f"Failed: {len(failed)}", file=sys.stderr)
        for p, msg in failed[:20]:
            print(f"- {p}: {msg}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

