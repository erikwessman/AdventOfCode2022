tot_array = []
curr_array = []

with open('day1/input.txt', 'r') as f:
    for l in f.read().splitlines():
        if l != '':
            curr_array.append(int(l))
        else:
            tot_array.append(curr_array)
            curr_array = []

most_calories = 0

for arr in tot_array:
    if sum(arr) > most_calories:
        most_calories = sum(arr)

print(most_calories)