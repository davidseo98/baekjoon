import sys
from collections import deque

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
visited = [[[False] * w for _ in range(h)] for _ in range(k + 1)]
dx = [1, -1, 0, 0, 2, 2, -2, -2, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1, 2, -2, 2, -2]
queue = deque()
queue.append((0, 0, 0, k))
visited[0][0][0] = True
answer = list()
while queue:
    x, y, cnt, ck = queue.popleft()
    if x == h - 1 and y == w - 1:
        print(cnt)
        exit()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (
            0 <= nx < h
            and 0 <= ny < w
            and not visited[k - ck][nx][ny]
            and graph[nx][ny] == 0
        ):
            visited[k - ck][nx][ny] = True
            queue.append((nx, ny, cnt + 1, ck))
    if ck > 0:
        for i in range(4, 12):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < h
                and 0 <= ny < w
                and not visited[k - ck + 1][nx][ny]
                and graph[nx][ny] == 0
            ):
                visited[k - ck + 1][nx][ny] = True
                queue.append((nx, ny, cnt + 1, ck - 1))
    # print()
    # for line in visited:
    #     print(line)
print(-1)
