import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

print(sorted(num_list)[k - 1])
