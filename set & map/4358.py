import sys

tree_dict = dict()
length = 0
while 1:
    tree_name = sys.stdin.readline().rstrip()
    if tree_name == "":
        break
    if tree_name not in tree_dict.keys():
        tree_dict[tree_name] = 1
    elif tree_name in tree_dict.keys():
        tree_dict[tree_name] += 1
    length += 1

result = list()
sorted_keys = sorted(tree_dict.keys())

for trees in sorted_keys:
    result.append((trees, round((tree_dict[trees] / length) * 100, 4)))

for i in result:
    print(f"{i[0]} {i[1]:.4f}")
