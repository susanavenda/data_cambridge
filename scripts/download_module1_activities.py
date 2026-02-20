#!/usr/bin/env python3
"""Download Module 1 Colab notebooks into activities-module-1/.
Uses Colab notebook titles (first # heading) as filenames."""

import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, build_opener
from http.cookiejar import CookieJar


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
OUTPUT_DIR = REPO_ROOT / "notebooks" / "activities-module-1" / "from-colab"

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

def _download_google_drive_file(file_id: str, out_path: Path) -> None:
    """
    Download a publicly accessible Google Drive file to out_path.

    Avoids third-party deps (gdown/requests). Handles the common "confirm download"
    interstitial for Drive virus-scan warnings.
    """
    base_url = "https://drive.google.com/uc"
    jar = CookieJar()
    opener = build_opener(
        # cookies are used for the "download_warning" confirm flows
        __import__("urllib.request").request.HTTPCookieProcessor(jar)
    )

    def fetch(url: str) -> bytes:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with opener.open(req, timeout=60) as resp:
            return resp.read()

    # 1) Initial request
    params = {"export": "download", "id": file_id}
    url = f"{base_url}?{urlencode(params)}"
    data = fetch(url)

    # 2) If we got HTML, it may be the confirm page.
    #    Look for a confirm token in the returned HTML.
    #    Example patterns include:
    #      confirm=t&... or confirm=ABCD1234&...
    if data.lstrip().startswith(b"<!") or b"<html" in data[:200].lower():
        m = re.search(rb"confirm=([0-9A-Za-z_\\-]+)", data)
        if m:
            confirm = m.group(1).decode("utf-8")
            url2 = f"{base_url}?{urlencode({'export':'download','confirm':confirm,'id':file_id})}"
            data = fetch(url2)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Drive often serves notebooks as minified one-line JSON.
    # Normalize to pretty-printed JSON for better tooling/editor support.
    try:
        nb = json.loads(data)
        out_path.write_text(json.dumps(nb, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except Exception:
        out_path.write_bytes(data)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for i, fid in enumerate(NOTEBOOK_IDS, start=1):
        out = OUTPUT_DIR / f"activity-{i:02d}.ipynb"
        print(f"[{i:2d}/14] Downloading {fid} -> {out.name}...", end=" ", flush=True)
        try:
            _download_google_drive_file(fid, out)
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
        time.sleep(0.2)

    print("\nDone.")
    print(f"Output: {OUTPUT_DIR}")
    print(f"Downloaded: {len(list(OUTPUT_DIR.glob('*.ipynb')))} notebooks")


if __name__ == "__main__":
    main()
