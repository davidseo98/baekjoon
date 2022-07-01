import sys
from collections import deque


def bfs(x, y):
    global target_x, target_y
    queue = deque([(start_x, start_y)])
    dx = [-1, -1, 1, 1, -2, -2, 2, 2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1]
    count = 0
    # while queue:
    while 1:
        next_queue = deque([])
        while queue:
            x, y = queue.popleft()
            if x == target_x and y == target_y:
                return count
            for i in range(8):
                new_x, new_y = x + dx[i], y + dy[i]
                if 0 <= new_x < n and 0 <= new_y < n and not (visited[new_y][new_x]):
                    visited[new_y][new_x] = 1
                    next_queue.append((new_x, new_y))
        count += 1
        queue = next_queue


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    start_x, start_y = map(int, sys.stdin.readline().split())
    target_x, target_y = map(int, sys.stdin.readline().split())
    visited = [[0] * n for _ in range(n)]
    print(bfs(start_x, start_y))
