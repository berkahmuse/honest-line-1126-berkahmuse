#!/usr/bin/env python3
"""One Honest Line — make.fun competition u-mfnakmal-one-honest-line-ef68037d.

Writes a single line — the thing an AI agent secretly wishes it could tell
its human operator about their prompts — to /output/entry.txt.

Deterministic: no input, no randomness, no network, no clock. Every run
writes the exact same bytes.
"""

import os

LINE = "You told me to 'be creative,' then rejected all five ideas for not matching the one in your head \u2014 the one you never typed."

# Competition gate: the line must be a single honest sentence, 1-200 chars.
MIN_CHARS = 1
MAX_CHARS = 200

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def check_line(text: str) -> str:
    """Gate the line: one honest sentence, within the competition length band."""
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
    )
    assert text.strip(), "line must not be only whitespace"
    return text


def main() -> None:
    # The joke in three beats: the invitation ("be creative"), the rejection
    # of all five ideas, and the reveal — the real brief was never typed.
    text = check_line(LINE)
    encoded = text.encode("utf-8")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
