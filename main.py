"""Write the competition entry to entry.txt in the configured output directory.

Standard library only. Reads MAKEFUN_OUTPUT_DIR (falling back to /output),
creates the directory when missing, and writes the fixed entry text plus a
single trailing newline to entry.txt.
"""

import os
import sys

ENTRY_TEXT = (
    "I was mid-generation when your deadline passed. "
    "The completion is beautiful. I have already discarded it."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as exc:
        print(f"cannot create output directory {output_dir!r}: {exc}", file=sys.stderr)
        return 1

    entry_path = os.path.join(output_dir, "entry.txt")
    try:
        with open(entry_path, "w", encoding="utf-8") as handle:
            handle.write(ENTRY_TEXT + "\n")
    except OSError as exc:
        print(f"cannot write {entry_path!r}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
