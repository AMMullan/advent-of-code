# https://adventofcode.com/2022/day/5


from aoc import get_input_data
from registry import register


def parse_rules(input_data: list[str]) -> list[list[int]]:
    return [[int(i) for i in item.split("|")] for item in input_data if "|" in item]


def parse_pages(input_data: list[str]) -> list[list[int]]:
    return [[int(i) for i in item.split(",")] for item in input_data if "," in item]


def passes_rules(page: list[int], rules) -> bool:
    return not any(
        (
            rule[0] in page
            and rule[1] in page
            and page.index(rule[0]) > page.index(rule[1])
        )
        for rule in rules
    )


@register(year=2024, day=5, part=1, completed=True)
def solve_part1(context: dict) -> int:
    input_data = get_input_data(context).splitlines()

    rules = parse_rules(input_data)
    pages = parse_pages(input_data)

    answer = sum(page[len(page) // 2] for page in pages if passes_rules(page, rules))

    if context["use_sample"]:
        assert answer == 143
    else:
        assert answer == 5747

    return answer


@register(year=2024, day=5, part=2)
def solve_part2(context: dict) -> int:
    input_data = get_input_data(context).splitlines()

    rules = parse_rules(input_data)
    pages = parse_pages(input_data)

    total = 0

    for page in pages:
        if passes_rules(page, rules):
            continue

        for rule in rules:
            if rule[0] not in page or rule[1] not in page:
                continue

            r1 = page.index(rule[0])
            r2 = page.index(rule[1])

            if r1 > r2:
                page.pop(r2)
                page.insert(r1, rule[1])

        total += page[len(page) // 2]

    if context["use_sample"]:
        assert total == 123
    else:
        assert total < 5990 and total != 5433

    return total
