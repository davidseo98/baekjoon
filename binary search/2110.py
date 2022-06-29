import sys


def is_possible(mid):
    global houses
    count = 0
    diff = 0
    for i in range(n - 1):
        diff += houses[i + 1] - houses[i]
        if diff >= mid:
            count += 1
            diff = 0

    if count >= m - 1:
        return 1
    else:
        return 0


n, m = map(int, sys.stdin.readline().split())
houses = list()
for _ in range(n):
    houses.append(int(sys.stdin.readline()))
houses.sort()

lo = 1
hi = max(houses)
answer = lo

while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        answer = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(answer)
