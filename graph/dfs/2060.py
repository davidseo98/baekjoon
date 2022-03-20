def dfs(graph, start, visited) :
    visited.append(start)
    for node in graph[start] :
        if node not in visited :
            dfs(graph, node, visited)
    return visited

n = int(input())
graph = dict()
visited = []
for i in range(n) :
    graph[i+1] = []
r = int(input())
for i in range(r) :
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

print(len(dfs(graph,1,visited))-1)
