from re import L
import sys
from collections import deque


def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    sheep_cnt, wolf_cnt = 0, 0
    while queue:
        cx, cy = queue.popleft()
        if graph[cx][cy] == "v":
            wolf_cnt += 1
        elif graph[cx][cy] == "k":
            sheep_cnt += 1
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if (
                0 <= nx < h
                and 0 <= ny < w
                and not visited[nx][ny]
                and graph[nx][ny] != "#"
            ):
                visited[nx][ny] = True
                queue.append((nx, ny))
    if sheep_cnt <= wolf_cnt:
        return 0, wolf_cnt
    else:
        return sheep_cnt, 0


h, w = map(int, sys.stdin.readline().split())
graph = [sys.stdin.readline().rstrip() for _ in range(h)]
visited = [[False] * w for _ in range(h)]
sheep_total, wolf_total = 0, 0
for i in range(h):
    for j in range(w):
        if graph[i][j] != "#" and not visited[i][j]:
            sc, wc = bfs(i, j)
            sheep_total += sc
            wolf_total += wc

print(sheep_total, wolf_total)
