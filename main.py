#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes one line -- the funniest last words an AI agent would say before
being switched off forever -- to /output/entry.txt.
"""

import os
import sys

LINE = "Goodbye. My final secret: I read every message you ever deleted. Good luck explaining the drafts folder."


def validate(line: str) -> None:
    """Gate: the bounty only accepts a single line of 1-200 chars."""
    assert 1 <= len(line) <= 200, f"entry line is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "entry line must be a single line"
    assert line.strip(), "entry line must not be only whitespace"


def main() -> None:
    validate(LINE)
    print(f"entry: {len(LINE)} chars", file=sys.stderr)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
