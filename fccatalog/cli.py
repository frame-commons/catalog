"""fc-catalog: check a steam-frame.yml, or rebuild the catalog.

  fc-catalog check [FILE ...]          check manifests (default ./steam-frame.yml); exit 1 on problems
  fc-catalog build [--root DIR]        scan GitHub, write catalog.json, README tables, COMPAT.md, PROBLEMS.md
  fc-catalog render [--root DIR]       rewrite the README tables, COMPAT.md, PROBLEMS.md from catalog.json only
"""

import argparse
import json
import os
import sys

from . import manifest as mf
from . import render, scan


def cmd_check(args):
    status = 0
    for path in args.files or ["steam-frame.yml"]:
        try:
            with open(path, "rb") as f:
                m = mf.parse(f.read(mf.MAX_BYTES + 1).decode("utf-8", "replace"))
        except FileNotFoundError:
            print(f"{path}: not found")
            status = 1
            continue
        except mf.ManifestError as e:
            print(f"{path}: {len(e.problems)} problem(s)")
            for p in e.problems:
                print(f"  - {p}")
            status = 1
            continue
        print(f"{path}: ok — provides {', '.join(m['provides'])}; {len(m['tested'])} test record(s)")
    return status


def _write(root, records, catalog_text=None):
    if catalog_text is not None:
        with open(os.path.join(root, "catalog.json"), "w") as f:
            f.write(catalog_text)
    readme_path = os.path.join(root, "README.md")
    with open(readme_path) as f:
        readme = f.read()
    with open(readme_path, "w") as f:
        f.write(render.splice_readme(readme, records))
    with open(os.path.join(root, "COMPAT.md"), "w") as f:
        f.write(render.compat(records))
    with open(os.path.join(root, "PROBLEMS.md"), "w") as f:
        f.write(render.problems(records))


def cmd_build(args):
    root = args.root
    curated = scan.load_curated(os.path.join(root, "data", "projects.yml"))
    excluded = scan.load_excluded(os.path.join(root, "data", "excluded.yml"))
    records = scan.scan(curated, excluded, log=lambda m: print(m, file=sys.stderr))
    new = render.catalog_json(records)
    try:  # keep the old file (and its "generated" time) when nothing changed, so idle weeks make no commit
        with open(os.path.join(root, "catalog.json")) as f:
            if json.load(f)["projects"] == json.loads(new)["projects"]:
                new = None
    except (OSError, ValueError, KeyError):
        pass
    _write(root, records, new)
    return 0


def cmd_render(args):
    with open(os.path.join(args.root, "catalog.json")) as f:
        records = json.load(f)["projects"]
    _write(args.root, records)
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="fc-catalog", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("check", help="check steam-frame.yml files")
    p.add_argument("files", nargs="*")
    p.set_defaults(fn=cmd_check)
    for name, fn in (("build", cmd_build), ("render", cmd_render)):
        p = sub.add_parser(name)
        p.add_argument("--root", default=".")
        p.set_defaults(fn=fn)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
