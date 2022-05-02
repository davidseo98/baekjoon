import sys
import copy
sys.setrecursionlimit(30000)

def dfs(graph,x,y) :
    if x < 0 or y < 0 or x >= n or y>= n :
        return 0
    if graph[x][y] <= m :
        return 0

    graph[x][y] = m-1
    dfs(graph,x+1,y)
    dfs(graph,x-1,y)
    dfs(graph,x,y+1)
    dfs(graph,x,y-1)
    return 1

n = int(input())
graph = []
for i in range(n) :
    graph.append(list(map(int, input().split())))
graph_max = 0
for line in graph :
    if max(line) > graph_max :
        graph_max = max(line)

answers = []
for m in range(graph_max,-1,-1) :
    answer = 0
    copy_graph = copy.deepcopy(graph)
    for i in range(n) :
        for j in range(n) :
            answer += dfs(copy_graph, i,j)
    answers.append(answer)
print(max(answers))