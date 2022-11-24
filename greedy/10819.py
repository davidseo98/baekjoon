import sys
from itertools import permutations

def eval(temp):
    score = 0
    for i in range(n - 1):
        score += abs(temp[i] - temp[i + 1])
    return score

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

answer = 0
for temp in permutations(num_list, n):
    cur = eval(temp)
    if answer < cur: answer = cur

print(answer)

