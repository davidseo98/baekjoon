import sys
sys.setrecursionlimit(10000)
def dfs(x, y) :
    if x <= -1 or y <= -1 or x >= m or y >= n :
        return False
    if graph[x][y] == 0 :
        return False
    graph[x][y] = 0
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True

t = int(input())
answers = []
for i in range(t) :
    n,m,l = map(int, input().split())
    graph = [[0]*n for _ in range(m)]
    for i in range(l) :
        x, y = map(int, input().split())
        graph[y][x] = 1

    answer = 0
    for i in range(m) :
        for j in range(n) :
            if graph[i][j]==1 :
                dfs(i,j)
                answer +=1
    answers.append(answer)


for answer in answers : 
    print(answer)
        
