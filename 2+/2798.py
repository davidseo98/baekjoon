import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
candidate = [sum(x) for x in combinations(num_list, 3) if sum(x) <= m]
print(max(candidate))
