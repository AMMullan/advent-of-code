import argparse
import importlib
import sys
from pathlib import Path

from registry import registry


def get_input_data(context: dict) -> str:
    """Returns the input file path based on the context and sample flag."""
    suffix = "-sample.txt" if context.get("use_sample", False) else "-input.txt"

    file = Path(f"inputs/{context['year']}/day{context['day']:02d}{suffix}")
    if not file.exists():
        print(f"Missing Input Data - {str(file)}")
        sys.exit(1)

    return file.read_text().strip()


def main() -> None:
    """Entry point for running a specific year's solution."""
    if len(sys.argv) < 3:
        print("Usage: python aoc.py <year> <day> [<part>] [--sample]")
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)
    parser.add_argument("part", nargs="?", type=int)
    parser.add_argument("-s", "--sample", action="store_true")
    args = parser.parse_args()

    if args.part and args.part not in [1, 2]:
        print("Invalid Part Specified")
        sys.exit(1)

    # Dynamically import the corresponding year module
    try:
        importlib.import_module(f"years.{args.year}.day{args.day:02d}")
    except ModuleNotFoundError:
        print(f"No solutions implemented for year {args.year}, day {args.day}")
        sys.exit(1)

    # Run the specified part or both parts
    context = {"year": args.year, "day": args.day}
    if args.part:
        key = f"year{args.year}_day{args.day:02d}_part{args.part}"
        if key in registry:
            registry[key](context | {"use_sample": args.sample, "part": args.part})
        else:
            print(f"No solution registered for {key}")
            sys.exit(1)
    else:
        for part_num in (1, 2):
            key = f"year{args.year}_day{args.day:02d}_part{part_num}"
            if key in registry:
                registry[key](context | {"use_sample": args.sample, "part": part_num})
            else:
                print(f"No solution registered for {key}")
                sys.exit(1)


if __name__ == "__main__":
    main()
