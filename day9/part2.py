import numpy as np

arr = []
with open('day9/input.txt', 'r') as f:
    arr = f.read().splitlines()

knots = np.zeros(shape=(10,2)).astype(int).tolist()
visited = set()

for line in arr:
    direction, steps = line.split(' ')
    steps = int(steps)

    for _ in range(steps):
        match direction:
            case 'L':
                knots[0][0] -= 1
            case 'R':
                knots[0][0] += 1
            case 'U':
                knots[0][1] -= 1
            case 'D':
                knots[0][1] += 1

        for i in range(1, len(knots)):
            hor_diff = knots[i-1][0] - knots[i][0]
            vert_diff = knots[i-1][1] - knots[i][1]

            if abs(vert_diff) >= 2:
                if vert_diff < 0:
                    knots[i][1] -= 1
                else:
                    knots[i][1] += 1

                if abs(hor_diff) == 1:
                    knots[i][0] += hor_diff

            if abs(hor_diff) >= 2:
                if hor_diff < 0:
                    knots[i][0] -= 1
                else:
                    knots[i][0] += 1

                if abs(vert_diff) == 1:
                    knots[i][1] += vert_diff


        if tuple(knots[len(knots)-1]) not in visited:
            visited.add(tuple(knots[len(knots)-1]))

print(len(visited))