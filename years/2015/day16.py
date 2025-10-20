from aoc import get_input_data
from registry import register

TICKER_TAPE = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


def parse_input(input_data: str) -> list[dict[str, int]]:
    return [
        {
            attr: int(val)
            for group in line.split(': ', 1)[1].split(', ')
            for attr, val in [group.split(': ')]
        }
        for line in input_data.splitlines()
    ]


@register(year=2015, day=16, part=1, completed=True)
def solve_part1(context: dict) -> int | None:
    input_data = get_input_data(context)

    correct_sue = next(
        (
            idx
            for idx, sue in enumerate(parse_input(input_data), start=1)
            if all(
                sue.get(attr) is None or sue[attr] == val
                for attr, val in TICKER_TAPE.items()
            )
        ),
        None,
    )
    assert correct_sue == 40
    return correct_sue


@register(year=2015, day=16, part=2, completed=True)
def solve_part2(context: dict) -> int:
    input_data = get_input_data(context)

    def could_match(aunt):
        for k, v in aunt.items():
            if k in ['cats', 'trees']:
                if TICKER_TAPE[k] >= v:
                    return False
            elif k in ['pomeranians', 'goldfish']:
                if TICKER_TAPE[k] <= v:
                    return False
            else:
                if TICKER_TAPE[k] != v:
                    return False
        return True

    correct_sue = next(
        (
            idx
            for idx, sue in enumerate(parse_input(input_data), start=1)
            if could_match(sue)
        ),
        None,
    )

    assert correct_sue == 241
    return correct_sue
