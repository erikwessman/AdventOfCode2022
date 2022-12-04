arr = []
with open('day4/input.txt', 'r') as f:
    arr = f.read().splitlines()

overlapping = 0

for line in arr:
    l_pair, r_pair = line.split(',')
    l = l_pair.split('-')
    r = r_pair.split('-')
    l1 = int(l[0])
    l2 = int(l[1])
    r1 = int(r[0])
    r2 = int(r[1])
    
    if (l1 <= r1 and l2 >= r2) or (l1 >= r1 and l2 <= r2):
        overlapping += 1

print(overlapping)