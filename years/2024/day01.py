# https://adventofcode.com/2022/day/1


from aoc import get_input_data
from registry import register


@register(year=2024, day=1, part=1)
def part1(context: dict) -> None:
    input_data = get_input_data(context).splitlines()

    left_items = []
    right_items = []
    for item in input_data:
        left_items.append(item.split()[0])
        right_items.append(item.split()[1])

    left_sorted = [int(itm) for itm in sorted(left_items)]
    right_sorted = [int(itm) for itm in sorted(right_items)]
    total = [abs(left - right) for left, right in zip(left_sorted, right_sorted)]

    print(f"Part 1: {sum(total)}")


@register(year=2024, day=1, part=2)
def solve_part2(context: dict) -> None:
    input_data = get_input_data(context).splitlines()
    left_items = []
    right_items = []
    for item in input_data:
        left_items.append(item.split()[0])
        right_items.append(item.split()[1])

    total = [int(item) * right_items.count(item) for item in left_items]

    print(f"Part 2: {sum(total)}")
