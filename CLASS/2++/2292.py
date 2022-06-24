import sys

n = int(sys.stdin.readline())

if n == 1:
    print(1)
    exit()

cnt = 0
standard = 1
while 1:
    if standard >= n:
        break
    cnt += 1
    standard += cnt * 6

print(cnt + 1)
