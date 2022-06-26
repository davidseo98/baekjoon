n = int(input())
dp = [0] * 1001 
dp[1], dp[2] = 1, 3
if n <= 2 :
    print(dp[n])

for i in range(3, 1001) :
    dp[i] = dp[i-1] + dp[i-2] * 2
    if i == n :
        print(dp[n] % 10007)

