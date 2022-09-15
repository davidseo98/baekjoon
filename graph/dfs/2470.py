import sys


def dfs(loc):
    global s, minimum_value, n1, n2

    if len(s) == 2:
        total_value = sum(s)
        if abs(total_value) < minimum_value:
            n1, n2 = s[0], s[1]
            minimum_value = abs(total_value)
        return

    for i in range(loc, n):
        s.append(num_list[i])
        dfs(i)
        s.pop()


n = int(sys.stdin.readline())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
minimum_value = float("inf")
s = list()
n1, n2 = 0, 0
stop = False

dfs(0)

print(n1, n2)
