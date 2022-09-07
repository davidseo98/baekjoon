import sys


def dfs(loc):
    if len(num) == l:
        check1 = sum([(check in ["a", "e", "i", "o", "u"]) for check in num])
        check2 = len(num) - check1
        if check1 and check2 >= 2:
            print("".join(num))
        return

    for i in range(c):
        if visited[i] or i <= loc:
            continue
        num.append(letters[i])
        dfs(i)
        num.pop()


l, c = map(int, sys.stdin.readline().split())
letters = sorted(list(sys.stdin.readline().rstrip().split()))
visited = [False] * c
num = list()
dfs(-1)
