# https://adventofcode.com/2015/day/10


def next_sequence(number):
    result = []
    i = 0
    while i < len(number):
        count = 1
        while i + 1 < len(number) and number[i] == number[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + number[i])
        i += 1
    return ''.join(result)


def look_and_say(count: int, start: int | str = None):
    result = [str(start)] if start else ["1"]
    result.extend(next_sequence(result[-1]) for _ in range(count))
    return result


# Get the first 5 sequences of the Look-and-say sequence
part1_sequences = look_and_say(40, start=1113222113)
part2_sequences = look_and_say(50, start=1113222113)
print(len(part1_sequences[-1]))
print(len(part2_sequences[-1]))
