# https://adventofcode.com/2015/day/3
from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "day3.input"
with open(INPUT_FILE) as input_file:
    input_data = input_file.read().strip()


def deliveries(players):
    houses = {(0, 0): 0}
    x = [0] * players
    y = [0] * players

    for c, move in enumerate(input_data):
        p = c % players
        x[p] += {'^': 0, 'v': 0, '>': 1, '<': -1}[move]

        y[p] += {'^': 1, 'v': -1, '>': 0, '<': 0}[move]

        houses[(x[p], y[p])] = houses.get((x[p], y[p]), 0) + 1

    return len(houses)


print('Part 1:', deliveries(1))
print('Part 2:', deliveries(2))
