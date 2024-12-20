# https://adventofcode.com/2022/day/2

import re

from aoc import get_input_data
from registry import register


def translate(round):
    first, second = round
    first = re.sub(r"[A|X]", "Rock", first)
    first = re.sub(r"[B|Y]", "Paper", first)
    first = re.sub(r"[C|Z]", "Scissors", first)

    second = re.sub(r"[A|X]", "Rock", second)
    second = re.sub(r"[B|Y]", "Paper", second)
    second = re.sub(r"[C|Z]", "Scissors", second)

    return [first, second]


def get_round_winner(input_data) -> tuple:
    points = {"Rock": 1, "Paper": 2, "Scissors": 3}
    win_map = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
    lose_map = {v: k for k, v in win_map.items()}

    part1_total = 0
    part2_total = 0
    for round in input_data:
        opponent, me = translate(round)
        part2_result = round[1]

        # Part 1 scoring
        part1_total += points[me]
        part1_total += 3 if opponent == me else (6 if win_map[me] == opponent else 0)

        # Part 2 scoring
        if part2_result == "X":  # Lose
            part2_total += points[win_map[opponent]]
        elif part2_result == "Y":  # Draw
            part2_total += 3 + points[opponent]
        else:  # Win
            part2_total += 6 + points[lose_map[opponent]]

    return (part1_total, part2_total)


@register(year=2022, day=2, part=1, completed=True)
def solve_part1(context: dict) -> int:
    input_data = [line.split() for line in get_input_data(context).splitlines()]
    return get_round_winner(input_data)[0]


@register(year=2022, day=2, part=2, completed=True)
def solve_part2(context: dict) -> int:
    input_data = [line.split() for line in get_input_data(context).splitlines()]
    return get_round_winner(input_data)[1]
