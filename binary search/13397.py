import sys


def is_possible(mid):
    global num_list, n, m
    temp = [num_list[0]]
    count = 1
    for i in range(1, n):
        temp.append(num_list[i])
        diff = max(temp) - min(temp)
        if diff > mid:
            temp = [num_list[i]]
            count += 1
    if count <= m:
        return 1
    else:
        return 0


n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

hi = max(num_list)
lo = 0
answer = 1

while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        answer = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(answer)
