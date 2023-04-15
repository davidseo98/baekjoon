from collections import defaultdict

n, m = map(int, input().split())
board = defaultdict(int)

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1 - 1, x2):
        for y in range(y1 - 1, y2):
            board[(x, y)] += 1

answer = 0
for x in range(100):
    for y in range(100):
        if board[(x, y)] > m: answer += 1

print(answer)