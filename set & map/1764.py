import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
not_heard = list()
not_seen = list()
for i in range(n):
    not_heard.append(sys.stdin.readline().rstrip())

for i in range(m):
    not_seen.append(sys.stdin.readline().rstrip())

both = set(not_heard) & set(not_seen)
both = sorted(list(both))
print(len(both))
for person in both:
    print(person)
