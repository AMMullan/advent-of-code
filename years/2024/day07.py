from aoc import get_input_data
from registry import register


def is_solvable_part1(target: int, numbers: list, current: int, index: int = 1) -> bool:
    # Base case: If we've used all numbers, check if the result matches the target
    if index == len(numbers):
        return current == target

    # Recursive case: Try applying both operators to the next number
    next_number = numbers[index]
    return is_solvable_part1(
        target, numbers, current + next_number, index + 1
    ) or is_solvable_part1(target, numbers, current * next_number, index + 1)


@register(year=2024, day=7, part=1, completed=True)
def solve_part1(context: dict) -> None:
    input_data = get_input_data(context).splitlines()

    total = 0
    for item in input_data:
        item_split = item.split(":")
        answer = int(item_split[0])
        nums = [int(num) for num in item_split[1].split()]

        if is_solvable_part1(answer, nums, nums[0]):
            total += answer

    print(total)
    if context["use_sample"]:
        assert total == 3749
    else:
        assert total == 1399219271639


@register(year=2024, day=7, part=2)
def solve_part2(context: dict) -> None:
    input_data = get_input_data(context).splitlines()

    total = 0

    print(total)
    if context["use_sample"]:
        assert total == 11387
