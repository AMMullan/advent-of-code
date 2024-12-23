# https://adventofcode.com/2022/day/3

import re

from aoc import get_input_data
from registry import register

part1_regex = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")
part2_delete = re.compile(r"don\'t\(\).*?(do\(\)|$)")


@register(year=2024, day=3, part=1, completed=True)
def solve_part1(context: dict) -> int:
    input_data = get_input_data(context).replace("\n", "")

    program_input = [(int(x), int(y)) for x, y in part1_regex.findall(input_data)]
    return sum(x * y for x, y in program_input)


@register(year=2024, day=3, part=2, completed=True)
def solve_part2(context: dict) -> int:
    input_data = get_input_data(context).replace("\n", "")

    actual_str = part2_delete.sub("", input_data)
    program_input = [(int(x), int(y)) for x, y in part1_regex.findall(actual_str)]

    return sum(x * y for x, y in program_input)
