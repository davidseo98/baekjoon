def solution(n, money):
    answer = 0
    dp = [[0] * (n + 1) for _ in range(len(money) + 1)]

    for i in range(1, len(money) + 1):
        m = money[i - 1]
        for amount in range(1, n + 1):
            dp[i][amount] += dp[i - 1][amount]
            
            if m == amount: dp[i][amount] += 1
            if m < amount: dp[i][amount] += dp[i][amount - m] 
            
    return dp[-1][-1]