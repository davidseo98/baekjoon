import sys

n = int(sys.stdin.readline())
people = list()
for _ in range(n):
    people.append(list(map(int, sys.stdin.readline().split())))

ranking_list = [0] * n

cnt = 0
for person in people:
    for other_person in people:
        if person[0] < other_person[0] and person[1] < other_person[1]:
            ranking_list[cnt] += 1
    cnt += 1

for rank in ranking_list:
    print(rank + 1, end=" ")
