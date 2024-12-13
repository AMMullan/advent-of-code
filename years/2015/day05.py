# https://adventofcode.com/2015/day/5

from aoc import get_input_data
from registry import register


@register(year=2015, day=5, part=1)
def solve_part1(context: dict) -> None:
    input_data = get_input_data(context).splitlines()

    def has_subsequent_doubles(input_string):
        return any(
            input_string[i] == input_string[i + 1] for i in range(len(input_string) - 1)
        )

    def has_forbidden(input_string):
        return any(bs in input_string for bs in ["ab", "cd", "pq", "xy"])

    part1_answer = 0
    for input_item in input_data:
        # Ignore words without at least 3 vowels
        if sum(vowel in "aeiou" for vowel in input_item) < 3:
            continue

        # Ignore if has no doubles
        if not has_subsequent_doubles(input_item):
            continue

        # Ignore words with specific strings
        if has_forbidden(input_item):
            continue

        part1_answer += 1

    print("Part 1:", part1_answer)


@register(year=2015, day=5, part=2)
def solve_part2(context: dict) -> None:
    input_data = get_input_data(context).splitlines()

    def has_non_overlapping_repeats(input_string):
        pairs = [input_string[i : i + 2] for i in range(len(input_string) - 1)]
        seen = set()

        for i, pair in enumerate(pairs):
            if pair in seen:
                # Ensure the found repeat is not overlapping
                previous_index = pairs.index(pair)
                if i - previous_index > 1:
                    return True
            else:
                seen.add(pair)

        return False

    part2_answer = 0
    for input_item in input_data:
        if not has_non_overlapping_repeats(input_item):
            continue

        thruples = [
            [input_item[i], input_item[i + 1], input_item[i + 2]]
            for i in range(len(input_item) - 2)
        ]

        nice = any(item[0] == item[2] for item in thruples)
        if nice:
            part2_answer += 1

    print("Part 1:", part2_answer)
