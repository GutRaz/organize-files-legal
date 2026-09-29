"""Writes the publisher's details from publisher.json into every document of this repository.

Each detail sits in the text between two HTML comments, which a reader on GitHub does not see:

    **Contact:** <!--publisher:ContactEmail-->name@example.com<!--/publisher-->

Change a value in publisher.json, run this script, and every document says the new one. Nothing
outside the comments is touched, so each file keeps its wording and its line endings.

Usage: python tools/refresh_publisher_facts.py [--check]

    --check  changes nothing, and exits with 1 when a document is out of date, names a detail
             publisher.json does not have, or leaves a marker open.
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPENING = "<!--publisher:"
MARKER = re.compile(r"<!--publisher:([A-Za-z]+)-->(.*?)<!--/publisher-->")


def main(argv):
    check = "--check" in argv[1:]
    facts = json.loads((ROOT / "publisher.json").read_text(encoding="utf-8"))
    problems, changed = [], []
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.relative_to(ROOT).parts:
            continue
        name = path.relative_to(ROOT).as_posix()
        text = path.read_bytes().decode("utf-8")
        markers = MARKER.findall(text)
        if text.count(OPENING) != len(markers):
            problems.append(f"{name}: a marker is not closed with <!--/publisher-->")
        for key, _ in markers:
            if key not in facts:
                problems.append(f"{name}: publisher.json has no {key}")
        filled = MARKER.sub(
            lambda m: f"<!--publisher:{m.group(1)}-->{facts.get(m.group(1), m.group(2))}<!--/publisher-->",
            text)
        if filled != text:
            changed.append(name)
            if not check:
                path.write_bytes(filled.encode("utf-8"))

    for problem in problems:
        print(problem)
    if check:
        for name in changed:
            print(f"{name}: out of date with publisher.json")
        return 1 if problems or changed else 0
    print(f"{len(changed)} documents updated")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
