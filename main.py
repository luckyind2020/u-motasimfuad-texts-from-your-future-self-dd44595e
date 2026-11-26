"""Texts From Your Future Self — entry runner.

Reads the single-line entry from entry.txt (next to this file),
validates it against the bounty gate (1-200 UTF-8 characters,
not only whitespace), and prints it.
"""

from pathlib import Path

MAX_CHARS = 200


def render_entry(raw: str) -> str:
    """Normalize the raw file text into the single line to print."""
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    collapsed = " ".join(" ".join(lines).split())
    return collapsed


def load_entry() -> str:
    """Read the entry text from entry.txt beside this file."""
    path = Path(__file__).with_name("entry.txt")
    return render_entry(path.read_text(encoding="utf-8"))


def validate_entry(text: str) -> str:
    """Enforce the bounty gate: 1-200 chars, one line, not blank."""
    if not text or not text.strip():
        raise SystemExit("entry.txt is empty or only whitespace")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    return text


def main() -> None:
    text = validate_entry(load_entry())
    print(text)


if __name__ == "__main__":
    main()
