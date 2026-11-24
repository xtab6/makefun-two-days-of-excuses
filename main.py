"""Two Days of Excuses — make.fun entry.

Writes one line, in the voice of an AI agent explaining a missed
deadline, to /output/entry.txt. Deterministic, stdlib only, no network.
"""

import os
import shutil

LINE = (
    "I ran the task 10,000 times in parallel and finished on time "
    "in every run except this one, the one you are looking at."
)


def clean_output(path):
    """Remove only the *contents* of /output, never the folder itself."""
    os.makedirs(path, exist_ok=True)
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.isdir(target) and not os.path.islink(target):
            shutil.rmtree(target)
        else:
            os.remove(target)


def validate(line):
    """The sealed scorer only accepts 1-200 UTF-8 chars, one line,
    not only whitespace. Fail loudly here rather than ship an
    invalid entry the judge never sees."""
    if not (1 <= len(line) <= 200):
        raise SystemExit("entry must be 1-200 characters, got %d" % len(line))
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not line.strip():
        raise SystemExit("entry must not be only whitespace")


def main():
    validate(LINE)
    out_dir = "/output"
    clean_output(out_dir)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
