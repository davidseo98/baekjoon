import sys
from collections import deque


def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while fire_loc_list:
        fx, fy = fire_loc_list.pop()
        queue.append((fx, fy, "f", 0))
        visited[fx][fy] = True
    queue.append((px, py, "p", 0))
    visited[px][py] = True
    while queue:
        cx, cy, t, cnt = queue.popleft()
        if t == "p" and (cx in [0, h - 1] or cy in [0, w - 1]):
            print(cnt + 1)
            return
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if (
                0 <= nx < h
                and 0 <= ny < w
                and not visited[nx][ny]
                and graph[nx][ny] != "#"
            ):
                visited[nx][ny] = True
                queue.append((nx, ny, t, cnt + 1))

    print("IMPOSSIBLE")


h, w = map(int, sys.stdin.readline().split())
visited = [[False] * w for _ in range(h)]
graph = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
queue = deque()
fire_loc_list = list()

for i in range(h):
    for j in range(w):
        if graph[i][j] == "J":
            px, py = i, j
        elif graph[i][j] == "F":
            fire_loc_list.append((i, j))

bfs()
