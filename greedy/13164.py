import sys


n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
diff_list = list()
for i in range(n - 1):
    diff_list.append(num_list[i + 1] - num_list[i])
print(sum(sorted(diff_list, reverse=True)[m - 1 :]))
