tot_array = []
curr_array = []

with open('day1/input.txt', 'r') as f:
    for l in f.read().splitlines():
        if l != '':
            curr_array.append(int(l))
        else:
            tot_array.append(curr_array)
            curr_array = []

summed_arr = [sum(x) for x in tot_array]

top_three = sorted(summed_arr)[-3:]

print(sum(top_three))