import sys

n, limit = map(int, sys.stdin.readline().split())
item_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * (limit + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    cur_value = item_list[i - 1][1]
    cur_weight = item_list[i - 1][0]
    for j in range(1, limit + 1):
        if cur_weight <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight] + cur_value)
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[-1][-1])
