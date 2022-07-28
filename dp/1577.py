import sys

n, m = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
blocked_list = set()
for _ in range(t):
    s_x, s_y, e_x, e_y = map(int, sys.stdin.readline().split())
    print(range(s_x, e_x + 1))
    print(range(s_y, e_y + 1))
    for x, y in zip(range(s_x, e_x + 1), range(s_y, e_y + 1)):
        blocked_list.add((x, y))
print(blocked_list)
