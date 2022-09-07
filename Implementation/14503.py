import sys


def check_left(x, y, d):
    global answer
    left_dir = (d - 1) % 4
    nx, ny = x + dx[left_dir], y + dy[left_dir]
    if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 0:
        graph[nx][ny] = 2
        answer += 1
        return 1, x, y, left_dir
    else:
        return 0, x, y, left_dir


def check_possible(x, y, d):
    original_dir = d
    for _ in range(4):
        check, x, y, d = check_left(x, y, d)
        if check:
            return 1, x + dx[d], y + dy[d], d

    back_dir = (original_dir + 2) % 4
    bx, by = x + dx[back_dir], y + dy[back_dir]
    if 0 <= bx < h and 0 <= by < w and graph[bx][by] == 2:
        return 2, bx, by, original_dir
    else:
        return 3, x, y, d


h, w = map(int, sys.stdin.readline().split())
start_x, start_y, start_dir = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
cur_x, cur_y, cur_dir = start_x, start_y, start_dir
answer = 0
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

graph[cur_x][cur_y] = 2
answer += 1

while 1:
    status, cur_x, cur_y, cur_dir = check_possible(cur_x, cur_y, cur_dir)
    if status == 3:
        break

print(answer)
