import sys
sys.setrecursionlimit(10000)

def dfs(graph, node, visited) :
    cnt = 0
    if node in visited :
        return 0
    visited.append(node) 
    if node not in graph.keys() or len(graph[node]) == 0 :
        return 1
    for child in graph[node] :
        cnt += dfs(graph, child, visited)
    return cnt

n = int(input())
visited = []
graph = {}
parents = list(map(int, input().split()))
for child in range(len(parents)) :
    parent = parents[child]
    if parent == -1 :
        graph[0] = []
        continue
    if parent not in graph.keys() :
        graph[parent] = [child]
    else :
        graph[parent].append(child)

remove = int(input())
if remove in graph.keys() :
    del graph[remove]
remove_key = parents[remove]
if remove_key != -1 :
    graph[remove_key].remove(remove)

if len(graph.keys()) == 0 :
    print(0)
else :
    print(dfs(graph, 0, visited))

