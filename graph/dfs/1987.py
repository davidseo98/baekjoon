from inspect import stack
import sys
from collections import deque


def dfs():
    global answer, visited

    # queue = deque()
    # queue.append((0, 0, graph[0][0], 1))
    stack = list()
    stack.append((0, 0, graph[0][0], 1))

    while stack:
        cur_x, cur_y, visited_alphas, count = stack.pop()
        if count > answer:
            answer = count
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                next_alpha = graph[nx][ny]
                if next_alpha in visited_alphas:
                    continue
                stack.append((nx, ny, visited_alphas + next_alpha, count + 1))


h, w = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
visited = [[False] * w for _ in range(h)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0

dfs()

print(answer)
