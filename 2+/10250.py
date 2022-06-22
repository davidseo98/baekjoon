import sys
import math

test_num = int(sys.stdin.readline())
for _ in range(test_num):
    h, w, n = map(int, sys.stdin.readline().split())
    x = str(math.ceil(n / h))
    y = n % h
    if len(x) == 1:
        x = "0" + x
    if y == 0:
        y = h
    print(str(y) + str(x))
