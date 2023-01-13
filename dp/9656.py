import sys

n = int(sys.stdin.readline())

def dp(total, cnt):
    global answer, memo

    if total == 0:
        answer.append(cnt)
        return 

    for coin in [2, 5]:
        leftover = total - coin
        if leftover >= 0: 
            dp(leftover, cnt + 1)
    
    return False

answer = []

dp(n, 0)
print(min(answer))