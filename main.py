#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — make.fun entry.

Writes the one-sentence pitch of the worst, most useless app imaginable
to /output/entry.txt. Deterministic: the same line every run.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-240 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 240:
        print(f"ERROR: entry is {len(line)} chars, over the 240-char limit",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "Meet SockMatch: our AI texts your dryer every morning to ask where your "
    "missing sock went, and after 214 unanswered messages, our founder Gary "
    "finally got a reply \u2014 the sock ran off with a washing machine in Ohio."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Self-check: read back what landed on disk and confirm it is
    # byte-identical to the entry line, so a partial or altered write
    # never ships silently.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("ERROR: entry.txt on disk does not match the entry line",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
