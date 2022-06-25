import sys
from collections import deque


def fibo(num: int):
    global memo, one_cnt, zero_cnt
    length = len(zero_cnt)

    if length <= num :
        for i in range(length, num+1) :
            zero_cnt.append(zero_cnt[i-1] + zero_cnt[i -2])
            one_cnt.append(one_cnt[i-1] + one_cnt[i-2])
    print(f"{zero_cnt[num]} {one_cnt[num]}")

t = int(sys.stdin.readline())
for _ in range(t):
    zero_cnt = [1, 0, 1]
    one_cnt = [0, 1, 1]
    fibo(int(sys.stdin.readline()))