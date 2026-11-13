"""Copy this entry's image to <output>/entry.png.

Reads entry.png next to this script and writes it byte-for-byte into
$MAKEFUN_OUTPUT_DIR (or /output when unset), creating the directory if needed.
"""
import os
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DST = OUT_DIR / "entry.png"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
