import sys

n, c = map(int, sys.stdin.readline().rstrip().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
count_dict = dict()
result = list()

for num in num_list:
    if num not in count_dict.keys():
        count_dict[num] = 1
    else:
        count_dict[num] += 1

for key in count_dict.keys():
    result.append((key, count_dict[key]))

result.sort(key=lambda x: x[1], reverse=True)

for r in result:
    for _ in range(r[1]):
        print(r[0], end=" ")
