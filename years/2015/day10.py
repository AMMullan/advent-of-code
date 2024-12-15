# https://adventofcode.com/2015/day/10

from registry import register


def next_sequence(number):
    result = []
    i = 0
    while i < len(number):
        count = 1
        while i + 1 < len(number) and number[i] == number[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + number[i])
        i += 1
    return "".join(result)


def look_and_say(count: int, start: int):
    result = [str(start)] if start else ["1"]
    result.extend(next_sequence(result[-1]) for _ in range(count))
    return result


@register(year=2015, day=10, part=1)
def solve_part1(context: dict) -> None:
    part1_sequences = look_and_say(40, start=1113222113)
    print(len(part1_sequences[-1]))


@register(year=2015, day=10, part=2)
def solve_part2(context: dict) -> None:
    part2_sequences = look_and_say(50, start=1113222113)
    print(len(part2_sequences[-1]))