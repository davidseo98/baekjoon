from collections import deque

queue = deque()
maxes = list()
dx, dy = [-1,1,0,0], [0,0,-1,1]
m, n = map(int, input().split())
graph = list()
for i in range(n) :
    graph.append(list(map(int, input().split())))

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            queue.append((i,j))

def bfs() :
    while queue : 
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

bfs()

for line in graph :
    for element in line :
        if element == 0 :
            print(-1)
            exit()
    maxes.append(max(line))

print(max(maxes)-1)
