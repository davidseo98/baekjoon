import sys
from collections import Counter


def is_possible(height):
    global tree_dict
    tree_cut = 0
    for key in tree_dict.keys():
        if key > height:
            tree_cut += (key - height) * tree_dict[key]
    if tree_cut >= m:
        return 1
    else:
        return 0


n, m = map(int, sys.stdin.readline().split())
tree_dict = Counter(list(map(int, sys.stdin.readline().split())))

lo = 0
hi = max(tree_dict.keys())
answer = 0
cnt = 0
past_mid = 0
while 1:
    mid = (lo + hi) // 2
    if past_mid == mid:
        break
    if is_possible(mid):
        answer = mid
        lo = mid
    else:
        hi = mid

    past_mid = mid


print(answer)
