import sys

n = int(sys.stdin.readline())
num_list = list(sys.stdin.readline().split())

for i in range(n - 1, 0, -1):
    if num_list[i] > num_list[i - 1]:
        for j in range(n - 1, 0, -1):
            if num_list[i - 1] < num_list[j]:
                num_list[i - 1], num_list[j] = num_list[j], num_list[i - 1]

                find = True
                break
        if find:
            num_list = num_list[:i] + sorted(num_list[i:])
            print(*num_list)
            break

if not (find):
    print(-1)
