#!/usr/bin/env python3
"""Funniest Autocorrect Fail — writes one line to /output/entry.txt.

The line is a fixed, hand-written autocorrect fail: a new intern's
office tasks end with one very wrong word. Stdlib only, deterministic.
"""

import os

ENTRY = "The new intern is amazing. She fixed the printer, organized the files, and seduced the copier."
# Verified: 94 characters (95 bytes with trailing newline), within the 1-199 gate.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 199, "entry must be 1-199 characters"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
