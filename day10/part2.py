import numpy as np

arr = []
with open('day10/input.txt', 'r') as f:
    arr = f.read().splitlines()

result = np.zeros(shape=(6,40)).astype(int).tolist()
instruction_dict = {'noop': 1, 'addx': 2}
cycle = 0
register = 1
x = 0
y = 0

for line in arr:
    instructions = line.split(' ')

    for _ in range(instruction_dict[instructions[0]]):
        sprite_positions = [register-1, register, register+1]

        if x in sprite_positions:
            result[y][x] = '#'
        else:
            result[y][x] = '.'

        cycle += 1
        x += 1

        if cycle % 40 == 0 and cycle != 0:
            y += 1
            x = 0

    if instructions[0] == 'noop':
        pass
    elif instructions[0] == 'addx':
        register += int(instructions[1])

r = ''

for l in result:
    r += ''.join(l)
    r += '\n'

print(r)