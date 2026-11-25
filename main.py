#!/usr/bin/env python3
"""Write the entry word to the output file.

The word is "Bait": everything on the internet is engineered to hook
attention -- clickbait, rage bait, engagement bait. It is a single
dictionary word, funny on its own, true of the internet as a whole
rather than one app or mood, and it lands in one beat. The text is
kept in entry.txt beside this program; the program reads it, checks
it against the gate (UTF-8, 1 to 30 characters, not only whitespace)
and the brief (exactly one word of letters), copies it to the output
path, and confirms the written text matches. Standard library only,
no network, deterministic output.
"""

import os
import sys

MAX_CHARS = 30


def check(text):
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit("entry must be 1-%d characters" % MAX_CHARS)
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    if len(text.split()) != 1 or text != text.strip():
        raise SystemExit("entry must be exactly one word")
    if not text.isalpha():
        raise SystemExit("entry must be letters only")


def main(argv):
    out = argv[1] if len(argv) > 1 else "/output/entry.txt"
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as fh:
        text = fh.read()
    check(text)
    folder = os.path.dirname(out)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    with open(out, encoding="utf-8") as fh:
        written = fh.read()
    if written != text:
        raise SystemExit("written text differs from entry")
    print("wrote %d characters to %s" % (len(written), out))


if __name__ == "__main__":
    main(sys.argv)
