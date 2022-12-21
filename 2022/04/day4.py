import os


def convert_range(input):
    return sum(
        (
            (
                list(
                    range(
                        *[
                            int(b) + c
                            for c, b in enumerate(a.split('-'))
                        ]
                    )
                )
                if '-' in a else [int(a)]
            )
            for a in input.split(', ')
        ), []
    )


__location__ = os.path.realpath(
    os.path.join(
        os.getcwd(), os.path.dirname(__file__)
    )
)
with open(os.path.join(__location__, 'day4.input')) as input_file:
    input_data = [
        line.strip()
        for line in input_file.readlines()
    ]

part1_total = 0
part2_total = 0
for item in input_data:
    pair1, pair2 = item.split(',')
    pair1 = convert_range(pair1)
    pair2 = convert_range(pair2)

    if (
        all(item in pair2 for item in pair1) or
        all(item in pair1 for item in pair2)
    ):
        part1_total += 1

    if (
        any(item in pair2 for item in pair1) or
        any(item in pair1 for item in pair2)
    ):
        part2_total += 1

print(f'Part 1: {part1_total}')
print(f'Part 2: {part2_total}')
