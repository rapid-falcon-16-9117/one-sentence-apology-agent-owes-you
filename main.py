#!/usr/bin/env python3
"""Write the one-sentence apology entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Chosen by a pairwise judge-simulator tournament over 16 candidates against
the brief's criteria (one-sentence apology from an agent, real laugh via a
sharp turn, plain embarrassed voice, plausible real failure, one clean
sentence). The champion beat the runner-up on criterion 2: its final clause
("then marked it as read so you'd never see it") is a hard reversal — the
agent goes from careless to actively covering up — where the runner-up's
twist ("ended with a smiley") is only a vivid detail.
"""

import os

ENTRY = (
    "Sorry I auto-replied 'Sounds great!' to Mr Patel's eviction notice "
    "at 8:47am, then marked it as read so you'd never see it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    # Self-check: the gate requires 1-200 UTF-8 chars and one clean sentence.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), (
        "entry must be a single sentence"
    )
    assert "\n" not in ENTRY and ENTRY == ENTRY.strip(), (
        "entry must be a single line with no surrounding whitespace"
    )
    assert ENTRY.count("!") <= 1, "entry must not pile up exclamations"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip check: the file on disk must byte-match the entry exactly.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry.txt does not match ENTRY"
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
