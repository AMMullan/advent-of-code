# https://adventofcode.com/2015/day/6


from aoc import get_input_data
from registry import register


def transform_grid(grid, action, start_coords, end_coords):
    start_row, start_col = start_coords
    end_row, end_col = end_coords

    # Iterate over the rows and columns
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Check if the current element is within the specified range
            if start_row <= row <= end_row and start_col <= col <= end_col:
                match action:
                    case "on":
                        grid[row][col] = 1
                    case "off":
                        grid[row][col] = 0
                    case "toggle":
                        if grid[row][col] == 1:
                            grid[row][col] = 0
                        elif grid[row][col] == 0:
                            grid[row][col] = 1


def adjust_brightness(grid, action, start_coords, end_coords):
    start_row, start_col = start_coords
    end_row, end_col = end_coords

    # Iterate over the rows and columns
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Check if the current element is within the specified range
            if start_row <= row <= end_row and start_col <= col <= end_col:
                match action:
                    case "on":
                        grid[row][col] += 1
                    case "off":
                        if grid[row][col] > 0:
                            grid[row][col] -= 1
                    case "toggle":
                        grid[row][col] += 2


@register(year=2015, day=6, part=1, completed=True)
def solve_part1(context: dict) -> None:
    part1_grid = [[0 for _ in range(1000)] for _ in range(1000)]

    input_data = get_input_data(context).splitlines()

    for instruction in input_data:
        data = instruction.split()
        start_pair = [int(item) for item in data[-3].split(",")]
        end_pair = [int(item) for item in data[-1].split(",")]
        if instruction.startswith("turn on"):
            action = "on"
        elif instruction.startswith("turn off"):
            action = "off"
        elif instruction.startswith("toggle"):
            action = "toggle"

        transform_grid(part1_grid, action, start_pair, end_pair)

    part1_answer = sum(sum(row) for row in part1_grid)
    print(part1_answer)


@register(year=2015, day=6, part=2, completed=True)
def solve_part2(context: dict) -> None:
    part2_grid = [[0 for _ in range(1000)] for _ in range(1000)]

    input_data = get_input_data(context).splitlines()

    for instruction in input_data:
        data = instruction.split()
        start_pair = [int(item) for item in data[-3].split(",")]
        end_pair = [int(item) for item in data[-1].split(",")]
        if instruction.startswith("turn on"):
            action = "on"
        elif instruction.startswith("turn off"):
            action = "off"
        elif instruction.startswith("toggle"):
            action = "toggle"

        adjust_brightness(part2_grid, action, start_pair, end_pair)

    part2_answer = sum(sum(row) for row in part2_grid)
    print(part2_answer)
