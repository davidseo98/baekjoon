import sys
from collections import deque


def bfs(s, f):
    visited = [[False] * (f + 1) for _ in range(f + 1)]
    queue = deque()
    queue.append((s, 0, 0))
    visited[0][s] = True
    while queue:
        # print(queue)
        cur_x, past_move, cnt = queue.popleft()
        if cur_x == f and past_move == 1:
            print(cnt)
            break
        for move in [past_move - 1, past_move, past_move + 1]:
            next = move + cur_x
            if move * (move + 1) // 2 > f - cur_x:
                continue
            if 0 < move <= f and next <= f and not visited[move][next]:
                queue.append((next, move, cnt + 1))
                visited[move][next] = True


n = int(sys.stdin.readline())
for _ in range(n):
    start, finish = map(int, sys.stdin.readline().split())
    bfs(start, finish)
