import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
sum_list = [0] * (n + 1)
all_minus = True
for i in range(n - 1, -1, -1):
    if num_list[i] >= 0:
        sum_list[i] = sum_list[i + 1] + num_list[i]
        all_minus = False
    else:
        if abs(num_list[i]) < sum_list[i + 1]:
            sum_list[i] = sum_list[i + 1] + num_list[i]
            all_minus = False

if all_minus:
    print(max(num_list))
else:
    print(max(sum_list))
