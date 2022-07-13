import sys
import math

n, l = map(int, sys.stdin.readline().split())
puddles = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
puddles.sort()

covered_end = puddles[0][0]
answer = 0
for puddle in puddles:
    start = puddle[0]
    end = puddle[1]
    if covered_end > end:
        continue
    if covered_end < start:
        covered_end = start
    cnt = math.ceil((end - covered_end) / l)
    answer += cnt
    covered_end += cnt * l

print(answer)
