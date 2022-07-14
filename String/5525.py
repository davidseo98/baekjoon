import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
string = sys.stdin.readline().strip()
target_string = "I"
for _ in range(n):
    target_string += "O"
    target_string += "I"
loc = 0
answer = 0
while loc < m - 2 * n:
    if string[loc : loc + 2 * n + 1] == target_string:
        answer += 1
        loc += 2
    else:
        loc += 1

print(answer)
