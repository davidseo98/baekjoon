# 구분 : 다이나믹 프로그래밍

def solution(x, y, n):

    dp_table = [1000001] * (y + 1)
    dp_table[x] = 0
    
    for i in range(x, y + 1):
        if i % 3 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i // 3] + 1)
        if i % 2 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i // 2] + 1)
        dp_table[i] = min(dp_table[i], dp_table[i - n] + 1)
    
    if dp_table[y] == 1000001: return -1
    else: return dp_table[y]