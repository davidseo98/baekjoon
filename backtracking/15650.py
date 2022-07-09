from itertools import combinations

n, m = map(int, input().split())
l = [x for x in combinations(list(range(1, n + 1)), m)]
for element in l:
    print(*element)
