# https://adventofcode.com/2022/day/4

from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "day3.input"
with open(INPUT_FILE) as input_file:
    input_data = [line.strip() for line in input_file.readlines()]


def get_points(char):
    return ord(char) - 96 if char.islower() else ord(char.lower()) - 96 + 26


def batch(iterable, n=1):
    length = len(iterable)
    for ndx in range(0, length, n):
        yield iterable[ndx : min(ndx + n, length)]


part1_total = 0
for item in input_data:
    item_size = len(item) // 2
    first = item[:item_size]
    second = item[item_size:]

    matches = {char for char in first if char in second}

    for match in matches:
        part1_total += get_points(match)

part2_total = 0
for items in batch(input_data, 3):
    matches = {char for char in items[0] if char in items[1] and char in items[2]}
    for match in matches:
        part2_total += get_points(match)

print(f'Part 1: {part1_total}')
print(f'Part 2: {part2_total}')
