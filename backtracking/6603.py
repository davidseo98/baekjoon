import sys

def dfs(loc):
    if len(s) == 6:
        print(*s) 
        return

    for i in range(loc, len(num)):
        s.append(num[i])
        dfs(i + 1)
        s.pop()

num_list = []
s = []
while True:

    num = list(map(int, sys.stdin.readline().split()))
    if num[0] == 0:
        break

    num = num[1:]
    num.sort()

    dfs(0)

    print()

    