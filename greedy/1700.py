import sys

n, m = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
item_use = [0] * (max(items) + 1)
for item in items:
    item_use[item] += 1
cur_use = set()
cnt = 0
for i in range(len(items)):
    item = items[i]
    if len(cur_use) < n and item not in cur_use:
        cur_use.add(item)
    if item in cur_use:
        item_use[item] -= 1
        continue
    removed = False
    if len(cur_use) == n:
        furthest = -1
        furthest_item = -1
        for use in cur_use:
            if use in items[i:] and furthest < items[i:].index(use):
                furthest = items[i:].index(use)
                furthest_item = use
            if item_use[use] == 0:
                cur_use.remove(use)
                removed = True
                break
        if not (removed):
            cur_use.remove(furthest_item)
        cur_use.add(item)
        cnt += 1
    item_use[item] -= 1
print(cnt)
