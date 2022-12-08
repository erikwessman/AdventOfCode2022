arr_input = []
with open('day8/input.txt', 'r') as f:
    arr_input = f.read().splitlines()

arr = []
for row in arr_input:
    arr.append([int(x) for x in row])

def is_visible(x,y,w,h):
    tree = arr[y][x]
    
    left = arr[y][0:x]
    right = arr[y][x+1:w]
    up = [i[x] for i in arr][0:y]
    down = [i[x] for i in arr][y+1:h]

    return max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree

w,h = len(arr[0]), len(arr)
result = w*2 + h*2 - 4

for i in range(1, h-1):
    for j in range(1, w-1):
        if is_visible(j,i,w,h):
            result += 1

print(result)