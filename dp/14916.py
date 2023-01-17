import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

input = sys.stdin.readline

n = int(input())
dp_table = defaultdict(int)

def dp(num):
    global dp_table

    # Base case
    if num in [2, 5]: return 1
    if num in [1, 3]: return False

    # Use Memo
    if dp_table[num]: return dp_table[num]
    
    for change in [2, 5]:
        if num >= change:
            value = dp(num - change)
            if value != False: 
                if dp_table[num] == 0: dp_table[num] = value + 1
                else: dp_table[num] = min(dp_table[num], value + 1)
    
    return dp_table[num]

table = [100001] * 100001
table[2], table[5], table[4] = 1, 1, 2
for i in range(6, n + 1):
    table[i] = min(table[i], table[i - 2] + 1, table[i - 5] + 1)

if table[n] == 100001: print(-1)
else: print(table[n])

