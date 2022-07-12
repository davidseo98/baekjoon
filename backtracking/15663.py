import sys


def backtracking():
    if len(seq) == m:
        print(*seq)
        return
    overlap = 0
    for i in range(n):
        if visited[i] or overlap == num_list[i]:
            continue
        seq.append(num_list[i])
        visited[i] = True
        overlap = num_list[i]
        backtracking()
        visited[i] = False
        seq.pop()


n, m = map(int, sys.stdin.readline().split())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
seq = list()
visited = [False] * n
backtracking()
