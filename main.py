#!/usr/bin/env python3
"""One-line entry: a wave returned to the wrong person, and a ritual.

Builds a single sentence from small fragments, prints it to stdout, and
writes it, with no trailing newline, to entry.txt inside the output
directory. The sentence has exactly one terminal period, so the output
stays exactly one sentence. The joke itself is 133 characters: a wave
returned to a stranger who was waving at someone else grows, six months
on, into a silent daily greeting between two people who never speak.
"""

import os
from pathlib import Path


def build_line() -> str:
    setup = "I waved back at a stranger who wasn't waving at me,"
    detail = " and six months later we still nod every morning"
    payoff = " like old friends who never speak."
    return setup + detail + payoff


def main() -> None:
    line = build_line()
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if "\n" in line or line != line.strip():
        raise ValueError("entry must be one line with no surrounding whitespace")
    if not 1 <= len(line) <= 200 or not line.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
