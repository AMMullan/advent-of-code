# https://adventofcode.com/2015/day/9

from itertools import permutations

from aoc import get_input_data
from registry import register


@register(year=2015, day=9, part=1)
def solve_part1(context: dict) -> None:
    input_data = get_input_data(context).splitlines()

    distances = {}
    locations = set()

    for line in input_data:
        start, _, end, _, distance = line.split()
        distances[frozenset([start, end])] = int(distance)
        locations.update([start, end])

    shortest = min(
        sum(distances[frozenset([a, b])] for a, b in zip(route, route[1:]))
        for route in permutations(locations)
    )

    print(shortest)


@register(year=2015, day=9, part=2)
def solve_part2(context: dict) -> None:
    input_data = get_input_data(context).splitlines()

    distances = {}
    locations = set()

    for line in input_data:
        start, _, end, _, distance = line.split()
        distances[frozenset([start, end])] = int(distance)
        locations.update([start, end])

    longest = max(
        sum(distances[frozenset([a, b])] for a, b in zip(route, route[1:]))
        for route in permutations(locations)
    )

    print(longest)
