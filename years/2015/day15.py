from dataclasses import dataclass
from itertools import combinations

from aoc import get_input_data
from registry import register


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def generate_combinations(items: list[str], total: int = 100) -> list[dict[str, int]]:
    """
    Generate all combinations of integer assignments to `items` that sum to `total`.
    Each item receives at least 1.
    """
    n = len(items)
    if n == 0:
        return []
    if total < n:
        raise ValueError(
            'Total must be >= number of items (since each gets at least 1).'
        )

    # Split total-1 into n-1 "bars" to get all compositions
    results = []
    for dividers in combinations(range(1, total), n - 1):
        parts = [b - a for a, b in zip((0, *dividers), (*dividers, total))]
        results.append(dict(zip(items, parts)))
    return results


def parse_ingredients(input_data: str) -> list[Ingredient]:
    ingredients = []

    for line in input_data.splitlines():
        line_split = line.split(': ')
        name = line_split[0]

        part_dict = {
            part[0]: int(part[1])
            for part in (
                item.split()
                for item in [item.strip() for item in line_split[1].split(', ')]
            )
        }

        ingredients.append(
            Ingredient(
                name,
                part_dict['capacity'],
                part_dict['durability'],
                part_dict['flavor'],
                part_dict['texture'],
                part_dict['calories'],
            )
        )

    return ingredients


def get_ingredient_totals(
    ingredients: dict[str, Ingredient], combination: dict[str, int]
) -> dict[str, int] | None:
    totals = {
        'capacity': 0,
        'durability': 0,
        'flavor': 0,
        'texture': 0,
        'calories': 0,
    }
    for name, amount in combination.items():
        ingredient = ingredients[name]
        totals['capacity'] += ingredient.capacity * amount
        totals['durability'] += ingredient.durability * amount
        totals['flavor'] += ingredient.flavor * amount
        totals['texture'] += ingredient.texture * amount
        totals['calories'] += ingredient.calories * amount

    return None if any(part <= 0 for part in totals.values()) else totals


@register(year=2015, day=15, part=1, completed=True)
def solve_part1(context: dict) -> int:
    input_data = get_input_data(context)

    ingredients = {
        ingredient.name: ingredient for ingredient in parse_ingredients(input_data)
    }
    combinations = generate_combinations([str(k) for k in ingredients], 100)

    highest_score = 0
    for combination in combinations:
        ingredient_totals = get_ingredient_totals(ingredients, combination)

        if not ingredient_totals:
            continue

        ingredient_multiplied = (
            ingredient_totals['capacity']
            * ingredient_totals['durability']
            * ingredient_totals['flavor']
            * ingredient_totals['texture']
        )
        if ingredient_multiplied > highest_score:
            highest_score = ingredient_multiplied

    if context['use_sample']:
        assert highest_score == 62842880
    else:
        assert highest_score == 21367368

    return highest_score


@register(year=2015, day=15, part=2, completed=True)
def solve_part2(context: dict) -> int:
    input_data = get_input_data(context)

    ingredients = {
        ingredient.name: ingredient for ingredient in parse_ingredients(input_data)
    }
    combinations = generate_combinations([str(k) for k in ingredients], 100)

    highest_score = 0
    for combination in combinations:
        ingredient_totals = get_ingredient_totals(ingredients, combination)

        if not ingredient_totals:
            continue

        if ingredient_totals['calories'] != 500:
            continue

        ingredient_multiplied = (
            ingredient_totals['capacity']
            * ingredient_totals['durability']
            * ingredient_totals['flavor']
            * ingredient_totals['texture']
        )
        if ingredient_multiplied > highest_score:
            highest_score = ingredient_multiplied

        if ingredient_multiplied > highest_score:
            highest_score = ingredient_multiplied

    if context['use_sample']:
        assert highest_score == 57600000
    else:
        assert highest_score == 1766400

    return highest_score
