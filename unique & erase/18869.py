import sys

m, n = map(int, sys.stdin.readline().split())
input_list = list()
results = list()

for i in range(m):

    input_list = list(sys.stdin.readline().split())

    cnt = 0
    count_dict = dict()

    for planet in sorted(list(set(input_list)), key=int):  ############
        count_dict[planet] = cnt
        cnt += 1

    result = list()

    for planet in input_list:
        result.append(count_dict[planet])
    results.append(result)


count = -m
for i in range(m):
    for j in range(m):
        if results[i] == results[j]:
            count += 1
print(count // 2)
