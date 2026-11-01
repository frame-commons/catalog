"""Read and check steam-frame.yml manifests (spec/steam-frame-yml.md, version 0)."""

import datetime
import re

import yaml

VOCABULARY = (
    "camera", "hands", "eyes", "face", "passthrough", "streaming", "input",
    "voice", "desktop", "overlay", "media", "tooling", "compat-fix", "game", "hardware",
)
RUNS_ON = ("headset", "pc", "both")
CHANNELS = ("stable", "beta", "preview")
RESULTS = ("works", "partial", "broken")
IMPLEMENTS_RE = re.compile(r"^[a-z][a-z0-9-]*:[A-Za-z0-9_.\-/]+(@[A-Za-z0-9_.\-]+)?$")
VERSION_FIELDS = ("steamos", "build", "steamvr")
MAX_BYTES = 64 * 1024     # manifests come from strangers' repos: bound everything
MAX_DEPTH = 8
MAX_ITEMS = 200


class ManifestError(ValueError):
    def __init__(self, problems):
        super().__init__("; ".join(problems))
        self.problems = problems


def _load(text):
    """safe_load with no aliases (no alias bombs), bounded nesting and a size cap."""
    if len(text.encode("utf-8", "replace")) > MAX_BYTES:
        raise ManifestError([f"file is larger than {MAX_BYTES // 1024} KB"])
    depth = 0
    for event in yaml.parse(text, Loader=yaml.SafeLoader):
        if isinstance(event, yaml.AliasEvent):
            raise ManifestError(["YAML anchors and aliases (*name) are not allowed"])
        if isinstance(event, (yaml.MappingStartEvent, yaml.SequenceStartEvent)):
            depth += 1
            if depth > MAX_DEPTH:
                raise ManifestError([f"nested more than {MAX_DEPTH} levels deep"])
        elif isinstance(event, (yaml.MappingEndEvent, yaml.SequenceEndEvent)):
            depth -= 1
    return yaml.safe_load(text)


def _short(value, limit=40):
    text = repr(value)
    return text if len(text) <= limit else text[: limit - 1] + "…"


def parse(text):
    """Return the checked manifest as a plain dict, or raise ManifestError listing every problem."""
    try:
        return _parse(text)
    except ManifestError:
        raise
    except Exception as e:  # yaml errors, bad dates (2026-13-45), anything else a stranger's file can cause
        raise ManifestError([f"could not read the file: {type(e).__name__}: {str(e)[:200]}"]) from None


def _parse(text):
    raw = _load(text)
    if not isinstance(raw, dict):
        raise ManifestError(["the file must be a mapping of keys (provides: ..., runs_on: ...)"])
    problems = []
    out = {"manifest": raw.get("manifest", 0)}

    if type(out["manifest"]) is not int or out["manifest"] != 0:
        problems.append(f"manifest: this checker knows version 0, got {_short(out['manifest'])}")

    provides = raw.get("provides")
    if isinstance(provides, str):
        provides = [provides]
    if not provides or not isinstance(provides, list):
        problems.append("provides: required, a list of one or more terms")
        provides = []
    if len(provides) > len(VOCABULARY):
        problems.append("provides: more terms than the vocabulary has")
        provides = provides[: len(VOCABULARY)]
    bad = [_short(p) for p in provides if p not in VOCABULARY]
    if bad:
        problems.append(f"provides: unknown term(s) {', '.join(bad[:5])}; known: {', '.join(VOCABULARY)}")
    out["provides"] = [p for p in provides if p in VOCABULARY]

    implements = raw.get("implements", [])
    if isinstance(implements, str):
        implements = [implements]
    if not isinstance(implements, list):
        problems.append("implements: must be a list of kind:name strings")
        implements = []
    if len(implements) > 50:
        problems.append("implements: more than 50 entries")
        implements = implements[:50]
    for item in implements:
        if not isinstance(item, str) or len(item) > 120 or not IMPLEMENTS_RE.match(item):
            problems.append(f"implements: {_short(item)} is not kind:name[@version]")
    out["implements"] = [i for i in implements if isinstance(i, str) and IMPLEMENTS_RE.match(i)]

    runs_on = raw.get("runs_on")
    if runs_on is not None and runs_on not in RUNS_ON:
        problems.append(f"runs_on: {_short(runs_on)}; use one of {', '.join(RUNS_ON)}")
        runs_on = None
    out["runs_on"] = runs_on

    install = raw.get("install")
    if install is not None and (not isinstance(install, str) or len(install) > 500):
        problems.append("install: must be one command or a URL, as a string of 500 characters or fewer")
        install = None
    out["install"] = install

    tested = raw.get("tested", [])
    if not isinstance(tested, list):
        problems.append("tested: must be a list of test records")
        tested = []
    if len(tested) > MAX_ITEMS:
        problems.append(f"tested: more than {MAX_ITEMS} records; drop the oldest")
        tested = tested[-MAX_ITEMS:]
    out["tested"] = []
    for n, rec in enumerate(tested, 1):
        rec_out, rec_problems = _test_record(rec)
        problems += [f"tested[{n}]: {p}" for p in rec_problems]
        if not rec_problems:
            out["tested"].append(rec_out)

    if problems:
        raise ManifestError(problems)
    return out


def _test_record(rec):
    if not isinstance(rec, dict):
        return None, ["must be a mapping like { steamos: \"0.4.5\", date: 2026-10-20, result: works }"]
    problems = []
    out = {}
    for field in VERSION_FIELDS:
        value = rec.get(field)
        if value is None:
            if field == "steamos":
                problems.append("steamos: required (the headset's SteamOS version)")
            continue
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            problems.append(f"{field}: quote it (\"{value}\"), YAML reads unquoted versions as numbers")
            continue
        if not isinstance(value, str) or len(value) > 40:
            problems.append(f"{field}: must be a short quoted string")
            continue
        out[field] = value
    channel = rec.get("channel")
    if channel is not None and channel not in CHANNELS:
        problems.append(f"channel: {_short(channel)}; use one of {', '.join(CHANNELS)}")
    elif channel is not None:
        out["channel"] = channel
    date = rec.get("date")
    if isinstance(date, datetime.date):
        out["date"] = date.isoformat()
    elif isinstance(date, str) and _iso_date(date):
        out["date"] = date
    else:
        problems.append("date: required, as YYYY-MM-DD")
    result = rec.get("result")
    if result not in RESULTS:
        problems.append(f"result: required, one of {', '.join(RESULTS)}")
    else:
        out["result"] = result
    notes = rec.get("notes")
    if notes is not None:
        if isinstance(notes, str) and len(notes) <= 200:
            out["notes"] = notes
        else:
            problems.append("notes: one line of text, 200 characters or fewer")
    return out, problems


def _iso_date(text):
    try:
        datetime.date.fromisoformat(text)
        return re.match(r"^\d{4}-\d{2}-\d{2}$", text) is not None
    except ValueError:
        return False
