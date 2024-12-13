from aoc import get_input_data
from registry import register


@register(year=2024, day=1, part=1)
def solve_part1(context: dict) -> None:
    """Solve part 1 of day 1 (2023)."""
    input_data = get_input_data(context)

    # Example logic
    result = sum(int(x) for x in input_data.split())
    print(
        f"Year {context['year']}, Day {context['day']}, Part {context['part']} ({'sample' if context['use_sample'] else 'full'}): {result}"
    )


@register(year=2024, day=1, part=2)
def solve_part2(context: dict) -> None:
    """Solve part 2 of day 1 (2023)."""
    data = get_input_data(context)
    # Example logic
    result = max(int(x) for x in data.split())
    print(
        f"Year {context['year']}, Day {context['day']}, Part {context['part']} ({'sample' if context['use_sample'] else 'full'}): {result}"
    )
