import sys
import bisect


def lower_bound(value, length):
    global line_list
    lo = 0
    hi = length
    while lo < hi:
        mid = (lo + hi) // 2
        if line_list[mid] < value:
            lo = mid + 1
        else:
            hi = mid
    return hi


n = int(sys.stdin.readline())
line_list = list(map(int, sys.stdin.readline().split()))

dp_table = [line_list[0]]

for i in range(n):
    cur_value = line_list[i]
    if dp_table[-1] < cur_value:
        dp_table.append(cur_value)
    else:
        # idx = lower_bound(cur_value, len(dp_table))
        idx = bisect.bisect_left(dp_table, cur_value)
        dp_table[idx] = cur_value

print(n - len(dp_table))
