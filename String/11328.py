import sys

n = int(sys.stdin.readline())
for _ in range(n):
    s1, s2 = sys.stdin.readline().rstrip().split()
    if len(s1) != len(s2):
        print("Impossible")
        continue
    l1, l2 = list(), list()
    for i in range(len(s1)):
        l1.append(s1[i])
        l2.append(s2[i])
    l1.sort()
    l2.sort()
    is_pos = True
    for i in range(len(s1)):
        if l1[i] != l2[i]:
            is_pos = False
            break
    if is_pos:
        print("Possible")
    else:
        print("Impossible")
