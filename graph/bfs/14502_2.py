import sys
from collections import deque
from copy import deepcopy


def bfs():
    global graph, answer
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    graph_cpy = deepcopy(graph)
    virus = deque()
    for y in range(h):
        for x in range(w):
            if graph_cpy[y][x] == 2:
                virus.append((x, y))

    while virus:
        x, y = virus.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if graph_cpy[ny][nx] == 0:
                    graph_cpy[ny][nx] = 2
                    virus.append((nx, ny))
    result = 0
    for line in graph_cpy:
        result += line.count(0)
    answer = max(answer, result)


def makewall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makewall(cnt + 1)
                graph[i][j] = 0


h, w = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

answer = 0
makewall(0)
print(answer)
