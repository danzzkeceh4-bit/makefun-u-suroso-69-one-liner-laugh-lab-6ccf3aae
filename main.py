#!/usr/bin/env python3
"""One-Liner Laugh Lab — make.fun entry.

Writes one funny line (the excuse a robot vacuum gives after eating a sock)
to /output/entry.txt: exactly 147 characters, no trailing newline.
Then reads it back and asserts it matches the constant exactly.
No network, no external input.
"""

import os

ENTRY = (
    "I didn't eat your sock \u2014 I adopted it. It was cold, alone, and "
    "clearly plotting something under the bed. Ask the dust bunnies; "
    "they saw everything."
)


def validate_entry(text: str) -> None:
    """Validate the entry before writing: 1-200 chars, no trailing newline."""
    assert 1 <= len(text) <= 200, (
        f"entry length {len(text)} chars out of range 1-200"
    )
    assert not text.endswith("\n"), "entry must not end with a newline"


def main() -> None:
    validate_entry(ENTRY)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(output_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, (
        f"entry mismatch after read-back: got {len(written)} chars "
        f"({len(written.encode('utf-8'))} bytes), expected {len(ENTRY)} chars "
        f"({len(ENTRY.encode('utf-8'))} bytes) — entry text does not match"
    )
    assert len(written) == 147, f"entry must be 147 chars, got {len(written)}"
    print(f"Wrote {len(written)} characters to {output_path}")


if __name__ == "__main__":
    main()
