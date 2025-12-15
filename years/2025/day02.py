from aoc import get_input_data
from registry import register


def all_repeating_patterns(value: int) -> list[tuple[str, int]]:
    s = str(value)
    n = len(s)

    lps = [0] * n
    j = 0

    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = lps[j - 1]
        if s[i] == s[j]:
            j += 1
            lps[i] = j

    base_period = n - lps[-1]

    # No repetition at all
    if base_period == n:
        return []

    patterns: list[tuple[str, int]] = []

    period = base_period
    while period <= n:
        if n % period == 0:
            patterns.append((s[:period], n // period))
        period += base_period

    return patterns


@register(year=2025, day=2, part=1, completed=True)
def solve_part1(context: dict) -> int:
    input_data = get_input_data(context)

    input_elements = input_elements = [
        list(map(int, items.split('-'))) for items in input_data.split(',')
    ]
    total = 0
    for group in input_elements:
        start, end = group
        numbers = list(range(start, end + 1))
        for number in numbers:
            patterns = all_repeating_patterns(number)
            if not patterns:
                continue

            if any(pattern[1] == 2 for pattern in patterns):
                total += number

    if context['use_sample']:
        assert total == 1227775554
    else:
        assert total == 31000881061

    return total


@register(year=2025, day=2, part=2, completed=True)
def solve_part2(context: dict) -> int:
    input_data = get_input_data(context)

    input_elements = input_elements = [
        list(map(int, items.split('-'))) for items in input_data.split(',')
    ]
    total = 0
    for group in input_elements:
        start, end = group
        numbers = list(range(start, end + 1))
        for number in numbers:
            patterns = all_repeating_patterns(number)
            if not patterns:
                continue

            if any(pattern[1] >= 2 for pattern in patterns):
                total += number

    if context['use_sample']:
        assert total == 4174379265
    else:
        assert total == 46769308485

    return total
