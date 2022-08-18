from collections import deque
import sys


def bfs():
    visited = [[False] * n for _ in range(m)]
    queue = deque()
    queue.append((0, 0, False, 0))
    visited[0][0] = "pass"
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        # for _ in range(10):
        x, y, did_break, cnt = queue.popleft()
        # print(x, y, did_break, cnt)
        if x == m - 1 and y == n - 1:
            answer.append(cnt)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 < nx < m and -1 < ny < n:
                if graph[nx][ny] == 0:
                    if visited[x][y] == "pass" and visited[nx][ny] != "pass":
                        visited[nx][ny] = visited[x][y]
                        queue.append((nx, ny, did_break, cnt + 1))
                    elif visited[x][y] == "break" and not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y]
                        queue.append((nx, ny, did_break, cnt + 1))
                if not did_break and graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = "break"
                    queue.append((nx, ny, True, cnt + 1))
        # print()
        # for line in visited:
        #     print(line)


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
