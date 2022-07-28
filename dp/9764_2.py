import sys

t = int(sys.stdin.readline())
dp = [[0] * (2001) for _ in range(2001)]
for i in range(1, 2001):
    add = i + 2
    std = i + i + 1
    nxt_std = std + add
    count = 1
    for j in range(1, 2001):
        if i == j:
            dp[i][j] = 1
            continue
        if j >= nxt_std:
            std = nxt_std
            add += 1
            nxt_std = std + add
            count += 1
        if j >= std:
            dp[i][j] = count

for _ in range(t):
    num = int(sys.stdin.readline())
    answer = 0
    for i in range(1, 2001):
        answer += dp[i][num]
    print(answer)
