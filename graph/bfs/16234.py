import sys
from collections import deque


def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    people_sum = graph[x][y]
    nation_count = 1
    nation_loc = list()

    while queue:
        cx, cy = queue.popleft()
        for move in range(4):
            nx, ny = cx + dx[move], cy + dy[move]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                diff = abs(graph[cx][cy] - graph[nx][ny])
                if l <= diff <= r:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    people_sum += graph[nx][ny]
                    nation_count += 1
                    nation_loc.append((nx, ny))

    new_people = people_sum // nation_count
    instructions[(x, y)] = new_people
    if nation_loc:
        for cur_x, cur_y in nation_loc:
            instructions[(cur_x, cur_y)] = new_people
        return 1
    else:
        return 0


n, l, r = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0

while 1:

    instructions = dict()
    visited = [[False] * n for _ in range(n)]
    changes = list()
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                changes.append(bfs(i, j))

    if sum(changes) == 0:
        break

    for key, item in instructions.items():
        graph[key[0]][key[1]] = item

    answer += 1

print(answer)
