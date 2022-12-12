arr = []
with open('day9/input.txt', 'r') as f:
    arr = f.read().splitlines()

head = [0,0]
tail = [0,0]
last_pos = [0,0]
visited = set()

for line in arr:
    direction, steps = line.split(' ')
    steps = int(steps)

    for _ in range(steps):
        match direction:
            case 'L':
                head[0] -= 1
            case 'R':
                head[0] += 1
            case 'U':
                head[1] -= 1
            case 'D':
                head[1] += 1

        is_diff = abs(head[0] - tail[0]) >= 2 or abs(head[1] - tail[1]) >= 2

        if is_diff:
            tail[0] = last_pos[0]
            tail[1] = last_pos[1]

        last_pos[0] = head[0]
        last_pos[1] = head[1]

        if tuple(tail) not in visited:
            visited.add(tuple(tail))

print(len(visited))