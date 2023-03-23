import sys
from collections import deque

def check_all(x, y):
    global answer

    for dxs, dys in zip(total_dxs, total_dys):
        for dx, dy in zip(dxs, dys):
            score = board[x][y]
            for i in range(3):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    score += board[nx][ny]

            answer = max(answer, score)

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

total_dxs = []
total_dys = []

# 정사각형
total_dxs.append([[0, 1, 1]])
total_dys.append([[1, 0, 1]])

# 직선 모양
total_dxs.append([[1, 2, 3], [0, 0, 0]])
total_dxs.append([[0, 0, 0], [1, 2, 3]])

# ㅗ 모양
total_dxs.append([[0, 0, -1], [1, 2, 1,], [0, 0, 1], [-1, -2, -1]])
total_dys.append([[1, 2, -1], [0, 0, 1], [-1, -2, -1], [0, 0, -1]])

# ㄴ 모양 (flip 필요)
total_dxs.append([[1, 2, 2], [1, 0, 0], [0, 1, 1], [1, 1, 1], [1, 2, 2], [1, 0, 0], [0, 1, 1], [1, 2, 2]])
total_dys.append([[0, 0, 1], [0, 1, 2], [1, 1, 2], [0, 1, 2], [0, 0, -1], [0, -1, -2], [-1, -1, -2], [0, -1, -2]])

# ㄹ 모양 (flip 필요)
total_dxs.append([[1, 1, 2], [0, -1, -1], [1, 1, 2], [0, -1, -1]])
total_dys.append([[0, 1, 1], [1, 1, 2], [0, -1, -1], [-1, -1, -2]])

answer = -1

for x in range(n):
    for y in range(m):
        check_all(x, y)

print(answer)
