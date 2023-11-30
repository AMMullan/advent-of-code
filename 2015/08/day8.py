# https://adventofcode.com/2015/day/8

import codecs
from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "day8.input"
with open(INPUT_FILE) as input_file:
    input_data = [line.strip() for line in input_file.readlines()]


def encode_to_escaped_characters(input_string):
    escaped_str = input_string.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped_str}"'


items = []
decoded = []
encoded = []
for item in input_data:
    items.append(len(item))

    decoded.append(len(codecs.decode(item[1:-1], 'unicode_escape')))
    encoded.append(len(encode_to_escaped_characters(item)))

part1_answer = sum(items) - sum(decoded)
part2_answer = sum(encoded) - sum(items)
print(f'{part1_answer=}')
print(f'{part2_answer=}')
