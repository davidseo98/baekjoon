t = int(input())
for i in range(t) :
    m,n,l = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(l) :
        x, y = map(int, input().split())
        graph[x][y] = 1

def dfs(graph, x, y) :
    if x <= -1 or y <= -1 or x >= m or y >= n :
        return False
    if graph[x][y] == 0 :
        return False
    graph[x][y] = 0
    dfs(graph,x-1,y)
    dfs(graph,x+1,y)
    dfs(graph,x,y-1)
    dfs(graph,x,y+1)
    return True

answer = 0
for i in range(m) :
    for j in range(n) :
        if dfs(graph, i, j) is True :
            answer +=1

print(answer)
        
