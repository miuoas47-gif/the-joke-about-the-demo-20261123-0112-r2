"""Write one original joke about the demo to $MAKEFUN_OUTPUT_DIR/entry.txt.

No network, no arguments, deterministic output.
"""

import os
import sys

JOKE = (
    "My AI agent fixed the bug live in the demo — then deleted the fix, "
    "apologised, and asked me to rate its confidence."
)

MIN_LEN = 1
MAX_LEN = 280


def validate(text):
    """Gate: one line, 1-280 Unicode code points, not only whitespace,
    no trailing whitespace or newline."""
    if not isinstance(text, str):
        raise ValueError("joke must be text")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if text != text.strip():
        raise ValueError("joke must not start or end with whitespace")
    n = len(text)
    if n < MIN_LEN or n > MAX_LEN:
        raise ValueError(f"joke is {n} code points, must be {MIN_LEN}-{MAX_LEN}")
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    return n


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    validate(JOKE)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Read-back verification: the written file must match exactly.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        print("read-back verification failed", file=sys.stderr)
        return 1
    validate(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
