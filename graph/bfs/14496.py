import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
n, m = map(int, sys.stdin.readline().split())
graph = dict()
for i in range(1, n + 1):
    graph[i] = list()
for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False] * (n + 1)
queue = deque()
queue.append((a, 0))
visited[a] = True
is_possible = False
while queue:
    cur, cnt = queue.popleft()
    if cur == b:
        is_possible = True
        print(cnt)
    for next in graph[cur]:
        if not visited[next]:
            queue.append((next, cnt + 1))
            visited[next] = True
if not is_possible :
    print(-1)