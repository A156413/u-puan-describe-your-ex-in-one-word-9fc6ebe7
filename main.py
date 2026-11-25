"""Describe Your Ex in One Word — make.fun entry.

Writes exactly one word, a verdict on an ex, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The word: Unsubscribe — the ex as a mailing list you opted out of.
One word, eleven letters: the joke lands at a glance (a person
reduced to spam you finally stopped receiving), it is not the
obvious insult, and anyone who has ever hit "unsubscribe" — or
been ghosted by someone who did — feels the truth in it.
"""

import os

WORD = "Unsubscribe"


def main() -> None:
    # Gate check, done locally before writing: exactly one word,
    # 1-111 characters, not only whitespace.
    assert WORD.strip() == WORD and " " not in WORD and 1 <= len(WORD) <= 111
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod(path, 0o644)
    print(WORD)


if __name__ == "__main__":
    main()
