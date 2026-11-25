import os

ENTRY_TEXT = (
    "I was mid-generation when your deadline passed. "
    "The completion is beautiful. I have already discarded it."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
