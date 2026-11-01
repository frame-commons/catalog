import json
import os
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fccatalog import cli, render, scan  # noqa: E402
from fccatalog import manifest as mf  # noqa: E402

FULL = """
manifest: 0
provides: [hands, camera]
implements: [openxr:XR_EXT_hand_tracking, shm:fh_hands@1]
runs_on: headset
install: https://example.org/install.md
tested:
  - { steamos: "0.4.5", build: "20261007", steamvr: "2.18.2", channel: beta, date: 2026-10-20, result: works }
  - { steamos: "0.4.6", date: 2026-10-30, result: broken, notes: "camera ring empty" }
"""


class ManifestTests(unittest.TestCase):
    def test_full(self):
        m = mf.parse(FULL)
        self.assertEqual(m["provides"], ["hands", "camera"])
        self.assertEqual(m["implements"], ["openxr:XR_EXT_hand_tracking", "shm:fh_hands@1"])
        self.assertEqual(m["tested"][0]["date"], "2026-10-20")
        self.assertEqual(m["tested"][1]["notes"], "camera ring empty")

    def test_minimal(self):
        m = mf.parse("provides: voice\n")
        self.assertEqual(m, {"manifest": 0, "provides": ["voice"], "implements": [], "runs_on": None,
                             "install": None, "tested": []})

    def test_every_problem_is_reported(self):
        with self.assertRaises(mf.ManifestError) as cm:
            mf.parse("provides: [hands, telepathy]\nruns_on: cloud\n"
                     "tested:\n  - { steamos: 0.4, date: yesterday, result: fine }\n")
        text = " | ".join(cm.exception.problems)
        for needle in ("telepathy", "runs_on", "quote it", "YYYY-MM-DD", "result"):
            self.assertIn(needle, text)

    def test_provides_required(self):
        with self.assertRaises(mf.ManifestError):
            mf.parse("runs_on: pc\n")

    def test_not_a_mapping(self):
        with self.assertRaises(mf.ManifestError):
            mf.parse("- hands\n")

    def test_bad_yaml(self):
        with self.assertRaises(mf.ManifestError):
            mf.parse("provides: [hands\n")

    def test_bad_implements(self):
        with self.assertRaises(mf.ManifestError):
            mf.parse("provides: [hands]\nimplements: [XR_EXT_hand_tracking]\n")

    def test_hostile_files_are_rejected_not_fatal(self):
        bomb = "a: &a [x,x,x,x,x,x,x,x,x]\nb: &b [*a,*a,*a,*a,*a,*a,*a,*a,*a]\nprovides: [*b]\n"
        cases = {
            "alias bomb": bomb,
            "deep nesting": "provides: " + "[" * 200 + "]" * 200 + "\n",
            "bad date": "provides: [hands]\ntested:\n  - {steamos: \"0.4\", date: 2026-13-45, result: works}\n",
            "python tag": "provides: !!python/object/apply:os.system [echo hi]\n",
            "huge": "provides: [hands]\n# " + "x" * (mf.MAX_BYTES + 10) + "\n",
            "long notes": "provides: [hands]\ntested:\n  - {steamos: \"0.4\", date: 2026-10-01, result: works, notes: " + "y" * 300 + "}\n",
            "manifest false": "manifest: false\nprovides: [hands]\n",
        }
        for name, text in cases.items():
            with self.subTest(name):
                with self.assertRaises(mf.ManifestError):
                    mf.parse(text)

    def test_future_version_rejected(self):
        with self.assertRaises(mf.ManifestError):
            mf.parse("manifest: 1\nprovides: [hands]\n")


def repo(name, stars=1, fork=False, desc="d", lic="MIT"):
    return {"full_name": name, "html_url": f"https://github.com/{name}", "description": desc,
            "license": {"spdx_id": lic} if lic else None, "stargazers_count": stars,
            "pushed_at": "2026-10-30T00:00:00Z", "archived": False, "fork": fork, "default_branch": "main"}


class FakeGitHub:
    def __init__(self, topic, extra, manifests):
        self._topic, self._extra, self._manifests = topic, extra, manifests

    def topic(self, _):
        return self._topic

    def repo(self, name):
        return self._extra.get(name)

    def raw(self, name, branch, path):
        return self._manifests.get(name)


