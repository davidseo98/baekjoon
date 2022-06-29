import sys


def is_possible(mid):
    global spending
    count = 1
    limit = mid
    for num in spending:
        if num > limit:
            limit = mid
            count += 1
            limit -= num

        else:
            limit -= num

    #     print(f"after using {num} money left is {limit} and count is {count}")
    #print(f"for mid {mid} count is {count}")
    if count <= m:
        return 1
    else:
        return 0


n, m = map(int, sys.stdin.readline().split())
spending = [int(sys.stdin.readline()) for _ in range(n)]

hi = sum(spending)
lo = max(spending)
answer = lo

while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        answer = mid
        hi = mid - 1
    else:
        lo = mid + 1
print(answer)
