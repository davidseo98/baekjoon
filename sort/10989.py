import sys

n = int(sys.stdin.readline().rstrip())
num = [0] * 10001
for i in range(n):
    num[int(sys.stdin.readline().rstrip())] += 1

for i in range(len(num)):
    if num[i] != 0:
        for _ in range(num[i]):
            print(i)
