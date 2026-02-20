#!/usr/bin/env python3
"""
Ensure each notebook has an "Open in Colab" badge linking to its GitHub URL.

We insert (or update) a top markdown cell:
  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
    https://colab.research.google.com/github/susanavenda/data_cambridge/blob/main/<path>
  )
"""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote


REPO_ROOT = Path(__file__).resolve().parent.parent
GITHUB_OWNER = "susanavenda"
GITHUB_REPO = "data_cambridge"
GITHUB_BRANCH = "main"


def to_posix_relative(path: Path) -> str:
    rel = path.resolve().relative_to(REPO_ROOT.resolve())
    return rel.as_posix()


def badge_markdown(rel_posix_path: str) -> str:
    # Keep slashes but escape spaces and other special characters in paths.
    rel_escaped = quote(rel_posix_path, safe="/")
    url = (
        f"https://colab.research.google.com/github/{GITHUB_OWNER}/{GITHUB_REPO}"
        f"/blob/{GITHUB_BRANCH}/{rel_escaped}"
    )
    return (
        "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
        f"({url})"
    )


def normalize_source(src) -> list[str]:
    if src is None:
        return []
    if isinstance(src, str):
        return [src]
    if isinstance(src, list):
        return [str(s) for s in src]
    return [str(src)]


def is_colab_badge_cell(cell: dict) -> bool:
    src = "".join(normalize_source(cell.get("source")))
    return ("colab-badge.svg" in src) or ("Open In Colab" in src)


def upsert_badge_cell(nb: dict, rel_posix_path: str) -> bool:
    cells = nb.get("cells")
    if not isinstance(cells, list):
        return False

    badge = badge_markdown(rel_posix_path)

    badge_idx = None
    for i, c in enumerate(cells):
        if isinstance(c, dict) and is_colab_badge_cell(c):
            badge_idx = i
            break

    new_cell = {"cell_type": "markdown", "metadata": {}, "source": [badge]}

    if badge_idx is None:
        cells.insert(0, new_cell)
        return True

    # Update existing cell and move it to top.
    c = cells[badge_idx]
    c["cell_type"] = "markdown"
    c.setdefault("metadata", {})
    c["source"] = [badge]
    if badge_idx != 0:
        cells.pop(badge_idx)
        cells.insert(0, c)
    return True


def format_and_write(path: Path, nb: dict) -> None:
    path.write_text(json.dumps(nb, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    targets: list[Path] = []
    targets += sorted((REPO_ROOT / "notebooks" / "activities-module-1").rglob("*.ipynb"))
    root_prep = REPO_ROOT / "Untitled-1.ipynb"
    if root_prep.exists():
        targets.append(root_prep)

    changed = 0
    for p in targets:
        nb = json.loads(p.read_text(encoding="utf-8"))
        rel = to_posix_relative(p)
        if upsert_badge_cell(nb, rel):
            format_and_write(p, nb)
            changed += 1

    print(f"Updated: {changed} notebooks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

