import sys

num = int(sys.stdin.readline())
if num < 4:
    if num == 1:
        print(1)
    elif num == 2:
        print(1)
    else:
        print(2)
    exit()
dp = [0] * (num + 1)
dp[1], dp[2], dp[3] = 1, 1, 2

for i in range(4, num + 1):
    dp[i] = sum(dp[: i - 1]) + 1
print(dp[num])
