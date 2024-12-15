# https://adventofcode.com/2022/day/6


from aoc import get_input_data
from registry import register


@register(year=2022, day=6, part=1)
def solve_part1(context: dict) -> None:
    input_data = get_input_data(context)
    count = 4

    marker = 0
    while marker < len(input_data):
        letters = list(input_data[marker : marker + count])

        if len(set(letters)) != count:
            marker += 1
            continue

        answer = marker + count
        break

    print(f"Part 1: {answer}")


@register(year=2022, day=6, part=2)
def solve_part2(context: dict) -> None:
    input_data = get_input_data(context)
    count = 14

    marker = 0
    while marker < len(input_data):
        letters = list(input_data[marker : marker + count])

        if len(set(letters)) != count:
            marker += 1
            continue

        answer = marker + count
        break

    print(f"Part 2: {answer}")
