import sys


t = int(sys.stdin.readline())
for _ in range(t):
    answer = 1
    s, e = map(int, sys.stdin.readline().split())
    for _ in range(s):
        answer *= e
        e -= 1
    for _ in range(s):
        answer = answer // s
        s -= 1
    print(answer)
