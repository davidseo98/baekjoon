import sys
from collections import deque
from copy import deepcopy

sys.setrecursionlimit(10000)

def infest():
    global s, board

    lab = deepcopy(board)

    for x, y in s:
        lab[x][y] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue = deque(virus.copy())
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
                queue.append((nx, ny))
                lab[nx][ny] = 2
    
    cnt = 0
    for line in lab:
        for square in line:
            if square == 0: cnt += 1

    return cnt

def dfs(sn):
    global answer, s

    if len(s) == 3:
        answer = max(answer, infest())
        return

    for i in range(sn, n):
        for j in range(m):
            if board[i][j] == 0 and (i, j) not in s: # 이 부분이 없다면, 동일한 벽을 포함시켜서 정답이 달라질 수 있다.
                s.append((i,j))
                dfs(i)
                s.pop()

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2: virus.append((i, j))

s = []
answer = -1

dfs(0)

print(answer)