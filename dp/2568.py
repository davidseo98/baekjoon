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
        if line_list[j][0] < cur_x and line_list[j][1] < cur_y:
            dp_table[i] = max(dp_table[i], dp_table[j] + 1)

print(n - max(dp_table))

max_dp = max(dp_table)
max_dp_idx = dp_table.index(max_dp)

lis = list()
for i in range(n - 1, -1, -1):
    if dp_table[i] == max_dp:
        lis.append(line_list[i])
    max_dp -= 1

result = list()
for line in line_list:
    if line not in lis:
        result.append(line[0])

for num in sorted(result):
    print(num)
