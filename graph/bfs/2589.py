import sys
from copy import deepcopy
from collections import deque


def bfs(start_x, start_y):
    global graph, h, w, visited, dx, dy
    visited = [[0] * w for _ in range(h)]
    graph_cp = deepcopy(graph)
    graph_cp[start_y][start_x] = "W"
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < w and 0 <= new_y < h and graph_cp[new_y][new_x] == "L":
                graph_cp[new_y][new_x] = "W"
                visited[new_y][new_x] = visited[y][x] + 1
                queue.append((new_x, new_y))
    # for line in visited:
    #     print(line)
    # print()
    result = max(list(map(max, visited)))
    return result


h, w = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(h)]

for i in range(h):
    line = sys.stdin.readline().rstrip()
    for j in range(len(line)):
        graph[i].append(line[j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = list()
for x in range(w):
    for y in range(h):
        if graph[y][x] == "L":
            l_count = 0
            for i in range(4):
                n_x, n_y = x + dx[i], y + dy[i]
                if 0 <= n_x < w and 0 <= n_y < h and graph[n_y][n_x] == "L":
                    l_count += 1
            if 0 < l_count <= 2:
                answer.append(bfs(x, y))

print(max(answer))
