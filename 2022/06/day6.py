# https://adventofcode.com/2022/day/6

from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "day6.input"
with open(INPUT_FILE) as input_file:
    input_data = input_file.read().strip()

quest = {'1': 4, '2': 14}
for part, count in quest.items():
    marker = 0
    while marker < len(input_data):
        letters = list(input_data[marker : marker + count])

        if len(set(letters)) != count:
            marker += 1
            continue

        answer = marker + count
        break

    print(f'Part {part}: {answer}')
