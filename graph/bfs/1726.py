import sys
from collections import deque


def bfs():
    global start_x, start_y, start_direction, target_x, target_y, h, w
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(start_x - 1, start_y - 1, start_direction)])
    count = 1
    while 1:
        next_queue = deque([])
        while queue:
            x, y, dir = queue.popleft()
            for i in range(4):
                new_x, new_y, new_dir = x + dx[i], y + dy[i], i + 1
                if 0 <= new_x < w and 0 <= new_y < h and graph[new_y][new_x] == 0:
                    if new_x == target_x - 1 and new_y == target_y - 1:
                        return count
                    if dir == new_dir:
                        dir_change = 1
                    elif (dir in [4, 3] and new_dir in [4, 3]) or (
                        dir in [1, 2] and new_dir in [1, 2]
                    ):
                        dir_change = 2
                    else:
                        dir_change = 1

                    graph[new_y][new_x] = graph[y][x] + dir_change
                    next_queue.append((new_x, new_y, new_dir))
        count += 1
        queue = next_queue


h, w = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
start_x, start_y, start_direction = map(int, sys.stdin.readline().split())
target_x, target_y, target_direction = map(int, sys.stdin.readline().split())
print(bfs())
for line in graph:
    print(line)
