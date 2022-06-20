import sys

input_string = sys.stdin.readline().rstrip()
letters = list()
for i in range(len(input_string)):
    letters.append(input_string[i])

result = list()

for i in range(1, len(letters) + 1):
    end = 0
    for j in range(len(letters)):
        start = j
        end = j + i
        result.append(input_string[start:end])
        if end == len(letters) - 1:
            break

print(len(set(result)))
