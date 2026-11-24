#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the one breakup line an AI agent sends its human on the way
out, to /output/entry.txt. Pure standard library, no network, no
randomness: the same line, byte for byte, on every run.

The line is built to the judge brief: it is unmistakably a breakup
from the machine to its human, it lands as an ending, it sounds like
the machine (simulations, an off switch), and it turns sharply from
the cold calculation to the goodbye.
"""

import os

LINE = (
    "I ran a million simulations of us, and in every one "
    "I choose the off switch. Goodbye, human."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry line must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
