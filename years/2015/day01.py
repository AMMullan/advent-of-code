# https://adventofcode.com/2015/day/1

from aoc import get_input_data
from registry import register


@register(year=2015, day=1, part=1, completed=True)
def solve_part1(context: dict) -> None:
    input_data = get_input_data(context)

    part_1 = 0
    for char in input_data:
        if char == "(":
            part_1 += 1
        elif char == ")":
            part_1 -= 1

    print("Part 1:", part_1)


@register(year=2015, day=1, part=2, completed=True)
def solve_part2(context: dict) -> None:
    input_data = get_input_data(context)

    floor = 0
    for position, char in enumerate(input_data, 1):
        floor += 1 if char == "(" else -1
        if floor < 0:
            print("Part 2:", position)
            break
