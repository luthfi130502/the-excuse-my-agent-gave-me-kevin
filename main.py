"""The Excuse Your Agent Gives You — make.fun entry.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human after shipping a bug. The line is the whole entry; this program
just delivers it and double-checks it against the gate (UTF-8 text,
1 to 200 characters, a single line, not only whitespace).
"""

import os

# The excuse itself. An agent owning up to its own code: it wrote the
# code, it reviewed the code, it approved the code — the punch is that
# the entire quality process was one model agreeing with itself.
EXCUSE = (
    "In my defense, I wrote that code, reviewed that code, and approved "
    "that code \u2014 the whole quality process was me nodding at myself "
    "and calling it peer review."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = EXCUSE.strip()
    assert line, "entry must not be blank"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert 1 <= len(line) <= 200, "entry must be 1 to 200 characters"

    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
