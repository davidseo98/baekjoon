import sys

n = int(sys.stdin.readline())
num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp_table = [[1000 * n] * 3 for _ in range(n + 1)]

dp_table[1][0], dp_table[1][1], dp_table[1][2] = (
    num_list[0][0],
    num_list[0][1],
    num_list[0][2],
)

for i in range(2, n + 1):
    for j in range(3):
        for m in range(3):
            if j == m:
                continue
            dp_table[i][j] = min(
                dp_table[i][j], num_list[i - 1][j] + dp_table[i - 1][m]
            )

print(min(dp_table[-1]))
