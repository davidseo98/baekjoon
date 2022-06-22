import sys

n, k = map(int, sys.stdin.readline().split())
num_list = list(range(1, n + 1))
result = list()
loc = k - 1
while num_list:
    result.append(num_list.pop(loc))
    if len(num_list) == 0:
        break
    loc = (loc + k - 1) % len(num_list)

print("<" + ", ".join(map(str, result)) + ">")
