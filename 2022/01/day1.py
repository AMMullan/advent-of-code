# https://adventofcode.com/2022/day/1

from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "day1.input"
with open(INPUT_FILE) as input_file:
    input_data = [line.strip() for line in input_file.readlines()] + [
        ''
    ]  # Ensure there's a last empty line

most_calories = 0
top_3 = []

current_elf_calories = 0
for item in input_data:
    if not item:
        if len(top_3) != 3:
            top_3.append(current_elf_calories)
        elif any(current_elf_calories > item for item in top_3):
            top_3.remove(min(top_3))
            top_3.append(current_elf_calories)

        if current_elf_calories > most_calories:
            most_calories = current_elf_calories

        current_elf_calories = 0
    else:
        current_elf_calories += int(item)

print(f'Part 1: {most_calories}')
print(f'Part 2: {sum(top_3)}')
