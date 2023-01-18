import math
from collections import defaultdict

def set_dp(n, num, dp):
    flag = True
    for i in range(n - 1, -1, -1):
        standard = 5 ** i
        value = int(math.ceil(num / standard))
        num -= (standard * (value - 1))
        dp[i + 1] = value

def solution(n, l, r):
    answer = 0
    dp = defaultdict(int)
    set_dp(n, l, dp)

    for i in range(l, r + 1):
        flag = True
        
        for key, item in dp.items():
            if item == 3:
                flag = False
                break
                
        if flag: answer += 1
        
        for level in range(1, n + 1):
            dp[level] += 1
            if dp[level] <= 5:
                break
            else:
                dp[level] -= 5
                
        
    return answer