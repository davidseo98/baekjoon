import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
compliments = defaultdict(int)

for i, boss in enumerate(list(map(int, input().split()))):
    graph[boss].append(i + 1)

for _ in range(m):
    person, amount = map(int, input().split())
    compliments[person] += amount

queue = deque([(-1, 0)])
visited = [0] * (n + 1)

while queue:
    
    cur, comp = queue.popleft()

    for child in graph[cur]:
        queue.append((child, comp + compliments[child]))
        visited[child] = comp + compliments[child]

print(*visited[1:])

