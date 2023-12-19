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
        h = 0
        for i in range(len(perm)):
            first = perm[i]
            second = perm[(i + 1) % len(perm)]
            second_rev = perm[(i - 1) % len(perm)]

            h += happiness[(first, second)]
            h += happiness[(first, second_rev)]

        best = max(best, h)

    return best


print(f'Part 1: {get_most_happy(guests, happiness)}')
guests.add('Allan')
print(f'Part 2: {get_most_happy(guests, happiness)}')
