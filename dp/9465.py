import sys

t = int(sys.stdin.readline())
for _ in range(t) :
    n = int(sys.stdin.readline())
    sticker_list = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0] * (n + 1) for _ in range(3)]
    
    for j in range(1, n + 1) :
        for i in range(1, 3) :
            if j == 1 :
                dp[i][j] = sticker_list[i - 1][j - 1]
                continue
            if i == 1 :
                dp[i][j] = sticker_list[i - 1][j - 1] + max(dp[i + 1][j - 1], dp[i][j - 2], dp[i + 1][j - 2])
            elif i == 2 :
                dp[i][j] = sticker_list[i - 1][j - 1] + max(dp[i - 1][j - 1], dp[i][j - 2], dp[i - 1][j - 2])
            
    print(max(dp[1][-1], dp[2][-1]))