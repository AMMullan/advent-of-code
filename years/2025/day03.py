from aoc import get_input_data
from registry import register


def largest_subsequence_number(s: str, k: int) -> int:
    stack: list[str] = []
    removals = len(s) - k

    for digit in s:
        while stack and removals > 0 and digit > stack[-1]:
            stack.pop()
            removals -= 1

        stack.append(digit)

    # Only keep first k digits
    return int(''.join(stack[:k]))


@register(year=2025, day=3, part=1)
def solve_part1(context: dict) -> int:
    input_data = get_input_data(context)
    output = 0

    for line in input_data.splitlines():
        output += largest_subsequence_number(line, 2)

    if context['use_sample']:
        assert output == 357, f'Received {output}'
    else:
        assert output == 17346, f'Received {output}'

    return output


@register(year=2025, day=3, part=2)
def solve_part2(context: dict) -> int:
    input_data = get_input_data(context)
    output = 0

    for line in input_data.splitlines():
        number = largest_subsequence_number(line, 12)
        print(number)
        output += number

    if context['use_sample']:
        assert output == 3121910778619, f'Received {output}'
    else:
        assert output == 172981362045136, f'Received {output}'

    return output
