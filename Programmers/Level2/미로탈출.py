from collections import deque

def bfs(sx, sy, maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    ex, ey = len(maps), len(maps[0])
    visited = [[[False] * ey for _ in range(ex)] for _ in range(2)]
    visited[0][sx][sy] = True
    queue = deque([(sx, sy, 0, 0)])
    
    while queue:
        cx, cy, switch, cnt = queue.popleft()

        if maps[cx][cy] == 'E' and switch: 
            return cnt
        if maps[cx][cy] == 'L': switch = 1
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < ex and 0 <= ny < ey and not visited[switch][nx][ny] and maps[nx][ny] != "X":
                queue.append((nx, ny, switch, cnt + 1))
                visited[switch][nx][ny] = True
        
    return -1

def solution(maps):

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                return bfs(i, j, maps)