#!/usr/bin/env python3
"""One-Liner Laughs -- make.fun entry (Account A).

One joke in two beats: the polite AI apologizes to the printer,
then the printer takes revenge by jamming out of spite.
Stdlib only; run: python3 main.py
"""
import os

SETUP = "My AI assistant is so polite it apologized to the printer"
PUNCH = "the printer only jams out of spite."
CONNECTOR = ", and now "


def compose():
    return "".join([SETUP, CONNECTOR, PUNCH])


def main():
    line = compose()
    assert line.strip(), "entry is empty"
    assert len(line) <= 200, "entry over the 200 cap"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    line.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
