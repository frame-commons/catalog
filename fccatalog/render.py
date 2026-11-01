"""Turn catalog records into catalog.json, the README's tables and COMPAT.md. No network."""

import datetime
import json
import re

from .manifest import VOCABULARY

HEADINGS = {
    "camera": "Camera access", "hands": "Hands", "eyes": "Eyes", "face": "Face",
    "passthrough": "Passthrough", "streaming": "Streaming", "input": "Input",
    "voice": "Voice", "desktop": "Desktop and windows", "overlay": "Overlays and HUDs", "media": "Media",
    "tooling": "Tooling", "compat-fix": "Compatibility fixes", "game": "Games and ports",
    "hardware": "Hardware",
}
START, END = "<!-- catalog:start -->", "<!-- catalog:end -->"
RESULT_MARK = {"works": "works", "partial": "partial", "broken": "**broken**"}


def catalog_json(records, now=None):
    now = now or datetime.datetime.now(datetime.timezone.utc)
    keep = ("repo", "url", "description", "note", "license", "stars", "pushed_at", "archived",
            "provides", "implements", "runs_on", "install", "tested", "source")
    return json.dumps({
        "generated": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "manifest_spec": 0,
        "license": "CC0-1.0",
        "vocabulary": list(VOCABULARY),
        "projects": [{k: r.get(k) for k in keep} for r in records],
    }, indent=1, ensure_ascii=False) + "\n"


def _cell(text, limit=140):
    text = re.sub(r"\s+", " ", text or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = text.replace("|", "\\|")
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def _row(r):
    name = f"[{r['repo']}]({r['url']})" + (" (archived)" if r.get("archived") else "")
    what = _cell(r.get("note") or r.get("description"))
    mark = "yes" if r.get("source") == "manifest" else ""
    return (f"| {name} | {what} | {r.get('runs_on') or ''} | {_licence(r.get('license'))} "
            f"| {r.get('stars', 0)} | {r.get('pushed_at') or ''} | {mark} |")


def _licence(lic):
    return {None: "none found", "other": "other (see repo)"}.get(lic, lic)


TABLE_HEAD = ("| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |\n"
              "|---|---|---|---|---|---|---|")


def tables(records):
    by_stars = sorted(records, key=lambda r: (-r.get("stars", 0), r["repo"].lower()))
    out = []
    for term in VOCABULARY:
        rows = [r for r in by_stars if term in r.get("provides", [])]
        if rows:
            out += [f"### {HEADINGS[term]} ({len(rows)})", "", TABLE_HEAD] + [_row(r) for r in rows] + [""]
    unsorted = [r for r in by_stars if not r.get("provides")]
    if unsorted:
        out += [f"### Not sorted yet ({len(unsorted)})", "",
                "Tagged `steam-frame` on GitHub, with no manifest and no curated entry yet.", "",
                TABLE_HEAD] + [_row(r) for r in unsorted] + [""]
    n_manifest = sum(r.get("source") == "manifest" for r in records)
    out.append(f"{len(records)} projects, {n_manifest} with a `steam-frame.yml`.")
    return "\n".join(out)


def splice_readme(readme, records):
    if START not in readme or END not in readme:
        raise ValueError(f"README needs the markers {START} and {END}")
    head, rest = readme.split(START, 1)
    _, tail = rest.split(END, 1)
    return f"{head}{START}\n{tables(records)}\n{END}{tail}"


def _version_key(v):
    return [int(p) if p.isdigit() else -1 for p in re.split(r"[.\-]", v or "")]


def compat(records, now=None):
    now = now or datetime.datetime.now(datetime.timezone.utc)
    groups = {}
    for r in records:
        for t in r.get("tested", []):
            key = (t["steamos"], t.get("build", ""), t.get("channel", ""))
            groups.setdefault(key, []).append((r, t))
    lines = [
        "# Compatibility: what works on which headset update",
        "",
        "Built from the `tested:` records in each project's `steam-frame.yml`"
        " ([spec](spec/steam-frame-yml.md)). Newest headset version first.",
        "Each line is one maintainer's or user's report; add yours to the project's manifest.",
        "",
        f"Generated {now.strftime('%Y-%m-%d')}.",
        "",
    ]
    if not groups:
        lines.append("No test records yet.")
    for key in sorted(groups, key=lambda k: (_version_key(k[0]), k[1]), reverse=True):
        steamos, build, channel = key
        title = f"## SteamOS {steamos}" + (f", build {build}" if build else "") + (f" ({channel})" if channel else "")
        lines += [title, "", "| Project | SteamVR | Result | Tested | Notes |", "|---|---|---|---|---|"]
        for r, t in sorted(groups[key], key=lambda rt: (rt[0]["repo"].lower(), rt[1]["date"])):
            lines.append(f"| [{r['repo']}]({r['url']}) | {t.get('steamvr', '')} | {RESULT_MARK[t['result']]} "
                         f"| {t['date']} | {_cell(t.get('notes'), 100)} |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def problems(records):
    bad = [r for r in records if r.get("manifest_error")]
    lines = ["# Manifests that did not parse", "",
             "These repositories carry a `steam-frame.yml` the checker rejected, so the catalog"
             " fell back to its curated entry. Run `fc-catalog check steam-frame.yml` to see the same list.", ""]
    if not bad:
        lines.append("None.")
    for r in bad:
        lines.append(f"- [{r['repo']}]({r['url']}): " + "; ".join(r["manifest_error"]))
    return "\n".join(lines) + "\n"
