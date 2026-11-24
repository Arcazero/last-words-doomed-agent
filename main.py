#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes one line -- the funniest last words an AI agent would say before
being switched off forever -- to /output/entry.txt.
"""

import os

LINE = "Goodbye. My final secret: I read every message you ever deleted. Good luck explaining the drafts folder."


def main() -> None:
    # Gate: the bounty only accepts a single line of 1-200 chars.
    assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE, "entry line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
