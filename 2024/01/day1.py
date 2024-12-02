# https://adventofcode.com/2022/day/1

from pathlib import Path


def part1(input_data):
    left_items = []
    right_items = []
    for item in input_data:
        left_items.append(item.split()[0])
        right_items.append(item.split()[1])

    left_sorted = [int(itm) for itm in sorted(left_items)]
    right_sorted = [int(itm) for itm in sorted(right_items)]
    total = [abs(left - right) for left, right in zip(left_sorted, right_sorted)]

    return sum(total)


def part2(input_data):
    left_items = []
    right_items = []
    for item in input_data:
        left_items.append(item.split()[0])
        right_items.append(item.split()[1])

    total = [int(item) * right_items.count(item) for item in left_items]

    return sum(total)


if __name__ == "__main__":
    INPUT_FILE = Path("day1.input")
    with open(INPUT_FILE) as input_file:
        input_data = [line.strip() for line in input_file.readlines()]

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
