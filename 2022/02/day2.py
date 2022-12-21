import os
import re

__location__ = os.path.realpath(
    os.path.join(
        os.getcwd(), os.path.dirname(__file__)
    )
)
with open(os.path.join(__location__, 'day2.input')) as input_file:
    input_data = [
        line.strip().split()
        for line in input_file.readlines()
    ]


def translate(round):
    first, second = round
    first = re.sub(r'[A|X]', 'Rock', first)
    first = re.sub(r'[B|Y]', 'Paper', first)
    first = re.sub(r'[C|Z]', 'Scissors', first)

    second = re.sub(r'[A|X]', 'Rock', second)
    second = re.sub(r'[B|Y]', 'Paper', second)
    second = re.sub(r'[C|Z]', 'Scissors', second)

    return [first, second]


points = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

part1_total = 0
part2_total = 0
for round in input_data:
    opponent, me = translate(round)
    part2_result = round[1]

    part1_total += points[me]
    # Draw
    if opponent == me:
        part1_total += 3

    # I Win!
    elif (
        (me == 'Rock' and opponent == 'Scissors') or
        (me == 'Scissors' and opponent == 'Paper') or
        (me == 'Paper' and opponent == 'Rock')
    ):
        part1_total += 6

    # I Lose
    if part2_result == 'X':
        if opponent == 'Rock':
            part2_total += points['Scissors']
        elif opponent == 'Paper':
            part2_total += points['Rock']
        else:
            part2_total += points['Paper']

    # Draw
    elif part2_result == 'Y':
        part2_total += 3
        part2_total += points[opponent]

    # I Win
    elif part2_result == 'Z':
        part2_total += 6

        if opponent == 'Rock':
            part2_total += points['Paper']
        elif opponent == 'Paper':
            part2_total += points['Scissors']
        else:
            part2_total += points['Rock']

print(f'Part 1: {part1_total}')
print(f'Part 2: {part2_total}')
