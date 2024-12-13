# https://adventofcode.com/2015/day/4

import hashlib

from aoc import get_input_data
from registry import register


def get_stuffer(input_data, zero_count):
    current_num = 0
    while True:
        result = hashlib.md5(f"{input_data}{str(current_num)}".encode())
        hex_ = result.hexdigest()

        if hex_.startswith("0" * zero_count):
            return current_num

        current_num += 1


@register(year=2015, day=4, part=1)
def solve_part1(context: dict) -> None:
    input_data = get_input_data(context)
    print("Part 1:", get_stuffer(input_data, 5))


@register(year=2015, day=4, part=2)
def solve_part2(context: dict) -> None:
    input_data = get_input_data(context)
    print("Part 1:", get_stuffer(input_data, 6))
