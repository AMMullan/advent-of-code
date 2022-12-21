# https://adventofcode.com/2015/day/4

import hashlib

input_data = 'ckczppom'


def get_stuffer(zero_count=5):
    current_num = 0
    while True:
        result = hashlib.md5(f'{input_data}{str(current_num)}'.encode())
        hex = result.hexdigest()

        if hex.startswith('0' * zero_count):
            return current_num

        current_num += 1


print('Part 1:', get_stuffer(5))
print('Part 2:', get_stuffer(6))
