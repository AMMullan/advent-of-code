# https://adventofcode.com/2022/day/4


from aoc import get_input_data
from registry import register


def get_points(char):
    return ord(char) - 96 if char.islower() else ord(char.lower()) - 96 + 26


def batch(iterable, n=1):
    length = len(iterable)
    for ndx in range(0, length, n):
        yield iterable[ndx : min(ndx + n, length)]


@register(year=2022, day=3, part=1, completed=True)
def solve_part1(context: dict) -> int:
    input_data = get_input_data(context).splitlines()
    part1_total = 0
    for item in input_data:
        item_size = len(item) // 2
        first = item[:item_size]
        second = item[item_size:]

        matches = {char for char in first if char in second}

        for match in matches:
            part1_total += get_points(match)

    return part1_total


@register(year=2022, day=3, part=2, completed=True)
def solve_part2(context: dict) -> int:
    input_data = get_input_data(context).splitlines()
    part2_total = 0
    for items in batch(input_data, 3):
        matches = {char for char in items[0] if char in items[1] and char in items[2]}
        for match in matches:
            part2_total += get_points(match)

    return part2_total
