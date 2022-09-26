import sys


def dfs(loc):
    global s
    if len(s) == x:
        value = sum(s)
        if not visited[value]:
            visited[value] = True
        return

    for i in range(loc, n):
        s.append(num_list[i])
        dfs(i + 1)
        s.pop()


n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
s = list()
visited = [False] * (sum(num_list) + 2)
for i in range(1, n + 1):
    x = i
    dfs(0)

for i in range(1, sum(num_list) + 2):
    if not visited[i]:
        print(i)
        break
