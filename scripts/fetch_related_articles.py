#!/usr/bin/env python3
"""Fetch only the redistributable PDFs listed in refs/related_articles.json.

Requires Python 3.10+ and Poppler (pdfinfo, pdftotext). Original PDF bytes are
preserved. Existing locked copies must match their recorded SHA-256 checksum.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 30 * 1024 * 1024
ALLOWED_HOSTS = {"www.preprints.org", "works.vntu.edu.ua", "arxiv.org", "drops.dagstuhl.de"}


def inspect_pdf(path: Path, item: dict) -> tuple[str, int]:
    data = path.read_bytes()
    if not data.startswith(b"%PDF-") or b"%%EOF" not in data[-4096:]:
        raise ValueError(f"{path.name}: response is not a complete PDF")
    info = subprocess.run(["pdfinfo", str(path)], check=True, capture_output=True, text=True).stdout
    match = re.search(r"^Pages:\s+(\d+)", info, re.MULTILINE)
    if match is None or int(match.group(1)) != item["pages"]:
        raise ValueError(f"{path.name}: unexpected page count")
    text = subprocess.run(["pdftotext", "-f", "1", "-l", "2", str(path), "-"],
                          check=True, capture_output=True, text=True).stdout
    normalized = " ".join(text.casefold().split())
    if any(term.casefold() not in normalized for term in item["title_markers"]):
        raise ValueError(f"{path.name}: title does not match the requested paper")
    return hashlib.sha256(data).hexdigest(), len(data)


def download(item: dict, target: Path) -> str:
    url = item["pdf_url"]
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS:
        raise ValueError(f"Unapproved source: {url}")
    for attempt in range(3):
        try:
            request = Request(url, headers={"User-Agent": "pnp-literature-archive/1.0 (+https://github.com/tarstars/pnp)"})
            with urlopen(request, timeout=45) as response:
                final_url = response.geturl()
                if urlparse(final_url).scheme != "https":
                    raise ValueError("Refusing a non-HTTPS redirect")
                data = response.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                raise ValueError("Download exceeds the 30 MiB limit")
            with tempfile.NamedTemporaryFile(dir=target.parent, suffix=".pdf", delete=False) as tmp:
                temporary = Path(tmp.name)
                tmp.write(data)
            try:
                inspect_pdf(temporary, item)
                temporary.replace(target)
            finally:
                temporary.unlink(missing_ok=True)
            return final_url
        except (OSError, ValueError, subprocess.CalledProcessError) as exc:
            if attempt == 2:
                raise RuntimeError(f"Unable to fetch {item['id']}: {exc}") from exc
            time.sleep(2 ** (attempt + 1))
    raise AssertionError("unreachable")


def main() -> None:
    for program in ("pdfinfo", "pdftotext"):
        if shutil.which(program) is None:
            raise RuntimeError(f"Install poppler-utils: missing {program}")
    manifest = json.loads((ROOT / "refs/related_articles.json").read_text(encoding="utf-8"))
    destination = ROOT / "refs/pdfs"
    destination.mkdir(parents=True, exist_ok=True)
    lock_path = destination / "manifest.lock.json"
    old_records = json.loads(lock_path.read_text(encoding="utf-8"))["files"] if lock_path.exists() else []
    old = {entry["id"]: entry for entry in old_records}
    records = []
    for item in manifest["articles"]:
        if item["copy_policy"] != "mirror":
            print(f"LINK ONLY: {item['id']}")
            continue
        filename = item["filename"]
        if Path(filename).name != filename or not filename.endswith(".pdf"):
            raise ValueError("Expected a PDF basename, not a path")
        path = destination / filename
        final_url = old.get(item["id"], {}).get("resolved_url", item["pdf_url"])
        if not path.exists():
            final_url = download(item, path)
        digest, size = inspect_pdf(path, item)
        previous = old.get(item["id"])
        if previous and previous["sha256"] != digest:
            raise ValueError(f"Checksum changed for {filename}; inspect the upstream version before updating")
        records.append({"id": item["id"], "path": "refs/pdfs/" + filename,
                        "source_url": item["pdf_url"], "resolved_url": final_url,
                        "sha256": digest, "bytes": size, "pages": item["pages"],
                        "license": item["license"], "license_url": item["license_url"]})
        print(f"VERIFIED: {filename} ({item['pages']} pages; SHA-256 {digest})")
    lock = {"schema_version": 1, "files": records}
    lock_path.write_text(json.dumps(lock, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    sums = "".join(f"{record['sha256']}  {Path(record['path']).name}\n" for record in records)
    (destination / "SHA256SUMS").write_text(sums, encoding="ascii")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
