import sys


def is_possible(mid):
    global desk_time, m
    people = 0
    for desk in desk_time:
        people += mid // desk
    if people >= m:
        return 1
    else:
        return 0


n, m = map(int, sys.stdin.readline().split())
desk_time = list()
for _ in range(n):
    desk_time.append(int(sys.stdin.readline()))

lo = 1
hi = max(desk_time) * m
answer = lo
desk_time.sort()
while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        answer = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(answer)
