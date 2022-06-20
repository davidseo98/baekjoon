import sys

n, m = map(int, input().split())
l1 = list(map(int, sys.stdin.readline().rstrip().split()))
l2 = list(map(int, sys.stdin.readline().rstrip().split()))
diff1 = set(l1) - set(l2)
diff2 = set(l2) - set(l1)
print(len(diff1) + len(diff2))
