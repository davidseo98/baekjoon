import sys
from collections import deque


def bfs(start_x, start_y):
    global visited

    dx = [1, 1, 1, -1, -1, -1, 0, 0]
    dy = [1, -1, 0, 1, -1, 0, -1, 1]
    queue = deque([(start_x, start_y)])
    graph[start_y][start_x] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < w and 0 <= new_y < h and graph[new_y][new_x]:
                graph[new_y][new_x] = 0
                queue.append((new_x, new_y))


while 1:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    graph = list()
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))
    visited = [[0] * w for _ in range(h)]
    count = 0
    for x in range(w):
        for y in range(h):
            if graph[y][x] == 1:
                bfs(x, y)
                count += 1
    print(count)
