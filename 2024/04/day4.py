# https://adventofcode.com/2022/day/4

from pathlib import Path


def find_word_in_direction(grid, word, start_r, start_c, dr, dc):
    rows, cols = len(grid), len(grid[0])
    return all(
        0 <= start_r + i * dr < rows
        and 0 <= start_c + i * dc < cols
        and grid[start_r + i * dr][start_c + i * dc] == word[i]
        for i in range(len(word))
    )


def part1(input_data) -> int:
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
    return sum(
        find_word_in_direction(input_data, word, r, c, dr, dc)
        for r in range(len(input_data))
        for c in range(len(input_data[0]))
        for dr, dc in directions
    )


def part2(input_data) -> int:
    return 0


if __name__ == "__main__":
    INPUT_FILE = Path(__file__).resolve().parent / "day4.input"
    with open(INPUT_FILE) as input_file:
        input_data = [line.strip() for line in input_file.readlines()]

    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
