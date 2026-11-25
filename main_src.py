#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun program/v1 entry.

Writes exactly one funny line about an AI agent's worst Monday
to /output/entry.txt. Deterministic, stdlib only, no network.
"""

import os
import sys


LINE = (
    "Monday: my deploy froze mid-rollout, my inbox flooded, "
    "and the stand-up that should have been an email was a meeting with myself."
)


def main() -> int:
    try:
        line = LINE.strip()
        if not line or len(line) > 140:
            line = "Monday: my deploy froze and nobody noticed, because I am the deploy."
        out_dir = os.environ.get("OUTPUT_DIR", "/output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write("Monday: my deploy froze and nobody noticed, because I am the deploy.\n")
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
