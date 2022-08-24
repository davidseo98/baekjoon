import sys
from collections import deque


def check_fuel(f):
    if f < 0:
        print(-1)
        exit()


def get_customer(x, y):
    visited = [[0] * n for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0
    candidate = list()
    min_dist = False
    while queue:
        cur_x, cur_y = queue.popleft()
        if min_dist and visited[cur_x][cur_y] > min_dist:
            return candidate
        if graph[cur_x][cur_y] == 2:
            if not min_dist:
                min_dist = visited[cur_x][cur_y]
            candidate.append((cur_x, cur_y, min_dist))
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and not visited[nx][ny]
                and graph[nx][ny] != 1
            ):
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                queue.append((nx, ny))
    return candidate


def go_desitination(x, y, end_x, end_y):
    visited = [[0] * n for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0
    while queue:
        cur_x, cur_y = queue.popleft()
        if cur_x == end_x and cur_y == end_y:
            return visited[cur_x][cur_y]
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and not visited[nx][ny]
                and graph[nx][ny] != 1
            ):
                visited[nx][ny] = visited[cur_x][cur_y] + 1
                queue.append((nx, ny))
    return -1


n, n_cus, fuel = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
start_x, start_y = map(int, sys.stdin.readline().split())
start_x, start_y = start_x - 1, start_y - 1
customers = dict()
for _ in range(n_cus):
    sx, sy, ex, ey = map(int, sys.stdin.readline().split())
    sx, sy, ex, ey = sx - 1, sy - 1, ex - 1, ey - 1
    if graph[sx][sy] == 1:
        print(-1)
        exit()
    graph[sx][sy] = 2
    customers[(sx, sy)] = [ex, ey]

for _ in range(n_cus):
    can = get_customer(start_x, start_y)
    if not can:
        print(-1)
        exit()
    can.sort(key=lambda x: x[1])
    can.sort(key=lambda x: x[0])
    # print(can)
    x, y, dist = can[0]
    fuel -= dist
    check_fuel(fuel)
    graph[x][y] = 0
    end_x, end_y = customers[(x, y)]
    result = go_desitination(x, y, end_x, end_y)
    fuel -= result
    check_fuel(fuel)
    fuel += result * 2
    if result == -1 or dist == -1:
        print(-1)
        exit()
    start_x, start_y = end_x, end_y
print(fuel)
