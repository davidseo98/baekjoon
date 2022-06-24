import sys

n = int(sys.stdin.readline())
num_list = list()
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        num_list.pop()
    else:
        num_list.append(num)

print(sum(num_list))
