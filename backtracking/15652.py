import sys

def backtrack():
    if len(s) == m:
        string = " ".join(map(str, s))
        print(string)
        return
    for i in range(1, n + 1):
        if len(s) > 0 and s[-1] > i:
            continue
        s.append(i)
        backtrack()
        s.pop()


n, m = map(int, sys.stdin.readline().split())
s = list()
visited = set()

backtrack()
