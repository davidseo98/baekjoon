import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
distance = {node: float("inf") for node in range(1, n + 1)}
distance[x] = 0
visited = [False] * (n + 1)
graph = dict()
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    if s not in graph.keys():
        graph[s] = [e]
    else:
        graph[s].append(e)

queue = deque()
queue.append(x)
while queue:
    cur = queue.popleft()
    if visited[cur] or cur not in graph.keys():
        continue
    visited[cur] = True
    for next in graph[cur]:
        distance[next] = min(distance[cur] + 1, distance[next])
        queue.append(next)

does_exists = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        does_exists = True

if not does_exists:
    print(-1)
