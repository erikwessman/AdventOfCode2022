arr = []
with open('day10/input.txt', 'r') as f:
    arr = f.read().splitlines()

instruction_dict = {'noop': 1, 'addx': 2}
result = 0
cycle = 0
register = 1
counter = 1

for line in arr:
    instructions = line.split(' ')

    for _ in range(instruction_dict[instructions[0]]):
        cycle += 1
        if cycle == 20:
            result += cycle * register
        elif cycle > 20:
            if counter == 40:
                result += cycle * register
                counter = 1
            else:
                counter += 1

    if instructions[0] == 'noop':
        pass
    elif instructions[0] == 'addx':
        register += int(instructions[1])

print(result)