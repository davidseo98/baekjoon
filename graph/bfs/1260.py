
from collections import deque
def dfs(graph, start,visited) : 
    if start not in visited :
        visited.append(start)
        for node in graph[start] :
            dfs(graph, node, visited)
    return visited

def bfs(graph, start) :
    visited = list()
    queue = deque()
    queue.append(start)
    while queue :
        node = queue.popleft()
        if node not in visited :
            visited.append(node)
            queue.extend(graph[node])
    return visited

n, m, start = map(int, input().split())
visited = list()
graph = dict()
for i in range(n) :
    graph[i+1] = []
for i in range(m): 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for item in dfs(graph,start,visited) : 
    print(item, end = " ")
print()
for item in bfs(graph, start) :
    print(item, end=" ")

