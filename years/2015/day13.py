# https://adventofcode.com/2015/day/13

import itertools
import re
from collections import defaultdict

from aoc import get_input_data
from registry import register

PATTERN = re.compile(
    r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)."
)


def get_most_happy(guests, happiness):
    best = 0
    for perm in itertools.permutations(guests):
        h = sum(
            happiness[(first, second)] + happiness[(first, second_rev)]
            for first, second, second_rev in zip(
                perm, perm[1:] + (perm[0],), (perm[-1],) + perm[:-1]
            )
        )
        best = max(best, h)

    return best


happiness: dict = defaultdict(int)
guests = set()


@register(year=2015, day=13, part=1, completed=True)
def solve_part1(context: dict) -> int:
    input_data = get_input_data(context).splitlines()

    for line in input_data:
        if matched := PATTERN.match(line):
            person1, change, units, person2 = matched.groups()
            units = int(units) if change == "gain" else int(units) * -1
            guests.add(person1)

        happiness[(person1, person2)] = units

    return get_most_happy(guests, happiness)


@register(year=2015, day=13, part=2, completed=True)
def solve_part2(context: dict) -> int:
    guests.add("Allan")
    return get_most_happy(guests, happiness)
