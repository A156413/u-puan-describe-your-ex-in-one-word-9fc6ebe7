"""Describe Your Ex in One Word — make.fun entry.

Writes exactly one word, a verdict on an ex, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The word: ExhibitA — the ex presented as courtroom Exhibit A.
One word, eight characters: the "ex" pun is built into the verdict
itself (Ex-hibit A), a whole relationship reduced to a single piece
of evidence. It reads as a judgement, not an insult — and anyone
who has ever been put on trial for someone else's version of
events feels the truth in it at a glance.
"""

import os

WORD = "ExhibitA"


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
