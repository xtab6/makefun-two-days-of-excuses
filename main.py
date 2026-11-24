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


def main():
    out_dir = "/output"
    clean_output(out_dir)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
