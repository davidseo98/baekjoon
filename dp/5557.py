import sys


answer = 0
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
dp_table = [[0] * 21 for _ in range(n)]
dp_table[1][num_list[0]] = 1
for i in range(1, n - 1):
    for j in range(0, 21):

        if dp_table[i][j]:

            if j - num_list[i] >= 0:
                dp_table[i + 1][j - num_list[i]] += dp_table[i][j]

            if j + num_list[i] <= 20:
                dp_table[i + 1][j + num_list[i]] += dp_table[i][j]

print(dp_table[-1][num_list[-1]])
