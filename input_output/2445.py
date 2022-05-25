n = int(input())
total_length = 2 * n
for i in range(1, n + 1):
    white_space = total_length - 2 * i
    print("*" * i + " " * white_space + "*" * i)

for i in range(n - 1, 0, -1):
    white_space = total_length - 2 * i
    print("*" * i + " " * white_space + "*" * i)
