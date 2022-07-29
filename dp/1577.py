import sys

n, m = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
blocked_list = set()
for _ in range(t):
    a, b, c, d = map(int, sys.stdin.readline().split())
    if a < c or b < d:
        s_x, s_y, e_x, e_y = a, b, c, d
    else:
        s_x, s_y, e_x, e_y = c, d, a, b
    blocked_list.add((s_x, s_y, e_x, e_y))
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(0, n + 1):
    for j in range(0, m + 1):
        if i == 0 and j == 0:
            dp[i][j] = 1
            continue
        if i == 0:
            if (j - 1, i, j, i) in blocked_list:
                dp[i][j] = 0
                break
            else:
                dp[i][j] = dp[i][j - 1]
            continue
        if j == 0:
            if (j, i - 1, j, i) in blocked_list:
                dp[i][j] = 0
                break
            else:
                dp[i][j] = dp[i - 1][j]
            continue

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (j - 1, i, j, i) in blocked_list:
            dp[i][j] = dp[i - 1][j]
        elif (j, i - 1, j, i) in blocked_list:
            dp[i][j] = dp[i][j - 1]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
for line in dp:
    print(line)
print(dp[-1][-1])
