# https://adventofcode.com/2015/day/11

import string

from registry import register


def split_string(seq, n):
    return ["".join(item) for item in zip(*[seq[n:] for n in range(n)])]


STRAIGHTS = split_string(string.ascii_lowercase, 3)


def is_valid_puzzle(puzzle_input: str) -> bool:
    if set(puzzle_input) & {"i", "o", "l"}:
        return False

    if all(item not in STRAIGHTS for item in split_string(puzzle_input, 3)):
        return False

    pair_count = set()
    for item in split_string(puzzle_input, 2):
        if len(set(item)) == 1 and set(item) not in pair_count:
            pair_count.add(item[0])

    return len(pair_count) >= 2


def get_next_password_iteration(s):
    if not s:
        return "a"

    s = list(s)
    i = len(s) - 1

    while i >= 0:
        if s[i] == "z":
            s[i] = "a"
            i -= 1
        else:
            s[i] = chr(ord(s[i]) + 1)
            return "".join(s)

    return "a" + "".join(s)


def get_next_password(puzzle_input: str):
    current_password = puzzle_input
    while True:
        current_password = get_next_password_iteration(current_password)
        if is_valid_puzzle(current_password):
            return current_password


@register(year=2015, day=11, part=1)  # type: ignore
def solve_part1(context: dict) -> str:
    part1 = get_next_password("cqjxjnds")

    if context:
        print(part1)

    return part1


@register(year=2015, day=11, part=2)
def solve_part2(context: dict) -> None:
    if part1 := solve_part1({}):
        part2 = get_next_password(part1)
        print(part2)
