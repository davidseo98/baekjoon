import sys
from collections import deque


def search():
    global answer
    queue = deque()
    queue.append(0)
    while queue:
        cur_node = queue.popleft()
        if cur_node not in graph.keys():
            answer += 1
            continue

        for child in graph[cur_node]:
            queue.append(child)


def bfs(delete):
    queue = deque()
    queue.append(delete)
    visited[delete] = True
    while queue:
        cur_node = queue.popleft()
        if cur_node not in graph.keys():
            continue

        for child in graph[cur_node]:
            if not visited[child] and child in graph.keys():
                queue.append(child)
                visited[child] = True


graph = dict()
n = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().split()))
delete_node = int(sys.stdin.readline())
visited = [False] * (n)
answer = 0

for i in range(n):
    if i == 0:
        graph[-1] = [i]
        continue
    if nodes[i] not in graph.keys():
        graph[nodes[i]] = [i]
    else:
        graph[nodes[i]].append(i)

bfs(delete_node)

graph[nodes[delete_node]].remove(delete_node)
if len(graph[nodes[delete_node]]) == 0:
    del graph[nodes[delete_node]]

for i in range(n):
    if visited[i] and i in graph.keys():
        del graph[i]

search()

print(answer)
