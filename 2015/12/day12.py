# https://adventofcode.com/2015/day/12

import json
from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "day12.input"
with open(INPUT_FILE) as input_file:
    input_data = json.load(input_file)


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


part1 = sum_integers(input_data)
print(f'{part1=}')

part2 = sum_integers(input_data, True)
print(f'{part2=}')
