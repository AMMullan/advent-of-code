# https://adventofcode.com/2015/day/5
import os


def has_subsequent_doubles(input_string):
    for i in range(len(input_string) - 1):
        if input_string[i] == input_string[i + 1]:
            return True
    return False


def has_forbidden(input_string):
    return any(
        bs in input_string
        for bs in [
            'ab',
            'cd',
            'pq',
            'xy'
        ]
    )


__location__ = os.path.realpath(
    os.path.join(
        os.getcwd(), os.path.dirname(__file__)
    )
)
with open(os.path.join(__location__, 'day5.input')) as input_file:
    input_data = [
        line.strip()
        for line in input_file.readlines()
    ]

day1_items = 0
for input_item in input_data:
    vowel_count = sum(
        1
        for vowel in input_item
        if vowel in 'aeiou'
    )

    # Ignore words without at least 3 vowels
    if vowel_count < 3:
        continue

    # Ignore if has no doubles
    if not has_subsequent_doubles(input_item):
        continue

    # Ignore words with specific strings
    if has_forbidden(input_item):
        continue

    day1_items += 1

print('Part 1:', day1_items)
