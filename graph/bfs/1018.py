from collections import deque
import sys
from copy import deepcopy

sys.setrecursionlimit(10000)


def bfs(t: tuple) -> int:
    global graph, m, n
    graph_copy = deepcopy(graph)
    queue = deque()
    error_count = 0
    visited = [[0] * m for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    start_y = t[0]
    start_x = t[1]

    end_x = 8 + start_x
    end_y = 8 + start_y

    queue.append((start_y, start_x))

    while queue:
        y, x = queue.popleft()
        is_white = check_is_white(graph_copy, x, y)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if start_x <= new_x < end_x and start_y <= new_y < end_y:
                if visited[new_y][new_x] == 0:
                    visited[new_y][new_x] = 1
                    error_count += check_right(graph_copy, new_x, new_y, is_white)
                    queue.append((new_y, new_x))

    return error_count


def bfs2(t: tuple) -> int:
    global graph, m, n
    graph_copy = deepcopy(graph)
    queue = deque()
    error_count = 1  # 처음을 바꾸고 시작하기 때문에, 1로 시작
    visited = [[0] * m for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    start_y = t[0]
    start_x = t[1]

    end_x = 8 + start_x
    end_y = 8 + start_y
    reverse_first(graph_copy, start_x, start_y)

    queue.append((start_y, start_x))

    while queue:
        y, x = queue.popleft()
        is_white = check_is_white(graph_copy, x, y)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if start_x <= new_x < end_x and start_y <= new_y < end_y:
                if visited[new_y][new_x] == 0:
                    visited[new_y][new_x] = 1
                    error_count += check_right(graph_copy, new_x, new_y, is_white)
                    queue.append((new_y, new_x))

    return error_count


def check_is_white(graph, x, y):
    if graph[y][x] == "W":
        return 1
    else:
        return 0


def reverse_first(graph, x, y):
    if graph[y][x] == "W":
        graph[y][x] = "B"
    else:
        graph[y][x] = "W"


def check_right(graph, x, y, prev_is_white):
    value = graph[y][x]
    if prev_is_white:
        if value == "W":
            graph[y][x] = "B"
            return 1
        else:
            return 0
    else:
        if value == "B":
            graph[y][x] = "W"
            return 1
        else:
            return 0


def print_graph(graph):
    for line in graph:
        print(line)


n, m = map(int, input().split())
graph = list()
result = list()
coordinates = list()

for i in range(n):
    line = list()
    for element in input():
        line.append(element)
    graph.append(line)

y_range = list(range(0, n - 7))
x_range = list(range(0, m - 7))

for y in y_range:
    for x in x_range:
        coordinates.append((y, x))

for coordinate in coordinates:
    result.append(bfs(coordinate))
    result.append(bfs2(coordinate))

print(min(result))
