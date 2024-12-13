# https://adventofcode.com/2015/day/7

from dataclasses import dataclass

from aoc import get_input_data
from registry import register

GATES = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]


def get_wire_detail(instruction):
    inputs = [int(i) if i.isdigit() else i for i in instruction[:-2] if i not in GATES]

    gate = next(
        (gate_keyword for gate_keyword in GATES if gate_keyword in instruction),
        "ASSIGN",
    )

    return inputs, gate


def evaluate_wire(gate, inputs):
    try:
        match gate:
            case "ASSIGN":
                return int(inputs[0])
            case "NOT":
                return int(65535 - inputs[0])
            case "OR":
                return int(inputs[0] | inputs[1])
            case "AND":
                return int(inputs[0] & inputs[1])
            case "LSHIFT":
                return int(inputs[0] << inputs[1])
            case "RSHIFT":
                return int(inputs[0] >> inputs[1])
            case _:
                raise ValueError(f"Invalid Gate: {gate}")
    except TypeError as e:
        raise ValueError from e


@dataclass
class Wire:
    id_: str
    inputs: list
    gate: str
    signal: int | None


def solve_puzzle(input_data: list, wire_a_signal=None) -> int:
    wires = {
        wire[-1]: Wire(wire[-1], *get_wire_detail(wire), None) for wire in input_data
    }
    if wire_a_signal is not None:
        wires["b"].signal = wire_a_signal

    while any(wire.signal is None for wire in wires.values()):
        for wire in wires.values():
            if wire.signal is not None:
                continue

            try:
                input_signals = [
                    wires[input_].signal if isinstance(input_, str) else input_
                    for input_ in wire.inputs
                ]
            except KeyError:
                continue

            if None not in input_signals:
                try:
                    wire.signal = evaluate_wire(wire.gate, input_signals)
                except ValueError:
                    continue

    return wires["a"].signal


@register(year=2015, day=7, part=1)
def solve_part1(context: dict) -> None:
    input_data = [line.strip().split() for line in get_input_data(context).splitlines()]

    part1_answer = solve_puzzle(input_data)
    print(f"{part1_answer=}")  # 3176


@register(year=2015, day=7, part=2)
def solve_part2(context: dict) -> None:
    input_data = [line.strip().split() for line in get_input_data(context).splitlines()]

    part1_answer = solve_puzzle(input_data)
    part2_answer = solve_puzzle(input_data, part1_answer)
    print(f"{part2_answer=}")  # 14710
