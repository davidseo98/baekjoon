import sys
from collections import deque


def bfs(start_x, start_y, visited):
    global n
    queue = deque([(start_x, start_y)])
    visited_1[start_y][start_x] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        x, y = queue.popleft()
        cur_letter = graph[y][x]
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if (
                0 <= new_x < n
                and 0 <= new_y < n
                and not (visited[new_y][new_x])
                and graph[new_y][new_x] == cur_letter
            ):
                visited[new_y][new_x] = 1
                queue.append((new_x, new_y))


n = int(sys.stdin.readline())
graph = [[] for _ in range(n)]
for j in range(n):
    line = sys.stdin.readline().rstrip()
    for i in range(n):
        graph[j].append(line[i])

visited_1 = [[0] * n for _ in range(n)]
visited_2 = [[0] * n for _ in range(n)]
answer_1 = 0
answer_2 = 0
for x in range(n):
    for y in range(n):
        if not (visited_1[y][x]):
            bfs(x, y, visited_1)
            answer_1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

for x in range(n):
    for y in range(n):
        if not (visited_2[y][x]):
            bfs(x, y, visited_2)
            answer_2 += 1
print(answer_1, answer_2)
