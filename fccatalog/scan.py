"""Collect the catalog from GitHub: the curated list, the steam-frame topic, and each repo's manifest.

Reads only public data: the GitHub REST API (a token raises the rate limit, nothing else) and
raw.githubusercontent.com for steam-frame.yml. Writes nothing anywhere; the caller saves the result.
"""

import json
import os
import shutil
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request

import yaml

from . import manifest as mf

API = "https://api.github.com"
RAW = "https://raw.githubusercontent.com"
MANIFEST_NAME = "steam-frame.yml"
TOPICS = ("steam-frame",)
USER_AGENT = "frame-commons-catalog (+https://github.com/frame-commons/catalog)"


def _token():
    if os.environ.get("GITHUB_TOKEN"):
        return os.environ["GITHUB_TOKEN"]
    if shutil.which("gh"):
        r = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
        if r.returncode == 0:
            return r.stdout.strip()
    return None


class GitHub:
    def __init__(self, token=None):
        self.token = token if token is not None else _token()

    def _get(self, url, accept="application/vnd.github+json", max_bytes=None):
        headers = {"User-Agent": USER_AGENT, "Accept": accept}
        if self.token and url.startswith(API):
            headers["Authorization"] = f"Bearer {self.token}"
        for attempt in range(3):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
                    return r.status, r.read() if max_bytes is None else r.read(max_bytes)
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    return 404, b""
                if e.code in (403, 429) and attempt < 2:  # rate limited: back off and retry
                    time.sleep(int(e.headers.get("Retry-After", "20")))
                    continue
                raise
        raise RuntimeError(f"gave up on {url}")

    def json(self, path):
        status, body = self._get(API + path)
        return None if status == 404 else json.loads(body)

    def topic(self, topic):
        repos, page = [], 1
        while True:
            q = urllib.parse.quote(f"topic:{topic}")
            data = self.json(f"/search/repositories?q={q}&per_page=100&page={page}")
            items = (data or {}).get("items", [])
            repos += items
            if len(items) < 100 or page >= 10:  # the search API stops at 1000 results
                return repos
            page += 1

    def repo(self, full_name):
        return self.json(f"/repos/{full_name}")

    def raw(self, full_name, branch, path):
        # one byte over the cap, so the parser reports "too large" instead of reading a truncated file
        status, body = self._get(f"{RAW}/{full_name}/{branch}/{path}", accept="*/*", max_bytes=mf.MAX_BYTES + 1)
        return None if status == 404 else body.decode("utf-8", "replace")


def load_curated(path):
    with open(path) as f:
        entries = yaml.safe_load(f) or []
    out = {}
    for e in entries:
        out[e["repo"].lower()] = e
    return out


def load_excluded(path):
    if not os.path.exists(path):
        return set()
    with open(path) as f:
        return {e["repo"].lower() for e in (yaml.safe_load(f) or [])}


def _meta(r):
    lic = (r.get("license") or {}).get("spdx_id")
    if lic == "NOASSERTION":  # a licence file GitHub couldn't classify, not "no licence"
        lic = "other"
    return {
        "repo": r["full_name"],
        "url": r["html_url"],
        "description": (r.get("description") or "").strip(),
        "license": lic,
        "stars": r.get("stargazers_count", 0),
        "pushed_at": (r.get("pushed_at") or "")[:10],
        "archived": bool(r.get("archived")),
        "fork": bool(r.get("fork")),
        "default_branch": r.get("default_branch") or "main",
    }


def scan(curated, excluded, gh=None, log=print):
    """Return the list of catalog records, sorted by repo name."""
    gh = gh or GitHub()
    found = {}
    for topic in TOPICS:
        for r in gh.topic(topic):
            found.setdefault(r["full_name"].lower(), r)
    log(f"topic search: {len(found)} repos")
    for key, entry in curated.items():
        if key not in found:
            r = gh.repo(entry["repo"])
            if r is None:
                log(f"curated repo gone: {entry['repo']}")
                continue
            found[r["full_name"].lower()] = r

    records = []
    for key, r in sorted(found.items()):
        if key in excluded:
            continue
        cur = curated.get(key)
        if r.get("fork") and not cur:
            continue  # forks appear only when someone curates them in
        try:
            records.append(_record(gh, r, cur))
        except Exception as e:  # one repo's outage or oddity must not stop the build
            log(f"skipped {r.get('full_name')}: {type(e).__name__}: {e}")
    log(f"catalog: {len(records)} projects, {sum(r['source'] == 'manifest' for r in records)} with a manifest")
    return records


def _record(gh, r, cur):
    """One catalog record: GitHub metadata, then the manifest, then the curated entry, then the bare topic hit."""
    rec = _meta(r)
    rec.update(provides=[], implements=[], runs_on=None, install=None, tested=[],
               note=(cur or {}).get("note"), manifest_error=None)
    text = gh.raw(rec["repo"], rec["default_branch"], MANIFEST_NAME)
    if text is not None:
        try:
            m = mf.parse(text)
            rec.update({k: m[k] for k in ("provides", "implements", "runs_on", "install", "tested")})
            rec["source"] = "manifest"
        except mf.ManifestError as e:
            rec["manifest_error"] = e.problems
    if "source" not in rec:
        if cur:
            rec["provides"] = list(cur.get("provides", []))
            rec["runs_on"] = cur.get("runs_on")
            rec["source"] = "curated"
        else:
            rec["source"] = "topic"
    return rec
