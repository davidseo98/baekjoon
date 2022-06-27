import sys


def find_reloc(cur_x, cur_y):
    global start_x, start_y, end_x, end_y, value, result, moves_needed
    cnt = moves_needed
    for _ in range(cnt):
        if cur_x == start_x and cur_y < end_y:
            cnt -= 1
            cur_y += 1
            continue
        if cur_x == end_x and cur_y > start_y:
            cnt -= 1
            cur_y -= 1
            continue
        if cur_y == start_y and cur_x > start_x:
            cnt -= 1
            cur_x -= 1
            continue
        if cur_y == end_y and cur_x < end_x:
            cnt -= 1
            cur_x += 1
    result[cur_y][cur_x] = value


n, m, r = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = [[0] * m for _ in range(n)]
moves_needed = r % (2 * (n + m))

for i in range(min(n, m) // 2):
    start_x = 0 + i
    start_y = 0 + i
    end_x = (m - 1) - i
    end_y = (n - 1) - i

    for j in range(start_x, end_x):
        value = graph[start_y][j]
        find_reloc(j, start_y)

    for j in range(start_y, end_y):
        value = graph[j][end_x]
        find_reloc(end_x, j)

    for j in range(end_x, start_x, -1):
        value = graph[end_y][j]
        find_reloc(j, end_y)

    for j in range(end_y, start_y, -1):
        value = graph[j][start_x]
        find_reloc(start_x, j)


for line in result:
    for value in line:
        print(value, end=" ")
    print()
