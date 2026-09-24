
from pathlib import Path
from datetime import datetime
import sys

DATA_DIR = Path("/data")
INPUT_FILE = DATA_DIR / "input.txt"
OUTPUT_FILE = DATA_DIR / "result.txt"


def main():
    print("SWE40006 Task 4.4 Data Processor")
    print("--------------------------------")
    print(f"Started: {datetime.now().isoformat()}")

    if not INPUT_FILE.exists():
        print(f"ERROR: Input file not found: {INPUT_FILE}")
        sys.exit(1)

    text = INPUT_FILE.read_text(encoding="utf-8")

    lines = len(text.splitlines())
    words = len(text.split())
    characters = len(text)

    result = (
        "SWE40006 Task 4.4 Processing Result\n"
        "===================================\n"
        f"Lines: {lines}\n"
        f"Words: {words}\n"
        f"Characters: {characters}\n"
    )

    OUTPUT_FILE.write_text(result, encoding="utf-8")

    print(f"Read input file: {INPUT_FILE}")
    print(f"Lines counted: {lines}")
    print(f"Words counted: {words}")
    print(f"Characters counted: {characters}")
    print(f"Result written to: {OUTPUT_FILE}")
    print("Processing completed successfully.")


if __name__ == "__main__":
    main()