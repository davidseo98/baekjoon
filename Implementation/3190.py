import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

c = int(input())
commands = defaultdict(int)
for _ in range(c):
    sec, dir = input().split()
    commands[int(sec)] = dir

dx = [0, 1, 0, -1] # R, D, L, U 순서
dy = [1, 0, -1, 0]

snake = deque([(0, 0)])
cur_sec, cur_dir = 1, 0

while True:

    cx, cy = snake[0]
    nx, ny = cx + dx[cur_dir], cy + dy[cur_dir]

    # 만약 벽이나 자기 자신에 부딛히면 게임 종료
    if not(0 <= nx < n) or not(0 <= ny < n) or (nx, ny) in snake:
        break

    snake.appendleft((nx, ny)) # 뱀의 머리 업데이트

    if not board[nx][ny]: # 만약 사과가 없다면 뱀의 꼬리 위치 제거
        snake.pop()
    else:
        board[nx][ny] = 0

    # 해당 시간에 명령이 있다면, 명령에 따라 반향 전환 
    if commands[cur_sec]:
        if commands[cur_sec] == 'D':
            cur_dir = (cur_dir + 1) % 4
        else:
            cur_dir = (cur_dir - 1) % 4
    
    cur_sec += 1

print(cur_sec)