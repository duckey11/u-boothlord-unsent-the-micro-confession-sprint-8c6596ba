#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to entry.txt: a To: line naming who
the unsent message was meant for, then the unsent line itself, exactly as
it was typed. Python standard library only, no network, no secrets.

Output: /output/entry.txt, or $MAKEFUN_OUTPUT_DIR/entry.txt when set.
Deterministic: every run writes the exact same bytes.
"""

import os

ENTRY = (
    "To: my mom\n"
    "i still rehearse what i'd say if you asked why i never came home "
    "for dad's birthday, the year you kept my slice in the fridge\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
