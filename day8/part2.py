arr_input = []
with open('day8/input.txt', 'r') as f:
    arr_input = f.read().splitlines()

arr = []
for row in arr_input:
    arr.append([int(x) for x in row])

def check_row(row, tree, start, stop, step):
    result = 0
    for i in range(start, stop, step):
        val = row[i]
        result += 1
        if val >= tree:
            break
    return result

def calc_scenic_score(x,y,w,h):
    tree = arr[y][x]
    row = arr[y]
    column = [r[x] for r in arr]

    l = check_row(row, tree, x-1,-1,-1)
    r = check_row(row, tree, x+1, w, 1)
    u = check_row(column, tree, y-1,-1,-1)
    d = check_row(column, tree, y+1, h, 1)

    return l*r*u*d

w,h = len(arr[0]), len(arr)
result = 0

for i in range(1, h-1):
    for j in range(1, w-1):
        score = calc_scenic_score(j,i,w,h)
        if score > result:
            result = score

print(result)