arr = []
with open('day2/input.txt', 'r') as f:
    arr = f.read().splitlines()

score_dict = {'X': 0, 'Y': 3, 'Z': 6}
total_score = 0

for a in arr:
    play, response = a.split(' ')

    total_score += score_dict[response]
    
    if play == 'A':
        if response == 'X':
            total_score += 3
        elif response == 'Y':
            total_score += 1
        else:
            total_score += 2
    elif play == 'B':
        if response == 'X':
            total_score += 1
        elif response == 'Y':
            total_score += 2
        else:
            total_score += 3
    else:
        if response == 'X':
            total_score += 2
        elif response == 'Y':
            total_score += 3
        else:
            total_score += 1

print(total_score)