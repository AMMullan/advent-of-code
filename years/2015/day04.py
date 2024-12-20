# https://adventofcode.com/2015/day/4

import hashlib

from aoc import get_input_data
from registry import register


def get_stuffer(input_data, zero_count) -> int:
    current_num = 0
    while True:
        result = hashlib.md5(f"{input_data}{str(current_num)}".encode())
        hex_ = result.hexdigest()

        if hex_.startswith("0" * zero_count):
            return current_num

        current_num += 1


@register(year=2015, day=4, part=1, completed=True)
def solve_part1(context: dict) -> int:
    input_data = get_input_data(context)
    return get_stuffer(input_data, 5)


@register(year=2015, day=4, part=2, completed=True)
def solve_part2(context: dict) -> int:
    input_data = get_input_data(context)
    return get_stuffer(input_data, 6)
