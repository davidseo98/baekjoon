import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append((start_x, start_y))
    visited.add((start_x, start_y))
    while queue:
        cur_x, cur_y = queue.popleft()
        if abs(cur_x - end_x) + abs(cur_y - end_y) <= 1000:
            print("happy")
            return
        for store in store_list:
            if (
                abs(cur_x - store[0]) + abs(cur_y - store[1]) <= 1000
                and (store[0], store[1]) not in visited
            ):
                queue.append((store[0], store[1]))
                visited.add((store[0], store[1]))
    print("sad")


t = int(sys.stdin.readline())
for _ in range(t):
    n_c = int(sys.stdin.readline())
    start_x, start_y = map(int, sys.stdin.readline().split())
    store_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n_c)]
    end_x, end_y = map(int, sys.stdin.readline().split())
    visited = set()
    bfs()
