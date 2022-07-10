import sys
from collections import deque


def bfs():
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    count = 0
    while person_queue:

        count += 1
        while fire_queue and fire_queue[0][2] < count:
            x, y, time = fire_queue.popleft()
            for i in range(4):
                new_x, new_y = x + dx[i], y + dy[i]
                if 0 <= new_x < w and 0 <= new_y < h:
                    if graph[new_y][new_x] == "@" or graph[new_y][new_x] == ".":
                        graph[new_y][new_x] = "*"
                        fire_queue.append((new_x, new_y, time + 1))

        while person_queue and person_queue[0][2] < count:
            x, y, time = person_queue.popleft()
            for i in range(4):
                new_x, new_y = x + dx[i], y + dy[i]
                if 0 <= new_x < w and 0 <= new_y < h:
                    if not visited[new_y][new_x] and graph[new_y][new_x] == ".":
                        person_queue.append((new_x, new_y, time + 1))
                        visited[new_y][new_x] = True
                else:
                    return count

    return "IMPOSSIBLE"


t = int(sys.stdin.readline())
for _ in range(t):
    w, h = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(h)]
    for i in range(h):
        line = sys.stdin.readline().rstrip()
        for j in range(len(line)):
            graph[i].append(line[j])
    visited = [[False] * w for _ in range(h)]  # 벽 또는 불로 인해 가지 못하는 공간 표시
    fire_queue = deque([])
    for x in range(w):
        for y in range(h):
            if graph[y][x] == "@":
                start_x, start_y = x, y
                person_queue = deque([(x, y, 0)])
                visited[y][x] = True
            elif graph[y][x] == "*":
                fire_queue.append((x, y, 0))

    if start_x in (0, w - 1) or start_y in (0, h - 1):
        print(1)
        continue

    print(bfs())
