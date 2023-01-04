import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pay = list(map(int, input().split()))

cur = sum(pay[:m])
best = cur
lo, hi = 0, m

while hi < n:
    
    cur = cur - pay[lo] + pay[hi]
    if cur > best: best = cur
    lo += 1
    hi += 1

print(best)