# https://adventofcode.com/2022/day/1


from aoc import get_input_data
from registry import register


@register(year=2022, day=1, part=1, completed=True)
def solve_part1(context: dict) -> None:
    input_data = get_input_data(context).splitlines()

    most_calories = 0

    current_elf_calories = 0
    for item in input_data:
        if not item:
            if current_elf_calories > most_calories:
                most_calories = current_elf_calories

            current_elf_calories = 0
        else:
            current_elf_calories += int(item)

    print(f"Part 1: {most_calories}")


@register(year=2022, day=1, part=2, completed=True)
def solve_part2(context: dict) -> None:
    input_data = get_input_data(context).splitlines()

    top_3 = []

    current_elf_calories = 0
    for item in input_data:
        if not item:
            if len(top_3) != 3:
                top_3.append(current_elf_calories)
            elif any(current_elf_calories > item for item in top_3):
                top_3.remove(min(top_3))
                top_3.append(current_elf_calories)

            current_elf_calories = 0
        else:
            current_elf_calories += int(item)

    print(f"Part 2: {sum(top_3)}")
