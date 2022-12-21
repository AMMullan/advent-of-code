import os

__location__ = os.path.realpath(
    os.path.join(
        os.getcwd(), os.path.dirname(__file__)
    )
)
with open(os.path.join(__location__, 'day6.input')) as input_file:
    input_data = input_file.read().strip()

quest = {
    '1': 4,
    '2': 14
}
for part, count in quest.items():
    marker = 0
    part1_answer = 0
    while marker < len(input_data):
        letters = list(input_data[marker:marker + count])

        if len(set(letters)) != count:
            marker += 1
            continue

        answer = marker + count
        break

    print(f'Part {part}: {answer}')
