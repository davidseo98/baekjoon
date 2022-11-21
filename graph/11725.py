import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())
graph = defaultdict(list)
find_parent = dict()
visited = set()

while True:
    input = sys.stdin.readline()
    if not input: break
    a, b = map(int, input.split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
visited.add(1)
while queue:
    cur_node = queue.pop()
    for child in graph[cur_node]:
        if child == cur_node or child in visited: continue
        find_parent[child] = cur_node
        queue.append(child)
        visited.add(child)

for i in range(2, n + 1):
    print(find_parent[i])