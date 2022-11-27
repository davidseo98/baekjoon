import sys

def dfs():

    if len(s) == k and tuple(s) not in visited:
        print(*s)
        visited.add(tuple(s))
        return
    
    if len(s) > k: return

    for i in range(n):
        s.append(num_list[i])
        dfs()
        s.pop()


n, k = map(int, sys.stdin.readline().split())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
s = []
visited = set()

dfs()

