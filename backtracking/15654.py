import sys


def backtracking():
    if len(s) == m:
        print(*s)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        s.append(num_list[i])
        backtracking()
        s.pop()
        visited[i] = False


n, m = map(int, sys.stdin.readline().split())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
visited = [False] * n
s = list()

backtracking()
