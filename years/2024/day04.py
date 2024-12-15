# https://adventofcode.com/2022/day/4


from aoc import get_input_data
from registry import register


def find_word_in_direction(grid, word, start_r, start_c, dr, dc):
    rows, cols = len(grid), len(grid[0])
    return all(
        0 <= start_r + i * dr < rows
        and 0 <= start_c + i * dc < cols
        and grid[start_r + i * dr][start_c + i * dc] == word[i]
        for i in range(len(word))
    )


@register(year=2024, day=4, part=1)
def solve_part1(context: dict) -> None:
    input_data = get_input_data(context).splitlines()
    word = "XMAS"
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Diagonal Down-Right
        (1, -1),  # Diagonal Down-Left
        (-1, 1),  # Diagonal Up-Right
        (-1, -1),  # Diagonal Up-Left
    ]
    answer = sum(
        find_word_in_direction(input_data, word, r, c, dr, dc)
        for r in range(len(input_data))
        for c in range(len(input_data[0]))
        for dr, dc in directions
    )
    print(f"Part 1: {answer}")


@register(year=2024, day=4, part=2)
def solve_part2(context: dict) -> None:
    pass
