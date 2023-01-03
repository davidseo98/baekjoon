import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))

lo, hi = 0, n - 1
best = 10e9

while lo < hi:

    add = liquid[hi] + liquid[lo]

    if abs(add) < best:
        best = abs(add)
        answer = [liquid[lo], liquid[hi]]
    
    if add <= 0: lo += 1
    else: hi -= 1

print(*answer)