import sys

input = sys.stdin.readline
n, m = map(int, input().split())
num_list = list(map(int, input().split()))

lo, hi = 0, 0
sum, best = num_list[lo], n + 1

while True:
    if sum >= m:
        best = min(best, hi - lo + 1)
        sum -= num_list[lo]
        lo += 1

    else:
        hi += 1
        if hi == n: break
        sum += num_list[hi]

print(0) if best == n + 1 else print(best)