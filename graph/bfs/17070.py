import sys
from collections import deque


def check_left(x, y, q):
    if 0 <= y + 1 < n and graph[x][y + 1] == 0:
        q.append((x, y + 1, 0))


def check_down(x, y, q):
    if 0 <= x + 1 < n and graph[x + 1][y] == 0:
        q.append((x + 1, y, 2))


def check_diag(x, y, q):
    if 0 <= x + 1 < n and 0 <= y + 1 < n:
        if graph[x + 1][y] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y + 1] == 0:
            q.append((x + 1, y + 1, 1))


def dfs(x, y, dir):
    global answer
    stack = list()
    stack.append((x, y, dir))
    while stack:
        cur_x, cur_y, cur_d = stack.pop()
        if cur_x == n - 1 and cur_y == n - 1:
            answer += 1
        if cur_d == 0:
            check_left(cur_x, cur_y, stack)
            check_diag(cur_x, cur_y, stack)
        elif cur_d == 1:
            check_left(cur_x, cur_y, stack)
            check_diag(cur_x, cur_y, stack)
            check_down(cur_x, cur_y, stack)
        else:
            check_diag(cur_x, cur_y, stack)
            check_down(cur_x, cur_y, stack)


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0

dfs(0, 1, 0)

print(answer)
