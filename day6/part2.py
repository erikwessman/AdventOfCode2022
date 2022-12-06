signal = ''
with open('day6/input.txt', 'r') as f:
    signal = f.read()

result = 0

for i, c in enumerate(signal):
    substring = signal[i:i+14]

    if len(set(substring)) == len(substring):
        result = i+14
        break

print(result)