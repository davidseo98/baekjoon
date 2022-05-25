n = int(input())
total_length = 2 * n - 1
for i in range(1, n + 1):
    star_count = 2 * i - 1
    one_side_count = (total_length - star_count) // 2
    print(" " * one_side_count + "*" * star_count)
