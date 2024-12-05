# https://adventofcode.com/2015/day/15

import re
from itertools import combinations_with_replacement
from pathlib import Path
from typing import NamedTuple

INPUT_FILE = Path(__file__).resolve().parent / "day15.input"


class Ingredient(NamedTuple):
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def generate_combinations(ingredients, teaspoons, current_mix=[]):
    if len(current_mix) == len(ingredients) - 1:
        return [current_mix + [teaspoons - sum(current_mix)]]

    combinations = []
    for i in range(teaspoons - sum(current_mix) + 1):
        combinations += generate_combinations(ingredients, teaspoons, current_mix + [i])

    return combinations


def calculate_score(ingredients, combination):
    score = 1
    for i in range(len(next(iter(ingredients.values()))) - 1):  # Exclude calories
        prop_score = sum(
            ingredients[name][i] * amount
            for name, amount in zip(ingredients.keys(), combination)
        )
        score *= max(prop_score, 0)
    return score


def find_max_score(ingredients, total_teaspoons):
    max_score = 0
    for combination in generate_combinations(ingredients, total_teaspoons):
        max_score = max(max_score, calculate_score(ingredients, combination))
    return max_score


PATTERN = re.compile(
    r'.*: capacity ([-]?\d+), durability ([-]?\d+), flavor ([-]?\d+), texture ([-]?\d+), calories ([-]?\d+)'
)
with open(INPUT_FILE) as input_file:
    ingredients = []
    for line in input_file:
        if matched := PATTERN.match(line):
            # ingredients.append(Ingredient(*matched.groups()))
            ingredients.append([int(i) for i in matched.groups()][:4])

total_teaspoons = 100
best_score = find_max_score(ingredients, total_teaspoons)
print(f"The best score is: {best_score}")
