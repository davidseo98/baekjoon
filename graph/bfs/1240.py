import sys
from collections import deque


def bfs(start, end):
    queue = deque()
    visited = [False] * (n + 1)
    queue.append((start, 0))
    visited[start] = True
    while queue:
        cur, dist = queue.popleft()
        if cur == end:
            print(dist)
        for next in graph[cur]:
            if not visited[next[0]]:
                queue.append((next[0], dist + next[1]))
                visited[next[0]] = True


input = sys.stdin.readline
n, m = map(int, input().split())
graph = dict()
for i in range(1, n + 1):
    graph[i] = list()
for _ in range(n - 1):
    n1, n2, dist = map(int, input().split())
    graph[n1].append((n2, dist))
    graph[n2].append((n1, dist))
for _ in range(m):
    start, end = map(int, input().split())
    bfs(start, end)
