# https://adventofcode.com/2015/day/13

import itertools
import re
from collections import defaultdict
from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "day13.input"
with open(INPUT_FILE) as input_file:
    input_data = [line.strip() for line in input_file.readlines()]

PATTERN = re.compile(
    r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).'
)

happiness = defaultdict(int)
guests = set()

for line in input_data:
    if matched := PATTERN.match(line):
        person1, change, units, person2 = matched.groups()
        units = int(units) if change == 'gain' else int(units) * -1
        guests.add(person1)

    happiness[(person1, person2)] = units


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


print(f'Part 1: {get_most_happy(guests, happiness)}')
guests.add('Allan')
print(f'Part 2: {get_most_happy(guests, happiness)}')
