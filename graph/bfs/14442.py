import sys
from collections import deque


def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((0, 0, 0, 0))
    visited[0][0][0] = True
    while queue:
        x, y, break_cnt, move_cnt = queue.popleft()
        if x == h - 1 and y == w - 1:
            print(move_cnt + 1)
            return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[break_cnt][nx][ny]:
                if graph[nx][ny] == "0":
                    visited[break_cnt][nx][ny] = True
                    queue.append((nx, ny, break_cnt, move_cnt + 1))
                if graph[nx][ny] == "1" and break_cnt < k:
                    visited[break_cnt][nx][ny] = True
                    queue.append((nx, ny, break_cnt + 1, move_cnt + 1))
    print(-1)


h, w, k = map(int, sys.stdin.readline().split())
graph = [sys.stdin.readline().rstrip() for _ in range(h)]
visited = [[[False] * w for _ in range(h)] for _ in range(k + 1)]
bfs()
