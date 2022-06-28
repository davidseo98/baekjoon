import sys

n = int(sys.stdin.readline())
line_list = list()
dp_table = [1] * (n + 1)
for _ in range(n):
    line_list.append(list(map(int, sys.stdin.readline().split())))

line_list.sort()

for i in range(n):
    cur_x, cur_y = line_list[i][0], line_list[i][1]
    max_dp = 0
    for j in range(i):
        if line_list[j][0] < cur_x and line_list[j][1] < cur_y and dp_table[j] > max_dp:
            max_dp = dp_table[j]
    dp_table[i] += max_dp

print(n - max(dp_table))
