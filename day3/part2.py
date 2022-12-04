import string

arr = []
with open('day3/input.txt', 'r') as f:
    arr = f.read().splitlines()

total_both = []
total_score = 0

for i in range(0, len(arr), 3):
    line1, line2, line3 = arr[i:i+3]

    both = []
    for letter in line1:
        if letter in line2 and letter in line3:
            total_both.append(letter)
            break

for letter in total_both:
    if letter.isupper():
        total_score += string.ascii_uppercase.index(letter) + 27
    else:
        total_score += string.ascii_lowercase.index(letter) + 1

print(total_score)