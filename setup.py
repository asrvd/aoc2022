# setup directory for advent of code each day

import os
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python setup.py <day>")
        sys.exit(1)

    day = sys.argv[1]
    if not day.isdigit():
        print("Day must be a number")
        sys.exit(1)

    if os.path.exists(day):
        print("Day already exists")
        sys.exit(1)

    os.mkdir(f"day{day}")
    os.chdir(f"day{day}")

    with open("input.txt", "w") as f:
        f.write("")

    with open("solution1.py", "w") as f:
        f.write("")

    with open("solution2.py", "w") as f:
        f.write("")


if __name__ == "__main__":
    main()
