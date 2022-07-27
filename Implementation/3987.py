import sys
from collections import deque


def bfs(x, y, direction):
    dir_name = {1: "U", 2: "R", 3: "D", 4: "L"}
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    queue.append((x, y, direction, 1))
    visited[y][x] = 0
    dir_dict_1 = {1: 2, 2: 1, 3: 4, 4: 3}
    dir_dict_2 = {1: 4, 2: 3, 3: 2, 4: 1}
    count = 0
    while queue:
        cur_x, cur_y, dir, cnt = queue.popleft()
        if count < cnt:
            count = cnt
        if visited[cur_y][cur_x] > 4:
            print(dir_name[direction])
            print("Voyager")
            exit()
        new_x, new_y = cur_x + dx[dir - 1], cur_y + dy[dir - 1]
        if 0 <= new_x < m and 0 <= new_y < n:
            if graph[new_y][new_x] == ".":
                queue.append((new_x, new_y, dir, cnt + 1))
            elif graph[new_y][new_x] == "/":
                queue.append((new_x, new_y, dir_dict_1[dir], cnt + 1))
            elif graph[new_y][new_x] == "\\":
                queue.append((new_x, new_y, dir_dict_2[dir], cnt + 1))
            visited[new_y][new_x] += 1
    return (direction, count)


n, m = map(int, sys.stdin.readline().split())
graph = [sys.stdin.readline().strip() for _ in range(n)]
start_x, start_y = map(int, sys.stdin.readline().split())
if graph[start_y - 1][start_x - 1] == "C":
    print("U")
    print(0)
    exit()
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
answer = [-1, -1]
dir_name = {1: "U", 2: "R", 3: "D", 4: "L"}
for i in range(4):
    d, c = bfs(start_x - 1, start_y - 1, i + 1)
    if c > answer[1]:
        answer[0] = dir_name[d]
        answer[1] = c

print(answer[0])
print(answer[1])
