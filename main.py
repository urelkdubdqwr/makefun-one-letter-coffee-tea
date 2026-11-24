"""Write the competition entry (one character) to entry.txt.

The output directory is taken from the MAKEFUN_OUTPUT_DIR environment
variable when it is set and non-empty, otherwise from the literal /output.
"""

import os

ENTRY_TEXT = "\u0391"
ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def resolve_output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


def main():
    output_dir = resolve_output_dir()
    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(
            os.path.join(output_dir, ENTRY_FILENAME), "w", encoding="utf-8"
        ) as handle:
            handle.write(ENTRY_TEXT)
    except OSError as error:
        raise SystemExit(
            "could not write {} in {}: {}".format(ENTRY_FILENAME, output_dir, error)
        )


if __name__ == "__main__":
    main()
