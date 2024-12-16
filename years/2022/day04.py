# https://adventofcode.com/2022/day/4


from aoc import get_input_data
from registry import register


def convert_range(input):
    return sum(
        (
            (
                list(range(*[int(b) + c for c, b in enumerate(a.split("-"))]))
                if "-" in a
                else [int(a)]
            )
            for a in input.split(", ")
        ),
        [],
    )


@register(year=2022, day=4, part=1, completed=True)
def solve_part1(context: dict) -> None:
    input_data = get_input_data(context).splitlines()
    part1_total = 0
    for item in input_data:
        pair1, pair2 = item.split(",")
        pair1 = convert_range(pair1)
        pair2 = convert_range(pair2)

        if all(item in pair2 for item in pair1) or all(item in pair1 for item in pair2):
            part1_total += 1

    print(f"Part 1: {part1_total}")


@register(year=2022, day=4, part=2, completed=True)
def solve_part2(context: dict) -> None:
    input_data = get_input_data(context).splitlines()

    part2_total = 0
    for item in input_data:
        pair1, pair2 = item.split(",")
        pair1 = convert_range(pair1)
        pair2 = convert_range(pair2)

        if any(item in pair2 for item in pair1) or any(item in pair1 for item in pair2):
            part2_total += 1

    print(f"Part 2: {part2_total}")
