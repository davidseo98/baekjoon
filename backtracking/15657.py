import sys


def backtracking(loc):
    if len(seq) == m:
        print(*seq)
        return

    for i in range(loc, n):
        seq.append(num_list[i])
        backtracking(i)
        seq.pop()


n, m = map(int, sys.stdin.readline().split())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
seq = list()
visited = list()
backtracking(0)
