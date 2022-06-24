import sys
import copy

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    num_list = list(range(1, n + 1))
    while k:
        num_list_cpy = copy.deepcopy(num_list)
        for i in range(n):
            num_list_cpy[i] = sum(num_list[: i + 1])
        num_list = num_list_cpy
        k -= 1

    print(num_list[-1])
