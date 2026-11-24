"""One-Sentence Absurd Invention Pitch — make.fun entry.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance: a printer that demands compliments and jams
in silent protest when shouted at. Stdlib only.
"""

import os
import sys

LINE = (
    "A printer that refuses to print until you compliment it, "
    "then jams in silent protest the moment you raise your voice."
)

MAX_CHARS = 220


def main() -> int:
    text = LINE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    if any(ch in text for ch in "\r\n"):
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
