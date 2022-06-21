import sys


n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

num_set = set(num_list)
cnt = 0
count_dict = dict()
for num in sorted(list(num_set)):
    count_dict[num] = cnt
    cnt += 1

for num in num_list:
    print(count_dict[num], end=" ")
