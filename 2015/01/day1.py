# https://adventofcode.com/2015/day/1
from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "day1.input"

with open(INPUT_FILE) as input_file:
    input_data = input_file.read().strip()

part_1 = 0
part_2 = 0
for idx, char in enumerate(input_data):
    if char == '(':
        part_1 += 1
    elif char == ')':
        part_1 -= 1

    if not part_2 and part_1 < 0:
        part_2 = idx + 1

print('Part 1:', part_1)
print('Part 2:', part_2)
