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


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(output_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, (
        f"entry mismatch: read back {len(written)} chars, "
        f"expected {len(ENTRY)} chars"
    )
    assert len(written) == 147, f"entry must be 147 chars, got {len(written)}"
    print(f"Wrote {len(written)} characters to {output_path}")


if __name__ == "__main__":
    main()
