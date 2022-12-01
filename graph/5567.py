import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())
r = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(r):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([(1, 0)])
visited = [False] * (n + 1)
visited[1] = True
answer = 0

while queue:
    cur, dist = queue.popleft()
    for child in graph[cur]:
        if not visited[child] and dist < 2:
            queue.append((child, dist + 1))
            visited[child] = True
            answer += 1

print(answer)


