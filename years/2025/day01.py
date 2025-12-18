# https://adventofcode.com/2025/day/1

from dataclasses import dataclass
from enum import Enum

from aoc import get_input_data
from registry import register


class RotationDirection(Enum):
    LEFT = 'L'
    RIGHT = 'R'


@dataclass
class Rotation:
    direction: RotationDirection
    value: int
    rotation_value: int = 0

    def __post_init__(self):
        if self.direction == RotationDirection.LEFT:
            self.rotation_value = -self.value
        elif self.direction == RotationDirection.RIGHT:
            self.rotation_value = self.value


@register(year=2025, day=1, part=1, completed=True)
def solve_part1(context: dict) -> int:
    input_data = get_input_data(context)

    instructions: list[Rotation] = [
        Rotation(
            RotationDirection.LEFT if item[0] == 'L' else RotationDirection.RIGHT,
            int(item[1:]),
        )
        for item in input_data.splitlines()
    ]

    current_value = 50
    zero_count = 0
    for rotation in instructions:
        current_value = (current_value + rotation.rotation_value) % 100

        if current_value == 0:
            zero_count += 1

    if context['use_sample']:
        assert zero_count == 3
    else:
        assert zero_count == 1092

    return zero_count


@register(year=2025, day=1, part=2)
def solve_part2(context: dict) -> int:
    def rotate_with_wraps(start: int, offset: int, n: int) -> tuple[int, int]:
        """Return (final_position, number_of_wraps)."""
        final_position = (start + offset) % n

        # Count complete wraps
        wraps = abs(offset) // n

        # Check if we crossed 0 in the partial wrap
        if wraps == 0:
            if offset > 0 and final_position < start:
                wraps = 1
            elif offset < 0 and final_position > start:
                wraps = 1
            elif offset < 0 and start == 0 and final_position != 0:
                wraps = 1

        return final_position, wraps

    input_data = get_input_data(context)

    instructions: list[Rotation] = [
        Rotation(
            RotationDirection.LEFT if item[0] == 'L' else RotationDirection.RIGHT,
            int(item[1:]),
        )
        for item in input_data.splitlines()
    ]

    current_value = 50
    zero_count = 0
    for rotation in instructions:
        new_value, wraps = rotate_with_wraps(
            current_value, rotation.rotation_value, 100
        )

        zero_count += wraps
        current_value = new_value

    if context['use_sample']:
        assert zero_count == 6, zero_count
    else:
        assert zero_count > 2385 and zero_count < 27684 and zero_count != 6160, (
            zero_count
        )
    return zero_count
