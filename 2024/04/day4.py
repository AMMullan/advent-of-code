# https://adventofcode.com/2022/day/4

from pathlib import Path


def part1(input_data) -> int:
    transposed = ["".join(item) for item in map(list, zip(*input_data))]

    occurrences = 0
    for item in [input_data, transposed]:
        for line in item:
            occurrences += line.count("XMAS")
            occurrences += line.count("SAMX")

    print(input_data)
    print(transposed)
    return occurrences


def part2(input_data) -> int:
    return 0


if __name__ == "__main__":
    INPUT_FILE = Path("day4.sample")
    with open(INPUT_FILE) as input_file:
        input_data = [line.strip() for line in input_file.readlines()]

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
