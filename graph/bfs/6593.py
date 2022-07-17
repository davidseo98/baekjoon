import sys
from collections import deque

def bfs() :
    global visited
    queue = deque()
    queue.append((start_x, start_y, start_z, 0))
    visited[start_z][start_y][start_x] = True
    while queue :
        cur_x, cur_y, cur_z, cnt = queue.popleft()
        if graph[cur_z][cur_y][cur_x] == "E" :
            print(f"Escaped in {cnt} minute(s).")
            return
        for i in range(6) :
            nx, ny, nz = cur_x + dx[i], cur_y + dy[i], cur_z + dz[i]
            if 0 <= nx < c and 0 <= ny < r and 0 <= nz < l :
                if not visited[nz][ny][nx] and graph[nz][ny][nx] != "#":
                    queue.append((nx,ny,nz,cnt + 1))
                    visited[nz][ny][nx] = True
    print("Trapped!")

l, r, c = map(int, sys.stdin.readline().split())
dz = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dx = [0,0,0,0,1,-1]
while l + r + c > 0 :
    graph = list()
    for z in range(l) :
        page = list()
        for y in range(r) :
            line = sys.stdin.readline().strip()
            page.append(line)
            for x in range(c) :
                if line[x] == "S" :
                    start_x, start_y, start_z = x, y, z
        graph.append(page)
        sys.stdin.readline()
    visited = [[[False] * (c) for _ in range(r)] for _ in range(l)]
    bfs()
    l, r, c = map(int, sys.stdin.readline().split())