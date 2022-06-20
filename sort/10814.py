import sys

n = int(sys.stdin.readline().rstrip())
result = list()
for _ in range(n):
    s = list(sys.stdin.readline().rstrip().split())
    result.append((int(s[0]), s[1]))

result.sort(key=lambda x: x[0])
for r in result:
    print(r[0], r[1])
