# https://adventofcode.com/2015/day/8

import codecs

from aoc import get_input_data
from registry import register


def encode_to_escaped_characters(input_string):
    escaped_str = input_string.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped_str}"'


@register(year=2015, day=8, part=1, completed=True)
def solve_part1(context: dict) -> int:
    input_data = get_input_data(context).splitlines()

    items = []
    decoded = []
    encoded = []
    for item in input_data:
        items.append(len(item))

        decoded.append(len(codecs.decode(item[1:-1], "unicode_escape")))
        encoded.append(len(encode_to_escaped_characters(item)))

    return sum(items) - sum(decoded)


@register(year=2015, day=8, part=2, completed=True)
def solve_part2(context: dict) -> int:
    input_data = get_input_data(context).splitlines()

    items = []
    decoded = []
    encoded = []
    for item in input_data:
        items.append(len(item))

        decoded.append(len(codecs.decode(item[1:-1], "unicode_escape")))
        encoded.append(len(encode_to_escaped_characters(item)))

    return sum(encoded) - sum(items)
