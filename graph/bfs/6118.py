import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = dict()
for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    if n1 not in graph.keys():
        graph[n1] = [n2]
    else:
        graph[n1].append(n2)
    if n2 not in graph.keys():
        graph[n2] = [n1]
    else:
        graph[n2].append(n1)

queue = deque()
queue.append((1, 0))
visited = [False] * (n + 1)
visited[1] = True
max_depth = 0
answer = list()
while queue:
    cur, cnt = queue.popleft()
    if cnt > max_depth:
        answer = [cur]
        max_depth = cnt
    elif cnt == max_depth:
        answer.append(cur)
    if cur in graph.keys():
        for next in graph[cur]:
            if not visited[next]:
                queue.append((next, cnt + 1))
                visited[next] = True
print(min(answer), max_depth, len(answer))
