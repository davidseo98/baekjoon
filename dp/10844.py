import sys

n = int(sys.stdin.readline())

limit = 1000000000
dp = [[0] * (n + 1) for _ in range(12)]

for i in range(1, n + 1):
    for j in range(1, 11):
        if i == 1:
            if 2 <= j <= 10:
                dp[j][i] = 1
            continue
        dp[j][i] = dp[j - 1][i - 1] + dp[j + 1][i - 1]
answer = 0
for i in range(1, 12):
    answer += dp[i][-1]
print(answer)
