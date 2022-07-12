import sys


def backtracking(loc):
    if len(seq) == m:
        print(*seq)
        return
    overlap = 0
    for i in range(loc, n):
        if visited[i] or overlap == num_list[i]:
            continue
        # visited[i] = True
        seq.append(num_list[i])
        overlap = num_list[i]
        backtracking(i)
        seq.pop()
        # visited[i] = False


n, m = map(int, sys.stdin.readline().split())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
seq = list()
visited = [False] * n
backtracking(0)
