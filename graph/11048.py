import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
dp_table = [[0]*c for _ in range(r)]
dp_table[0][0] = graph[0][0]
for i in range(r):
    for j in range(c):
        
        if 0 < i: dp_table[i][j] = max(dp_table[i][j], graph[i][j] + dp_table[i - 1][j])
        if 0 < j: dp_table[i][j] = max(dp_table[i][j], graph[i][j] + dp_table[i][j - 1])
        if 0 < i and 0 < j : dp_table[i][j] = max(dp_table[i][j], graph[i][j] + dp_table[i - 1][j - 1])

print(dp_table[-1][-1])