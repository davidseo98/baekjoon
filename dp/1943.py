import sys
import math

n = sys.stdin.readline()
while n:
    item_count = 0
    value = list()
    for _ in range(int(n)):
        v, c = map(int, sys.stdin.readline().split())
        for _ in range(c):
            value.append(v)
            item_count += 1
    weight = [1] * item_count
    value.sort()
    dp_table = [[0] * (item_count // 2 + 1) for _ in range(item_count + 1)]
    total_value = sum(value)
    half_value = total_value / 2
    if round(half_value) != int(half_value):
        print(0)
        continue
    is_pos = False
    for i in range(1, item_count + 1):
        for w in range(1, item_count // 2 + 1):
            if weight[i - 1] > w:
                dp_table[i][w] = dp_table[i - 1][w]
            else:
                dp_table[i][w] = max(
                    value[i - 1] + dp_table[i - 1][w - 1], dp_table[i - 1][w]
                )
            if dp_table[i][w] == int(half_value):
                is_pos = True
                print(1)
            if is_pos:
                break
        if is_pos:
            break
    if not (is_pos):
        print(0)
    for line in dp_table:
        print(line)
    n = sys.stdin.readline()