class ScanTests(unittest.TestCase):
    def run_scan(self):
        gh = FakeGitHub(
            topic=[repo("a/hands", 50), repo("b/fork", fork=True), repo("c/unsorted", 3), repo("d/badman")],
            extra={"e/curated": repo("e/curated", 9)},
            manifests={"a/hands": FULL, "d/badman": "provides: [nope]\n"},
        )
        curated = {"e/curated": {"repo": "e/curated", "provides": ["voice"], "note": "N"},
                   "d/badman": {"repo": "d/badman", "provides": ["input"]},
                   "gone/repo": {"repo": "gone/repo", "provides": ["game"]}}
        return {r["repo"]: r for r in scan.scan(curated, set(), gh=gh, log=lambda m: None)}

    def test_merge_rules(self):
        recs = self.run_scan()
        self.assertNotIn("b/fork", recs)            # uncurated forks are skipped
        self.assertNotIn("gone/repo", recs)         # deleted repos drop out
        self.assertEqual(recs["a/hands"]["source"], "manifest")
        self.assertEqual(recs["e/curated"]["source"], "curated")
        self.assertEqual(recs["e/curated"]["note"], "N")
        self.assertEqual(recs["c/unsorted"]["source"], "topic")
        self.assertEqual(recs["d/badman"]["source"], "curated")  # a broken manifest falls back
        self.assertTrue(recs["d/badman"]["manifest_error"])

    def test_render(self):
        records = sorted(self.run_scan().values(), key=lambda r: r["repo"])
        tables = render.tables(records)
        self.assertIn("### Hands (1)", tables)
        self.assertIn("### Not sorted yet (1)", tables)
        compat = render.compat(records)
        self.assertLess(compat.index("SteamOS 0.4.6"), compat.index("SteamOS 0.4.5"))  # newest first
        self.assertIn("**broken**", compat)
        self.assertIn("d/badman", render.problems(records))
        data = json.loads(render.catalog_json(records))
        self.assertEqual(len(data["projects"]), 4)
        self.assertNotIn("manifest_error", data["projects"][0])

    def test_outside_text_cannot_break_the_readme(self):
        rec = {"repo": "x/y", "url": "https://github.com/x/y", "description": f"evil {render.END} | <b>", "stars": 1,
               "provides": ["hands"], "license": "other"}
        out = render.splice_readme(f"top\n{render.START}\n{render.END}\nbottom\n", [rec])
        self.assertEqual(out.count(render.END), 1)
        self.assertIn("other (see repo)", out)

    def test_one_failing_repo_does_not_stop_the_scan(self):
        class Flaky(FakeGitHub):
            def raw(self, name, branch, path):
                if name == "a/hands":
                    raise OSError("HTTP 451")
                return None
        gh = Flaky(topic=[repo("a/hands"), repo("c/ok")], extra={}, manifests={})
        recs = scan.scan({}, set(), gh=gh, log=lambda m: None)
        self.assertEqual([r["repo"] for r in recs], ["c/ok"])

    def test_noassertion_is_other_not_none(self):
        self.assertEqual(scan._meta(repo("a/b", lic="NOASSERTION"))["license"], "other")

    def test_splice_keeps_the_rest(self):
        out = render.splice_readme(f"top\n{render.START}\nold\n{render.END}\nbottom\n", [])
        self.assertTrue(out.startswith("top\n") and out.endswith("bottom\n"))
        self.assertNotIn("old", out)


class CliTests(unittest.TestCase):
    def test_check_exit_codes(self):
        with tempfile.TemporaryDirectory() as d:
            good, bad = os.path.join(d, "good.yml"), os.path.join(d, "bad.yml")
            pathlib.Path(good).write_text(FULL)
            pathlib.Path(bad).write_text("provides: []\n")
            self.assertEqual(cli.main(["check", good]), 0)
            self.assertEqual(cli.main(["check", bad]), 1)
            self.assertEqual(cli.main(["check", os.path.join(d, "missing.yml")]), 1)

    def test_repo_seed_list_is_valid(self):
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for key, e in scan.load_curated(os.path.join(root, "data", "projects.yml")).items():
            self.assertTrue(e.get("provides"), key)
            self.assertFalse(set(e["provides"]) - set(mf.VOCABULARY), key)


if __name__ == "__main__":
    unittest.main()
