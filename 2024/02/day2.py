# https://adventofcode.com/2022/day/2

import itertools
from pathlib import Path


def generate_combinations(input_list: list) -> list:
    # Create combinations by omitting one element at a time
    return [
        list(comb) for comb in itertools.combinations(input_list, len(input_list) - 1)
    ]


def is_safe(levels: list[int]) -> bool:
    is_increasing = levels[0] < levels[1]

    for left, right in itertools.pairwise(levels):
        error_1 = is_increasing and left > right
        error_2 = not is_increasing and left < right
        error_3 = left == right
        error_4 = abs(left - right) > 3
        if any([error_1, error_2, error_3, error_4]):
            return False

    return True


def part1(input_data) -> int:
    safe = 0
    for report in input_data:
        levels = [int(level) for level in report.split()]
        if is_safe(levels):
            safe += 1

    return safe


def part2(input_data) -> int:
    safe = 0
    for report in input_data:
        levels = [int(level) for level in report.split()]
        if is_safe(levels):
            safe += 1
        elif any(is_safe(new_list) for new_list in generate_combinations(levels)):
            safe += 1

    return safe


if __name__ == "__main__":
    INPUT_FILE = Path("day2.input")
    with open(INPUT_FILE) as input_file:
        input_data = [line.strip() for line in input_file.readlines()]

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
