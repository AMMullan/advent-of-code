# https://adventofcode.com/2015/day/2

import math
from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "day2.input"

with open(INPUT_FILE) as input_file:
    input_data = [input_item.strip() for input_item in input_file.readlines()]

part_1 = 0
part_2 = 0
for item in input_data:
    areas = [int(i) for i in item.split('x')]

    # Part 1
    sides = [2 * areas[0] * areas[1], 2 * areas[1] * areas[2], 2 * areas[2] * areas[0]]
    part_1 += sum(sides) + int(min(sides) / 2)

    # Part 2
    areas.sort()
    dimensions = sum(areas[:2] + areas[:2])
    product = math.prod(areas)

    part_2 += dimensions + product

print('Part 1:', part_1)
print('Part 2:', part_2)
