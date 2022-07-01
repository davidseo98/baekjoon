import sys
from collections import deque


def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 1
    graph[start_y][start_x] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m and graph[new_y][new_x] == 0:
                graph[new_y][new_x] = 1
                count += 1
                queue.append((new_x, new_y))
    return count


m, n, k = map(int, sys.stdin.readline().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())
    for x in range(start_x, end_x):
        for y in range(m - end_y, m - start_y):
            graph[y][x] = 1

result = list()
for x in range(n):
    for y in range(m):
        if graph[y][x] == 0:
            result.append(bfs(x, y))

print(len(result))
for r in sorted(result):
    print(r, end=" ")
