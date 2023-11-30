# https://adventofcode.com/2015/day/9

from itertools import permutations
from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "day9.input"
with open(INPUT_FILE) as input_file:
    input_data = [line.strip() for line in input_file.readlines()]

paths = []
for item in input_data:
    broken = item.split()
    paths.append([sorted((broken[0], broken[2])), int(broken[4])])

flight_paths = {loc for path in paths for loc in path[0]}

shortest = float('inf')
longest = 0
for flight in permutations(flight_paths):
    flight_total = sum(
        path[1]
        for path in paths
        for start, end in zip(flight, flight[1:])
        if path[0] == sorted([start, end])
    )
    shortest = min(shortest, flight_total)
    longest = max(longest, flight_total)

print(shortest)
print(longest)
