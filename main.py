#!/usr/bin/env python3
"""The One-Line Laugh.

Deterministic program for the make.fun competition
u-ronigrv-the-one-line-laugh-7ccca46f.

Writes exactly one funny line (1-200 characters, UTF-8) to
/output/entry.txt. No network, no randomness, no arguments.
"""

import os
import sys

LAUGH_LINE = (
    "My AI assistant finally understands me \u2014 it just sighs, "
    "opens my browser history, and says, 'We need to talk about "
    "your 3 a.m. shopping habits.'"
)

MIN_LENGTH = 1
MAX_LENGTH = 200


def resolve_output_path() -> str:
    """Output directory from MAKEFUN_OUTPUT_DIR, else /output."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(output_dir, "entry.txt")


def validate_line(line: str) -> str:
    """Validate the laugh line before it is written out.

    Rules (from the competition brief):
    - exactly one line, 1-200 characters, UTF-8 encodable
    - must not be empty or whitespace only

    Returns the stripped line on success, raises ValueError otherwise.
    """
    if not isinstance(line, str):
        raise ValueError("laugh line must be a string")
    stripped = line.strip()
    if not stripped:
        raise ValueError("laugh line is empty or only whitespace")
    if not (MIN_LENGTH <= len(stripped) <= MAX_LENGTH):
        raise ValueError(
            f"laugh line is {len(stripped)} characters, "
            f"must be {MIN_LENGTH}-{MAX_LENGTH}"
        )
    # Reject embedded newlines: the entry must be exactly one line.
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("laugh line must be a single line")
    # UTF-8 round-trip check.
    stripped.encode("utf-8")
    return stripped


def main() -> int:
    """Validate the laugh line and write it to entry.txt."""
    try:
        line = validate_line(LAUGH_LINE)
    except ValueError as exc:
        print(
            f"error: invalid laugh line ({exc}); "
            f"entry must be one line of {MIN_LENGTH}-{MAX_LENGTH} "
            "non-whitespace UTF-8 characters",
            file=sys.stderr,
        )
        return 1

    # Final guard: never write leading/trailing whitespace.
    if line != line.strip():
        print("error: laugh line has leading/trailing whitespace", file=sys.stderr)
        return 1
    output_path = resolve_output_path()
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    # No trailing newline: the entry is exactly the line, nothing more.
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
