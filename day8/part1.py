arr_input = []
with open('day8/input.txt', 'r') as f:
    arr_input = f.read().splitlines()

arr = []
for row in arr_input:
    arr.append([int(x) for x in row])

def calc_scenic_score(x,y,w,h):
    tree = arr[y][x]
    row = arr[y]
    column = [r[x] for r in arr]

    left = 0
    for i in range(x-1, -1, -1):
        val = row[i]
        left += 1
        if val >= tree:
            break
    
    right = 0
    for i in range(x+1, w):
        val = row[i]
        right += 1
        if val >= tree:
            break

    up = 0
    for i in range(y-1, -1, -1):
        val = column[i]
        up += 1
        if val >= tree:
            break

    down = 0
    for i in range(y+1, h):
        val = column[i]
        down += 1
        if val >= tree:
            break


    return left*right*up*down

w,h = len(arr[0]), len(arr)
result = 0

for i in range(1, h-1):
    for j in range(1, w-1):
        score = calc_scenic_score(j,i,w,h)
        if score > result:
            result = score

print(result)