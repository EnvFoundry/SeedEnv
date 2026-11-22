"""Exercise a fresh native TeX install and every distinct writing template.

Use --home to retain the installation and --output for the generated projects.
This script explicitly downloads TinyTeX when absent; core tests remain offline.
"""
import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from seedenv import Manager
from seedenv.tex import prepare
from seedenv.writing import templates, create_manuscript


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--home", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    manager = Manager(args.home)
    command, location = prepare(manager.home)
    manager.state.bind("tool-tex", manager.catalog.components["tool-tex"], command, location, True)
    seen = set()
    failed = []
    for template in templates()["items"]:
        if template["file"] in seen:
            continue
        seen.add(template["file"])
        destination = Path(args.output).absolute() / template["id"]
        if not destination.exists():
            create_manuscript(template["id"], destination)
        result = manager.build(str(destination / "main.tex"))
        print(template["id"], result["status"], flush=True)
        if result["status"] != "built":
            failed.append(template["id"])
            print(Path(result["transcript"]).read_text(encoding="utf-8", errors="replace")[-5000:])
    print(f"{len(seen) - len(failed)}/{len(seen)} distinct templates compiled")
    return bool(failed)


if __name__ == "__main__":
    raise SystemExit(main())
