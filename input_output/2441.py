n = int(input())
for i in range(n, 0, -1):
    white_space = n - i
    print(" " * white_space + "*" * i)
