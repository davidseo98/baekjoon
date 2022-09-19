import sys


def bfs(x, y):
    global answer

    stack = list()
    stack.append((x, y, 1, graph[x][y]))
    while stack:
        cx, cy, cnt, sum_val = stack.pop()
        if cnt == 4:
            if sum_val > answer:
                answer = sum_val
            continue
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                stack.append((nx, ny, cnt + 1, sum_val + graph[nx][ny]))


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        bfs(i, j)

print(answer)
