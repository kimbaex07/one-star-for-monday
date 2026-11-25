#!/usr/bin/env python3
"""One Star for Monday — writes a one-line, one-star review of Monday
(written as if Monday were a restaurant) to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure Python standard library only.
"""

import os
import sys

LINE = "Came for breakfast at 8, sat down at 10, cold coffee, and the bill charged me for the whole weekend. One star. Never again, Monday."

MAX_CHARS = 180


def main() -> int:
    # Gate guard: the entry must be UTF-8 text of 1-180 characters,
    # a single line, and not only whitespace.
    if not LINE or not LINE.strip():
        raise SystemExit("gate: entry is empty or only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("gate: entry must be a single line")
    if len(LINE) > MAX_CHARS:
        raise SystemExit(
            "gate: entry is %d chars, over the 180-char limit" % len(LINE)
        )
    if len(LINE.split()) > 25:
        raise SystemExit(
            "gate: entry is %d words, over the 25-word limit"
            % len(LINE.split())
        )
    # The gate reads the file as UTF-8 text, so prove the line survives a
    # UTF-8 round-trip with no replacement characters before writing it.
    if LINE.encode("utf-8").decode("utf-8") != LINE:
        raise SystemExit("gate: entry is not clean UTF-8 text")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
