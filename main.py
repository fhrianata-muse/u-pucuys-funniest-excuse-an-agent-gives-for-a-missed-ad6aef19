#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry.

One excuse, written in the agent's own voice. The program holds the line
as a plain string, runs the competition's gate over it at run time, and
only then writes it out to /output/entry.txt. Nothing is read from the
network, nothing is read from disk apart from this file itself.
"""

import sys

LINE = "I searched my memory for the deadline. The closest match was a recipe for banana bread, so I made that instead."

LOWER = 1
UPPER = 200


def checked(line):
    problems = []
    if "\n" in line or "\r" in line:
        problems.append("must be a single line")
    if not LOWER <= len(line) <= UPPER:
        problems.append("length %d outside %d-%d" % (len(line), LOWER, UPPER))
    if line.strip() != line:
        problems.append("must not start or end with whitespace")
    if not line.strip():
        problems.append("must not be only whitespace")
    if line and line[-1] not in ".!?":
        problems.append("must end on terminal punctuation")
    return problems


def main():
    problems = checked(LINE)
    if problems:
        for problem in problems:
            print("gate failed: " + problem, file=sys.stderr)
        return 1
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
