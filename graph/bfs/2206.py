from collections import deque
import queue

m, n = map(int, input().split())

graph = list()
for i in range(m):
    line = list()
    inp = input()
    for j in range(n):
        line.append(int(inp[j]))
    graph.append(line)

queue = deque()
queue.append((0, 0, 0))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(graph)
graph[0][0] = 1
break_count = 0


def bfs():
    while queue:
        x, y, b = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 < nx < n and -1 < ny < m and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))


bfs()

print(graph)
