import sys

n, k = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
lo, best = 0, 0
sum = sum(num_list[:k])

for _ in range(n - k):
    sum = sum - num_list[lo] + num_list[lo + k]
    lo += 1
    if sum > best: best = sum

print(best)
