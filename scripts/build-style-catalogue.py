#!/usr/bin/env python3
"""Import the lookbook style library into the shipped Piton style catalogue.

Reads evals/lookbook/spec/design/VisualStyles.pi, where every style is one
property of a single library anchor, and writes one Piton anchor file per
style under spec/skills/ui/catalogue/styles/, named after the style, such
as EditorialGuideStyle.pi for the style named Editorial guide. The
style text is copied verbatim; only the lookbook bookkeeping (run, page and
verdict) is dropped and a base property (light or dark) is added. The
catalogue travels with the package when it is tethered.

Run from the repository root, then piton format:
    python3 scripts/build-style-catalogue.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "evals/lookbook/spec/design/VisualStyles.pi"
CATALOGUE = ROOT / "spec/skills/ui/catalogue"
OUT = CATALOGUE / "styles"

INDEX_HEADER = """\
// The crux style catalogue: one worked visual style per file in styles/,
// imported from the lookbook by scripts/build-style-catalogue.py. Do not
// edit the style files by hand; change the lookbook and re-run the script.
//
// Each style was drawn for Brightwork, a sample work suite, on the screen
// its screen property names. Content words such as On track, At risk and
// Behind belong to that sample.
//
// The catalogue is deliberately not re-exported from the package entry,
// so a consuming project never compiles or emits it. The UI skills search
// it in the installed package as source. Check it with
// piton check spec/skills/ui/catalogue.
"""

# Runs 1 to 45 were made on a light base, runs 46 onward on a dark one.
FIRST_DARK_RUN = 46
DROP = {"run", "page", "verdict"}

# Anchor names cannot start with a digit, so these names are respelled.
RESPELL = {
    "90s rave flyer": "Nineties rave flyer",
    "1998 homepage": "Homepage 1998",
    "50s diner": "Fifties diner",
}


def anchor_name(name):
    name = RESPELL.get(name, name)
    words = re.split(r"[^A-Za-z0-9]+", name)
    return "".join(w[:1].upper() + w[1:] for w in words if w) + "Style"


def split_styles(lines):
    """Yield (number, body lines at 8+ spaces) for each styleN property."""
    current = None
    for line in lines:
        if line.strip() and not line.startswith("        "):
            if current:
                yield current
            m = re.fullmatch(r"    style(\d+):", line.rstrip())
            current = (int(m.group(1)), []) if m else None
        elif current is not None:
            current[1].append(line)
    if current:
        yield current


def properties(body):
    """Group body lines into (key, lines) for each 8-space property."""
    props = []
    for line in body:
        if not line.strip():
            continue
        if not line.startswith("         "):
            key = line.strip().partition(":")[0]
            props.append((key, [line]))
        else:
            props[-1][1].append(line)
    return props


def values(body):
    return {k: ls[0].partition(":")[2].strip() for k, ls in properties(body)}


def render(anchor, body):
    props = properties(body)
    base = "dark" if int(values(body)["run"]) >= FIRST_DARK_RUN else "light"
    out = [f"export anchor {anchor}:"]
    for key, ls in props:
        if key in DROP:
            continue
        out.extend(line[4:] for line in ls)
        if key == "idea":
            out.append(f"    base: {base}")
    return "\n".join(out) + "\n"


def main():
    lines = SOURCE.read_text().splitlines()
    styles = list(split_styles(lines))
    if not styles:
        sys.exit(f"no styles found in {SOURCE}")
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*"):
        old.unlink()
    anchors = []
    for number, body in sorted(styles):
        anchor = anchor_name(values(body)["name"])
        if anchor in anchors:
            sys.exit(f"style {number} repeats the anchor name {anchor}")
        anchors.append(anchor)
        (OUT / f"{anchor}.pi").write_text(render(anchor, body))
    index = INDEX_HEADER + "\n" + "".join(
        f"from ./styles/{a} export *\n" for a in anchors
    )
    (CATALOGUE / "index.pi").write_text(index)
    print(f"wrote {len(styles)} styles to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
