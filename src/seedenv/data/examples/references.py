"""Retrieve bibliographic metadata; optionally pass a DOI on the command line."""
import json
import sys
from urllib.parse import quote
import httpx

doi = sys.argv[1] if len(sys.argv) > 1 else "10.1038/nphys2525"
response = httpx.get("https://api.crossref.org/works/" + quote(doi, safe=""),
                     headers={"User-Agent": "SeedEnv/0.1 (research metadata example)"}, timeout=30)
response.raise_for_status()
work = response.json()["message"]
print(json.dumps({"doi": work["DOI"], "title": work.get("title", []),
                  "published": work.get("published", {}), "url": work.get("URL")}, ensure_ascii=False))
