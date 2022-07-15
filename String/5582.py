import sys

input = sys.stdin.readline
string1 = input().strip()
string2 = input().strip()
answer = 0
for i in range(len(string1)):
    if string1[i] in string2:
        for j in range(i + answer, len(string1) + 1):
            temp = string1[i:j]
            if temp in string2:
                answer = max(answer, len(temp))
            else:
                break
print(answer)
