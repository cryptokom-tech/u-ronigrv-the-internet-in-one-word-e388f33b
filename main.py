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
MAX_WORD_CHARS = 200


def validate(word):
    """Validate the brief-level shape of the entry word.

    The entry must be a single word made only of letters, with a
    length between 1 and 200 characters. This is intentionally
    separate from the stricter gate check in check() below so the
    brief rules can be reused for any candidate word.
    """
    if not isinstance(word, str):
        raise SystemExit("entry must be text")
    if not 1 <= len(word) <= MAX_WORD_CHARS:
        raise SystemExit("entry must be 1-%d characters" % MAX_WORD_CHARS)
    if not word.strip():
        raise SystemExit("entry is only whitespace")
    if len(word.split()) != 1 or word != word.strip():
        raise SystemExit("entry must be exactly one word")
    if not word.isalpha():
        raise SystemExit("entry must be letters only")
    return word


def check(text):
    validate(text)
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit("entry must be 1-%d characters" % MAX_CHARS)


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
    # Read-back verification: re-read the file we just wrote and
    # confirm it still holds exactly the validated entry word.
    with open(out, encoding="utf-8") as fh:
        written = fh.read()
    if written != text:
        raise SystemExit("written text differs from entry")
    validate(written)
    check(written)
    if os.path.getsize(out) != len(text.encode("utf-8")):
        raise SystemExit("written byte count differs from entry")
    print("wrote %d characters to %s" % (len(written), out))


if __name__ == "__main__":
    main(sys.argv)
