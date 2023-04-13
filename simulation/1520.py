import sys

def dfs():
    stack = [(0, 0)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while stack:
        cx, cy = stack.pop()
        dp[cx][cy] += 1

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] < board[cx][cy]:
                stack.append((nx, ny))


input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

dfs()

print(dp[-1][-1])