import sys
from collections import deque

def check_all(x, y):
    global answer

    for i, diffs in enumerate(zip(total_dxs, total_dys)):
        dxs, dys = diffs
        if i == 0: r = 2
        elif i == 1: r = 1
        else: r = 4

        for rotate in range(r): # rotate 0 ~ 3
            cnt = 0
            score = board[x][y] # 현재 칸 점수 

            for dx, dy in zip(dxs, dys):

                for _ in range(rotate): # 도형 회전 
                    dx, dy = -dy, dx

                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    cnt += 1
                    score += board[nx][ny]

                else: break
                
            if cnt == 3: answer = max(answer, score) # 모든 칸이 올려졌을 때만 반영


input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

total_dxs = [[0, 0, 0], [0, 1, 1], [0, 0, 1], [-1, 0, 1], [-1, 0, 1], [1, 2, 2], [1, 2, 2]]
total_dys = [[1, 2, 3], [1, 0, 1], [1, 2, 1], [1, 1, 0], [-1, -1, 0], [0, 0, 1], [0, 0, -1]]

answer = -1

for x in range(n):
    for y in range(m):
        check_all(x, y)

print(answer)
