import sys

n = int(sys.stdin.readline())
num_set = set(map(int, sys.stdin.readline().split()))
p = int(sys.stdin.readline())
prob_list = list(map(int, sys.stdin.readline().split()))

for prob in prob_list:
    if prob in num_set:
        print(1)
    else:
        print(0)
