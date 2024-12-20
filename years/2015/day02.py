# https://adventofcode.com/2015/day/2

import math

from aoc import get_input_data
from registry import register


@register(year=2015, day=2, part=1, completed=True)
def solve_part1(context: dict) -> int:
    input_data = get_input_data(context).splitlines()

    part_1 = 0
    for item in input_data:
        areas = [int(i) for i in item.split("x")]

        # Part 1
        sides = [
            2 * areas[0] * areas[1],
            2 * areas[1] * areas[2],
            2 * areas[2] * areas[0],
        ]
        part_1 += sum(sides) + int(min(sides) / 2)

    return part_1


@register(year=2015, day=2, part=2, completed=True)
def solve_part2(context: dict) -> int:
    input_data = get_input_data(context).splitlines()

    part_2 = 0
    for item in input_data:
        areas = [int(i) for i in item.split("x")]

        # Part 2
        areas.sort()
        dimensions = sum(areas[:2] + areas[:2])
        product = math.prod(areas)

        part_2 += dimensions + product

    return part_2
