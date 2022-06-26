import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
dp_table = [0] * (n + 1)

for i in range(n):
    if i == 0:
        dp_table[i+1] = num_list[i]
    else:
        dp_table[i + 1] = dp_table[i] + num_list[i]
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(dp_table[end] - dp_table[start - 1])
