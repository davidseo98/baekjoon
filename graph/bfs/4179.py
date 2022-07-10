import sys
from collections import deque


def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0
    while person_queue:
        count += 1
        while fire_queue and fire_queue[0][2] < count:
            x, y, time = fire_queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < w and 0 <= ny < h:
                    if graph[y][x] == "." or graph[y][x] == "J":
                        fire_queue.append((nx, ny, time + 1))
                        graph[ny][nx] = "F"

        while person_queue and person_queue[0][2] < count:
            x, y, time = person_queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < w and 0 <= ny < h:
                    if not visited[ny][ny] and graph[ny][nx] == ".":
                        person_queue.append((nx, ny, time + 1))
                        visited[ny][nx] = True
                else:
                    return count

    return "IMPOSSIBLE"


h, w = map(int, sys.stdin.readline().split())
visited = [[False] * w for _ in range(h)]
graph = [[] for _ in range(h)]
for i in range(h):
    for element in sys.stdin.readline().strip():
        graph[i].append(element)

fire_queue = deque()
for y in range(h):
    for x in range(w):
        if graph[y][x] == "J":
            person_queue = deque([(x, y, 0)])
            visited[y][x] = True
        elif graph[y][x] == "F":
            fire_queue.append((x, y, 0))

print(bfs())
