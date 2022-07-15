import sys

n_people, n_party = map(int, sys.stdin.readline().split())
know_set = set(sys.stdin.readline().split()[1:])
party_set = [set(sys.stdin.readline().split()[1:]) for _ in range(n_party)]
for party in party_set:
    if party & know_set:
        know_set = know_set.union(party)
answer = 0
for party in party_set:
    if party & know_set:
        continue
    answer += 1

print(answer)
