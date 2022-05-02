import sys
sys.setrecursionlimit(10000)

def dfs(x,y) :
    if x <= -1 or y <= -1 or x >= n or y >= n :
        return 0
    if graph[x][y] == 0:
        return 0
    graph[x][y] =0
    cnt = 1
    cnt += dfs(x+1,y)
    cnt += dfs(x-1,y)
    cnt += dfs(x,y+1)
    cnt += dfs(x,y-1)

    return cnt

n = int(input())
graph = [[] for _ in range(n)]
num_of_houses = []
for i in range(n) :
    line = input()
    for item in line : 
        graph[i].append(int(item))

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            num_of_houses.append(dfs(i,j))
print(len(num_of_houses))
for num in sorted(num_of_houses) :
    print(num)