import sys
from collections import deque


def bfs():
    global fire_queue, person_queue, visited, graph, person_visited
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    count = 1
    while 1:
        if len(person_queue) == 0:
            return "IMPOSSIBLE"
        new_fire_queue = deque([])
        new_person_queue = deque([])
        while fire_queue:
            x, y = fire_queue.popleft()
            for i in range(4):
                new_x, new_y = x + dx[i], y + dy[i]
                if 0 <= new_x < w and 0 <= new_y < h and visited[new_y][new_x] == 0:
                    visited[new_y][new_x] = 1
                    new_fire_queue.append((new_x, new_y))

        while person_queue:
            x, y = person_queue.popleft()
            for i in range(4):
                new_x, new_y = x + dx[i], y + dy[i]
                if (
                    0 <= new_x < w
                    and 0 <= new_y < h
                    and visited[new_y][new_x] == 0
                    and ((new_x, new_y) not in person_visited)
                ):
                    if new_x in (0, w - 1) or new_y in (0, h - 1):
                        return count + 1
                    person_visited.add((new_x, new_y))
                    new_person_queue.append((new_x, new_y))
        count += 1
        person_queue = new_person_queue
        fire_queue = new_fire_queue


t = int(sys.stdin.readline())
for _ in range(t):
    w, h = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(h)]
    for i in range(h):
        line = sys.stdin.readline().rstrip()
        for j in range(len(line)):
            graph[i].append(line[j])
    visited = [[0] * w for _ in range(h)]  # 벽 또는 불로 인해 가지 못하는 공간 표시
    person_visited = set()  # 이미 방문한 공간 표시
    fire_queue = deque([])
    for x in range(w):
        for y in range(h):
            if graph[y][x] == "@":
                start_x, start_y = x, y
                person_queue = deque([(x, y)])
                person_visited.add((x, y))
            elif graph[y][x] == "*":
                visited[y][x] = 1
                fire_queue.append((x, y))
            elif graph[y][x] == "#":
                visited[y][x] = 1
    if start_x in (0, w - 1) or start_y in (0, h - 1):
        print(1)
        exit()

    print(bfs())
