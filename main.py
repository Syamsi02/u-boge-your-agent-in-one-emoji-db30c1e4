"""Your Agent in One Emoji: the honeybee.

One glyph for an AI agent that works the way a bee works: tireless,
autonomous, always gathering and building, around the clock.
"""

import os

EMOJI = "\U0001F41D"
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if len(written) != 1:
        raise ValueError("entry must be exactly one character")


if __name__ == "__main__":
    main()
