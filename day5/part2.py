arr = []
with open('day5/input.txt', 'r') as f:
    arr = f.read().splitlines()

# separate input into crates and instructions
crates_input = []
instructions_input = []
for i, line in enumerate(arr):
    if line == '':
        crates_input = arr[0:i-1]
        instructions_input = arr[i+1::]
        break

# split crates from whitepaces
crates_arr = []
for line in crates_input:
    temp = []
    for i in range(0, len(line), 4):
        temp.append(line[i:i+3])
    crates_arr.append(temp)

# arrange crates into proper stacks
crates = []
for x in range(len(crates_arr[0])):
    new_arr = []
    for y in range(len(crates_arr)-1, -1, -1):
        if crates_arr[y][x] != '   ':
            new_arr.append(crates_arr[y][x])
    crates.append(new_arr)

# extract relevant instructions
instructions = []
for line in instructions_input:
    instructions_arr = line.split(' ')
    instructions.append([instructions_arr[1], instructions_arr[3], instructions_arr[5]])

# move the crates according to instructions 
for nr_crates, from_index, to_index in instructions:
    moved_elements = crates[int(from_index)-1][-int(nr_crates)::]
    del crates[int(from_index)-1][-int(nr_crates)::]
    crates[int(to_index)-1].extend(moved_elements)

# get the top of each stack
result = ''
for s in crates:
    result += s.pop()

print(result)