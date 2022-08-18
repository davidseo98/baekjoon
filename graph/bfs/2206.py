from collections import deque
import sys


def bfs():
    visited = [[[False] * n for _ in range(m)] for _ in range(2)]
    queue = deque()
    queue.append((0, 0, False, 0))
    visited[0][0][0] = True
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        x, y, did_break, cnt = queue.popleft()
        if x == m - 1 and y == n - 1:
            answer.append(cnt)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 < nx < m and -1 < ny < n and not visited[did_break][nx][ny]:
                if graph[nx][ny] == 0:
                    visited[did_break][nx][ny] = True
                    queue.append((nx, ny, did_break, cnt + 1))
                if not did_break and graph[nx][ny] == 1:
                    visited[1][nx][ny] = True
                    queue.append((nx, ny, 1, cnt + 1))


m, n = map(int, sys.stdin.readline().split())
answer = list()
graph = list()
for i in range(m):
    line = list()
    inp = sys.stdin.readline().rstrip()
    for j in range(n):
        line.append(int(inp[j]))
    graph.append(line)

bfs()

if answer:
    print(min(answer) + 1)
else:
    print(-1)
