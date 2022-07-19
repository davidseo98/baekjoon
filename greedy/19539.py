import sys

n = int(sys.stdin.readline())
tree_list = list(map(int, sys.stdin.readline().split()))
div_list = list()
total = 0
for tree in tree_list:
    if tree % 3 != 0:
        div_list.append((tree, tree % 3))
        total += tree % 3
if total % 3 != 0:
    print("NO")
    exit()
div_list.sort(reverse=True)


print(div_list)
