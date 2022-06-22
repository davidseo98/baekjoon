import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
cnt = len(num_list)
for num in num_list:
    for i in range(2, num):
        if num % i == 0:
            cnt -= 1
            break
if 1 in num_list:
    cnt -= 1
print(cnt)
