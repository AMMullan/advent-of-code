# https://adventofcode.com/2015/day/14

from typing import NamedTuple

from aoc import get_input_data
from registry import register

END_TIME = 2503


class Reindeer(NamedTuple):
    name: str
    speed: int
    duration: int
    rest: int


def calculate_reindeer_speed(reindeers: list[Reindeer]) -> int:
    fastest = 0
    for reindeer in reindeers:
        cycle_time = reindeer.duration + reindeer.rest
        complete_cycles, remaining_time = divmod(END_TIME, cycle_time)
        total_distance = complete_cycles * reindeer.duration * reindeer.speed
        total_distance += min(remaining_time, reindeer.duration) * reindeer.speed

        fastest = max(fastest, total_distance)
    return fastest


def calculate_reindeer_points(reindeers: list[Reindeer]) -> int:
    """
    Calculate the maximum points a reindeer can earn based on speed, duration, and rest.
    """

    def calculate_distance(reindeer: Reindeer, time: int) -> int:
        cycle_time = reindeer.duration + reindeer.rest
        full_cycles = time // cycle_time
        remaining_time = min(reindeer.duration, time % cycle_time)
        return reindeer.speed * (full_cycles * reindeer.duration + remaining_time)

    scores = [0] * len(reindeers)
    for sec in range(1, END_TIME + 1):
        distances = [calculate_distance(r, sec) for r in reindeers]
        max_distance = max(distances)
        for i, distance in enumerate(distances):
            if distance == max_distance:
                scores[i] += 1

    return max(scores)


@register(year=2015, day=14, part=1, completed=True)
def solve_part1(context: dict) -> int:
    input_data = [line.split() for line in get_input_data(context).splitlines()]

    reindeers = [
        Reindeer(reindeer[0], int(reindeer[3]), int(reindeer[6]), int(reindeer[-2]))
        for reindeer in input_data
    ]
    return calculate_reindeer_speed(reindeers)


@register(year=2015, day=14, part=2, completed=True)
def solve_part2(context: dict) -> int:
    input_data = [line.split() for line in get_input_data(context).splitlines()]

    reindeers = [
        Reindeer(reindeer[0], int(reindeer[3]), int(reindeer[6]), int(reindeer[-2]))
        for reindeer in input_data
    ]

    return calculate_reindeer_points(reindeers)
