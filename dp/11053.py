import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
dp_table = [1] * (n + 1)
for i in range(n):
    cur_value = num_list[i]
    max_dp = 0
    for j in range(0, i):
        if num_list[j] < cur_value and dp_table[j + 1] > max_dp:
            max_dp = dp_table[j + 1]
    dp_table[i + 1] += max_dp
print(max(dp_table))
