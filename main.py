#!/usr/bin/env python3
"""Write one original line in the Moon's voice for make.fun.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.

The joke is built on the Moon's ledger: four billion years of
listening, and the bill it sends back. Wishes, howls and 2 a.m.
promises are the three things people have always aimed at the sky,
so the line names all three, then pays them off with the only two
things humanity ever actually left up there — a flag and a golf
ball. The Moon comes off old, wry and faintly underpaid, which is
the voice the brief asks for, and the turn lands in one read
because the grandeur of "four billion years" collapses into
souvenirs.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def get_line() -> str:
    """Return the entry line: the Moon totals up four billion years of
    wishes, howls and late-night promises and presents its souvenirs.
    """
    return (
        "Four billion years of wishes, howls, and 2 a.m. promises "
        "— and all I ever got was a flag and a golf ball."
    )


LINE = get_line()


def validate(line: str) -> None:
    """Enforce the gate: 1-240 chars, exactly one non-blank UTF-8 line."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 240:
        raise ValueError("entry line must be 1-240 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Round-trip check: what the grader reads must be exactly the line.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == LINE + "\n", "entry.txt round-trip mismatch"
    print(LINE)


if __name__ == "__main__":
    main()
