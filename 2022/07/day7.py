from pathlib import Path

INPUT_FILE = Path(__file__).resolve().parent / "day7.input"
with open(INPUT_FILE) as input_file:
    input_data = [line.strip() for line in input_file.readlines()]

current_path = ''
tree = {}

for line in input_data:
    if line.startswith('$ cd'):
        folder = line.split()[-1]
        if folder.startswith('/'):
            current_path = folder

        elif folder == '..':
            current_path = current_path[: current_path.rindex('/')]

        else:
            current_path += current_path if current_path == '/' else f'/{current_path}'

        if current_path not in tree:
            tree[current_path] = []

    elif line[0].isdigit():
        tree[current_path].append(int(line.split()[0]))

tree_sum = {}
# Create sum for each directory
for key1 in tree:
    dir_total = 0
    for key2 in tree:
        if key2.startswith(key1):
            dir_total += sum(tree[key2])
    tree_sum[key1] = dir_total

print(tree_sum)
