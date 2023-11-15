from collections import deque
from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "day5.input"
with open(INPUT_FILE) as input_file:
    input_data = [line.strip() for line in input_file.readlines()][10:]

for part in ['1', '2']:
    cargo = [
        deque(['H', 'L', 'R', 'F', 'B', 'C', 'J', 'M']),
        deque(['D', 'C', 'Z']),
        deque(['W', 'G', 'N', 'C', 'F', 'J', 'H']),
        deque(['B', 'S', 'T', 'M', 'D', 'J', 'P']),
        deque(['J', 'R', 'D', 'C', 'N']),
        deque(['Z', 'G', 'J', 'P', 'Q', 'D', 'L', 'W']),
        deque(['H', 'R', 'F', 'T', 'Z', 'P']),
        deque(['G', 'M', 'V', 'L']),
        deque(['J', 'R', 'Q', 'F', 'P', 'G', 'B', 'C']),
    ]

    for instruction in input_data:
        instructions = instruction.split()
        count = int(instructions[1])
        origin = int(instructions[3]) - 1
        target = int(instructions[5]) - 1

        if part == '1':
            while count:
                count -= 1
                removed = cargo[origin].popleft()
                cargo[target].appendleft(removed)
        elif part == '2':
            move_items = list(cargo[origin])[:count]
            while count:
                count -= 1
                cargo[origin].popleft()
                cargo[target].appendleft(move_items[count])

    answer = ''.join(item[0] for item in cargo)
    print(f'Part {part}: {answer}')
