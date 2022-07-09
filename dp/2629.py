import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    num_list.append(-num_list[i])
num_list.sort()
print(num_list)

t = int(sys.stdin.readline())
test_list = list(map(int, sys.stdin.readline().split()))
dp_table = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
for i in range(1, 2 * n + 1):
    for w in range(1, 2 * n + 1):
        dp_table[i][w] = max(
            num_list[i - 1] + dp_table[i - 1][w - 1], dp_table[i - 1][w]
        )

for line in dp_table:
    print(line)
