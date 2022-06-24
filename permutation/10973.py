import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
not_poss = True
for i in range(n - 1, 0, -1):
    if num_list[i] < num_list[i - 1]:
        for j in range(n-1, i-1, -1):
            if num_list[j] < num_list[i - 1]:
                num_list[i - 1], num_list[j] = num_list[j], num_list[i - 1]
                num_list = num_list[:i] + sorted(num_list[i:], reverse=True)
                not_poss = False
                break
    if not (not_poss):
        break

if not_poss:
    print(-1)
    exit()

for num in num_list:
    print(num, end=" ")
