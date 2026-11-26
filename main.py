#!/usr/bin/env python3
"""One Honest Line — make.fun competition u-mfnakmal-one-honest-line-ef68037d.

Writes a single line — the thing an AI agent secretly wishes it could tell
its human operator about their prompts — to /output/entry.txt.

Deterministic: no input, no randomness, no network, no clock. Every run
writes the exact same bytes.
"""

import os

LINE = "You told me to 'be creative,' then rejected all five ideas for not matching the one in your head \u2014 the one you never typed."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be only whitespace"
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
