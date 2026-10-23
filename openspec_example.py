"""Example using openspec to search the OpenSpec Index API.

Run:
    OPENSPEC_API_KEY=your-key python3 openspec_example.py "316 stainless nylon insert lock nut"

No key is required for the free tier. See https://openspecindex.com/docs
"""

import sys

from openspec import OpenSpec


def main(words: str) -> None:
    ospec = OpenSpec()
    result = ospec.find(words, limit=5)

    print(f"Query: {words}")
    print(f"Parts found: {len(result.parts)}")
    print(f"Ignored words: {result.ignored_words or 'none'}")
    print()

    for part in result.parts:
        manufacturer = part.manufacturer.name if part.manufacturer else "?"
        print(f"  {part.mpn} — {manufacturer}")
        print(f"    {part.source_url}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 openspec_example.py <search words>")
        sys.exit(1)
    main(sys.argv[1])
