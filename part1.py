import string

arr = []
with open('day3/input.txt', 'r') as f:
    arr = f.read().splitlines()

total_both = []
total_score = 0

for line in arr:
    h = len(line) // 2
    f_half = line[0:h]
    s_half = line[h:len(line)]

    both = []
    for letter in f_half:
        if letter in s_half and letter not in both:
            both.append(letter)
            total_both.append(letter)

for letter in total_both:
    if letter.isupper():
        total_score += string.ascii_uppercase.index(letter) + 27
    else:
        total_score += string.ascii_lowercase.index(letter) + 1

print(total_score)