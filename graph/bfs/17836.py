from stringprep import map_table_b2
import sys
from collections import deque

n, m, t = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
queue = deque()
queue.append((0,0,0,False))
visited[0][0] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
while queue :
    cur_x, cur_y, cnt, is_break = queue.popleft()
    if cnt > t : 
        print("Fail")
        exit()
    if cur_x == m - 1 and cur_y == n - 1:
        print(cnt)
        exit()
    for i in range(4) :
        nx, ny = cur_x + dx[i], cur_y + dy[i]
        if is_break :
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] < 2:
                queue.append((nx, ny, cnt + 1, is_break))
                visited[ny][nx] = 2
        else :
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                if graph[ny][nx] != 1 :
                    if graph[ny][nx] == 2 :
                        queue.append((nx, ny, cnt + 1, True))
                    else :
                        queue.append((nx,ny,cnt + 1, is_break))
                    visited[ny][nx] = 1
print("Fail")