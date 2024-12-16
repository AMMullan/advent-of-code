# https://adventofcode.com/2015/day/3

from aoc import get_input_data
from registry import register


def deliveries(input_data, players):
    houses = {(0, 0): 0}
    x = [0] * players
    y = [0] * players

    for c, move in enumerate(input_data):
        p = c % players
        x[p] += {"^": 0, "v": 0, ">": 1, "<": -1}[move]

        y[p] += {"^": 1, "v": -1, ">": 0, "<": 0}[move]

        houses[(x[p], y[p])] = houses.get((x[p], y[p]), 0) + 1

    return len(houses)


@register(year=2015, day=3, part=1, completed=True)
def solve_part1(context: dict) -> None:
    input_data = get_input_data(context)
    print("Part 1:", deliveries(input_data, 1))


@register(year=2015, day=3, part=2, completed=True)
def solve_part2(context: dict) -> None:
    input_data = get_input_data(context)
    print("Part 2:", deliveries(input_data, 2))
