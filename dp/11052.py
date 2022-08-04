import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    cur_num = num_list[i - 1]
    for j in range(1, n + 1):
        if j < i:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - i] + cur_num, cur_num * (j // i))
print(dp[-1][-1])
