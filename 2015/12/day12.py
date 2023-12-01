# https://adventofcode.com/2015/day/12

import json
from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "day12.input"
with open(INPUT_FILE) as input_file:
    input_data = json.load(input_file)


def sum_integers(data, ignore_red=False):
    total = 0

    if isinstance(data, dict):  # If data is a dictionary
        if ignore_red and "red" in data.values():
            return total

        for value in data.values():
            total += sum_integers(value, ignore_red)  # Recursive call

    elif isinstance(data, list):  # If data is a list
        for item in data:
            total += sum_integers(item, ignore_red)  # Recursive call

    elif isinstance(data, int):  # If data is an integer
        total = data

    return total


part1 = sum_integers(input_data)
print(part1)

part2 = sum_integers(input_data, True)
print(part2)
