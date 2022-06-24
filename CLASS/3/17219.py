import sys

n, m = map(int, sys.stdin.readline().split())
pass_dict = dict()
for _ in range(n) :
    site, pw = sys.stdin.readline().rstrip().split()
    pass_dict[site] = pw

for _ in range(m) :
    print(pass_dict[sys.stdin.readline().rstrip()])