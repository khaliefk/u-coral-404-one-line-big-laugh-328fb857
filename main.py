"""One Line, Big Laugh entry.

Writes a single funny line to /output/entry.txt.
"""

import os
from pathlib import Path

LINE = (
    "I finally cleaned my room and found my motivation under the bed, "
    "dead since 2019, next to a charger for a phone I never owned."
)


def main():
    # Gate: 1 to 200 characters, one line, no trailing newline so the
    # file holds exactly the line that gets judged.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert "\n" not in LINE and LINE.strip() == LINE
    output = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
