import sys

n = int(sys.stdin.readline())
num_set = set(map(int, sys.stdin.readline().rstrip().split()))

for num in sorted(list(num_set)):
    print(num, end=" ")
