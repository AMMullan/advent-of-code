# https://adventofcode.com/2015/day/12


import json

from aoc import get_input_data
from registry import register


def sum_integers(data, ignore_red=False):
    def recurse(json_data):
        if isinstance(json_data, dict):  # If data is a dictionary
            if ignore_red and "red" in json_data.values():
                return 0

            return sum(map(recurse, json_data.values()))

        elif isinstance(json_data, list):  # If data is a list
            return sum(map(recurse, json_data))

        elif isinstance(json_data, int):  # If data is an integer
            return json_data

        return 0

    return recurse(data)


@register(year=2015, day=12, part=1, completed=True)
def solve_part1(context: dict) -> int:
    input_data = json.loads(get_input_data(context))
    return sum_integers(input_data)


@register(year=2015, day=12, part=2, completed=True)
def solve_part2(context: dict) -> int:
    input_data = json.loads(get_input_data(context))
    return sum_integers(input_data, True)
