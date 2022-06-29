import sys


def is_possible(mid):
    global num_list
    result = 0
    for num in num_list:
        result += min(mid, num)
    if result <= total:
        return 1
    else:
        return 0


n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
total = int(sys.stdin.readline())

lo = 1
hi = max(num_list)
answer = lo

while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        answer = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(answer)
