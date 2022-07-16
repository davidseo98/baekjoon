import sys
from collections import deque

a, b, start, end = map(int, sys.stdin.readline().split())
visited = [False] * (100001)
queue = deque()
queue.append((start, 0))
visited[start] = True
while queue:
    cur, cnt = queue.popleft()
    if cur == end:
        print(cnt)
        break
    for next in [
        cur - 1,
        cur + 1,
        cur + a,
        cur - a,
        cur + b,
        cur - b,
        cur * a,
        cur * b,
    ]:
        if 0 <= next <= 100000 and not visited[next]:
            queue.append((next, cnt + 1))
            visited[next] = True
