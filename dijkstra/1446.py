import sys

n, end = map(int, sys.stdin.readline().split())
distance = [float("inf")] * (end + 1)
distance[0] = 0
graph = dict()
for _ in range(n):
    s, e, l = map(int, sys.stdin.readline().split())
    if e > end:
        continue
    if s not in graph.keys():
        graph[s] = [(e, l)]
    else:
        graph[s].append((e, l))

for i in range(0, end + 1):
    if i > 0:
        distance[i] = min(distance[i], distance[i - 1] + 1)
    if i in graph.keys():
        for destination, length in graph[i]:
            distance[destination] = min(distance[destination], distance[i] + length)

print(distance[-1])
