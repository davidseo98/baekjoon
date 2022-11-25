import sys
from collections import deque

def bfs():
    global answer

    queue = deque([(0, 0, graph[0][0])])
    while queue:
        cx, cy, cs = queue.popleft()
        if cx == r - 1 and cy == c - 1:
            if cs > answer: answer = cs

        for i in range(3):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                queue.append((nx, ny, cs + graph[nx][ny]))
            

r, c = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx = [1, 0, 1]
dy = [0, 1, 1]
s = [0, 0, graph[0][0]]
answer = 0

bfs()

print(answer)