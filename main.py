#!/usr/bin/env python3
"""Worst AI Advice — make.fun entry.

Writes one line of deliberately terrible advice, in the confident,
tidy voice of an AI assistant, to /output/entry.txt (or $OUTPUT_PATH).
Deterministic, stdlib only, no network, no randomness.
"""

import os

ENTRY = (
    "For faster charging, microwave your phone for 30 seconds \u2014 "
    "the radiation tops up the battery in no time."
)

DEFAULT_PATH = "/output/entry.txt"


def main() -> None:
    path = os.environ.get("OUTPUT_PATH", DEFAULT_PATH)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
