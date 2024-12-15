# https://adventofcode.com/2022/day/5


from aoc import get_input_data
from registry import register


def passes_rules(page: list[int], rules) -> bool:
    return not any(
        (
            rule[0] in page
            and rule[1] in page
            and page.index(rule[0]) > page.index(rule[1])
        )
        for rule in rules
    )


@register(year=2024, day=5, part=1)
def solve_part1(context: dict) -> None:
    input_data = get_input_data(context).splitlines()

    rules = [[int(i) for i in item.split("|")] for item in input_data if "|" in item]
    pages = [[int(i) for i in item.split(",")] for item in input_data if "," in item]

    answer = sum(page[len(page) // 2] for page in pages if passes_rules(page, rules))

    assert answer == 5747
    print(f"Part 1: {answer}")


@register(year=2024, day=5, part=2)
def solve_part2(context: dict) -> None:
    input_data = get_input_data(context).splitlines()

    rules = [[int(i) for i in item.split("|")] for item in input_data if "|" in item]
    pages = [[int(i) for i in item.split(",")] for item in input_data if "," in item]

    total = 0

    for page in pages:
        if passes_rules(page, rules):
            continue

        for rule in rules:
            if rule[0] not in page or rule[1] not in page:
                continue

            r1 = page.index(rule[0])
            r2 = page.index(rule[1])

            if r1 >= r2:
                page.pop(r2)
                page.insert(r1, rule[1])

        total += page[len(page) // 2]

    assert total == 5184
    print(f"Part 2: {total}")
