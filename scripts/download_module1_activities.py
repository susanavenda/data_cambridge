#!/usr/bin/env python3
"""Download Module 1 Colab notebooks into activities-module-1/.
Uses Colab notebook titles (first # heading) as filenames."""

import json
import re
import sys
from pathlib import Path


def _get_notebook_title(path: Path) -> str | None:
    """Extract first meaningful # heading from notebook."""
    try:
        nb = json.loads(path.read_text())
        for c in nb.get("cells", []):
            src = "".join(c.get("source", []))
            for m in re.finditer(r"^#+\s+(.+)$", src, re.M):
                t = m.group(1).strip()
                if "First things first" not in t and "Academic integrity" not in t and len(t) > 5:
                    return re.sub(r'[\\/:*?"<>|$]', "-", t).strip()[:100]
    except Exception:
        pass
    return None

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "activities-module-1"

# Colab notebook IDs (from sharing URLs)
NOTEBOOK_IDS = [
    "12ks-SWT5Q27KM6v8yxsy759V43AV-LOu",
    "1AOXRSRWaBFndVpezc1b2rNbLDmOBihP8",
    "1DRbt6phCwXuOfKkA0ai_6a7YvtgjPu0c",
    "1JRNYgd_uri3ztnoGujBw47oulgN9jU_7",
    "1KHF0qhiQoM8DYbpg_jU6DzasOKKzxlEQ",
    "1MGNDtpMZt7ADCEpwx82o0dFSePNJZcji",
    "1N1-L5JYeC7Ne7rt6ZWpzxVJp1RDdUfrh",
    "1PJCm4m1KXCf3S1ZBBJ9p0OiGq2YsXghl",
    "1aWvvk9gi92DdBOUHVEBwTxbg2s5oa_8F",
    "1exFgkWDb2ToylLp10WQp5K26eQ27JggV",
    "1iX9wpKSVo0Q6yMEN4BbRze4wuKhqO5xb",
    "1jA1GWs2BGOov8mHwb9CAA_WmAHCgT0DI",
    "1pTH0aOluJLr3YRuW56MHMOFwKlxJMtMy",
    "1ycWjElyZNje23jB86L3Kf6MKVsI8I2qq",
]


def main():
    try:
        import gdown
    except ImportError:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "gdown", "-q"])
        import gdown

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for i, fid in enumerate(NOTEBOOK_IDS, start=1):
        out = OUTPUT_DIR / f"activity-{i:02d}.ipynb"
        url = f"https://drive.google.com/uc?id={fid}"
        print(f"[{i:2d}/14] Downloading {fid} -> {out.name}...", end=" ", flush=True)
        try:
            gdown.download(url, str(out), quiet=True, fuzzy=False)
            if out.exists() and out.stat().st_size > 100:
                # Rename to Colab title (first # heading)
                name = _get_notebook_title(out)
                if name:
                    final = OUTPUT_DIR / f"{name}.ipynb"
                    if final.exists() and final.resolve() != out.resolve():
                        final = OUTPUT_DIR / f"{name} ({i}).ipynb"
                    out.rename(final)
                    print(f"-> {final.name}")
                else:
                    print("OK")
            else:
                print("FAIL (empty or missing)")
        except Exception as e:
            print(f"FAIL: {e}")

    print("\nDone.")
    print(f"Output: {OUTPUT_DIR}")
    print(f"Downloaded: {len(list(OUTPUT_DIR.glob('*.ipynb')))} notebooks")


if __name__ == "__main__":
    main()
