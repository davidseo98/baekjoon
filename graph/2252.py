import sys
from collections import deque, defaultdict

input = sys.stdin.readline

in_dim = defaultdict(int)
graph = defaultdict(list)
n, m = map(int, input().split())

for _ in range(m):
    tall, short = map(int, input().split())
    graph[short].append(tall)
    in_dim[tall] += 1

queue = deque([])
result = []

for node in range(1, n + 1):
    if in_dim[node] == 0:
        queue.append(node)

while queue:
    cur = queue.popleft()
    result.append(cur)

    for child in graph[cur]:
        in_dim[child] -= 1
        if in_dim[child] == 0: queue.append(child)

print(* result[::-1])