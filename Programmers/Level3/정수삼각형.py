def solution(triangle):

    dp = [[0] * i for i in range(1, len(triangle) + 1)]
    dp[0][0] = triangle[0][0]
    
    for l in range(1, len(triangle)):
        for i in range(l + 1):
            if i == 0: dp[l][i] = dp[l - 1][0] + triangle[l][i]
            elif i == l: dp[l][i] = dp[l - 1][l - 1] + triangle[l][i]
            else:
                dp[l][i] = max(dp[l - 1][i - 1], dp[l - 1][i]) + triangle[l][i]

    return max(dp[-1])