"""One-line cat joke entry for make.fun.

Writes the joke to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "My cat doesn't knock things off the table out of spite — she's running gravity tests, and gravity keeps failing."


def main() -> None:
    print(ENTRY)
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
