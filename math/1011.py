from re import S
import sys


def find_least_cnt(s, f):
    target = f - s
    num = 1
    answer = float("inf")
    while 1:
        cur_val = num * (num + 1)
        diff = target - cur_val
        if cur_val > target:
            break
        answer = min(answer, 2 * num + diff)
        num += 1
    print(answer)


n = int(sys.stdin.readline())
for _ in range(n):
    start, finish = map(int, sys.stdin.readline().split())
    find_least_cnt(start, finish)
