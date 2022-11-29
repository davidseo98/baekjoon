import sys

def dfs(loc):
    global s

    if len(s) == m and tuple(s) not in visited:
        print(*s)
        visited.add(tuple(s))
        return

    for i in range(loc, n):
        s.append(num_list[i])
        dfs(i + 1)
        s.pop()

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
s = []
visited = set()

dfs(0)