# https://adventofcode.com/2022/day/3

import re
from pathlib import Path

part1_regex = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")
part2_delete = re.compile(r"don\'t\(\).*?(do\(\)|$)")


def part1(input_data) -> int:
    program_input = [(int(x), int(y)) for x, y in part1_regex.findall(input_data)]
    return sum(x * y for x, y in program_input)


def part2(input_data) -> int:
    actual_str = part2_delete.sub("", input_data)
    program_input = [(int(x), int(y)) for x, y in part1_regex.findall(actual_str)]
    return sum(x * y for x, y in program_input)


if __name__ == "__main__":
    INPUT_FILE = Path("day3.input")
    input_data = INPUT_FILE.read_text().replace("\n", "")
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
