arr = []
with open('day2/input.txt', 'r') as f:
    arr = f.read().splitlines()

score_dict = {'X': 1, 'Y': 2, 'Z': 3}
total_score = 0

for a in arr:
    play, response = a.split(' ')

    total_score += score_dict[response]
    
    if play == 'A':
        if response == 'X':
            total_score += 3
        elif response == 'Y':
            total_score += 6
        else:
            total_score += 0
    elif play == 'B':
        if response == 'X':
            total_score += 0
        elif response == 'Y':
            total_score += 3
        else:
            total_score += 6
    else:
        if response == 'X':
            total_score += 6
        elif response == 'Y':
            total_score += 0
        else:
            total_score += 3

print(total_score)