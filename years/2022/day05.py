from collections import deque
from copy import deepcopy

from aoc import get_input_data
from registry import register

CARGO = [
    deque(["H", "L", "R", "F", "B", "C", "J", "M"]),
    deque(["D", "C", "Z"]),
    deque(["W", "G", "N", "C", "F", "J", "H"]),
    deque(["B", "S", "T", "M", "D", "J", "P"]),
    deque(["J", "R", "D", "C", "N"]),
    deque(["Z", "G", "J", "P", "Q", "D", "L", "W"]),
    deque(["H", "R", "F", "T", "Z", "P"]),
    deque(["G", "M", "V", "L"]),
    deque(["J", "R", "Q", "F", "P", "G", "B", "C"]),
]


@register(year=2022, day=5, part=1, completed=True)
def solve_part1(context: dict) -> str:
    input_data = get_input_data(context).splitlines()[10:]
    cargo = deepcopy(CARGO)

    for instruction in input_data:
        instructions = instruction.split()
        count = int(instructions[1])
        origin = int(instructions[3]) - 1
        target = int(instructions[5]) - 1

        while count:
            count -= 1
            removed = cargo[origin].popleft()
            cargo[target].appendleft(removed)

    return "".join(item[0] for item in cargo)


@register(year=2022, day=5, part=2, completed=True)
def solve_part2(context: dict) -> str:
    input_data = get_input_data(context).splitlines()[10:]
    cargo = deepcopy(CARGO)

    for instruction in input_data:
        instructions = instruction.split()
        count = int(instructions[1])
        origin = int(instructions[3]) - 1
        target = int(instructions[5]) - 1

        move_items = list(cargo[origin])[:count]
        while count:
            count -= 1
            cargo[origin].popleft()
            cargo[target].appendleft(move_items[count])

    return "".join(item[0] for item in cargo)
