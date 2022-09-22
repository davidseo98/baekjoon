import sys


def binary_search(x):
    global answer
    min_val = abs(x + alkali[0])
    start = 0
    end = len(alkali) - 1

    if end == 0:
        return min_val, x, alkali[0]

    while start < end:
        mid = (start + end) // 2
        if abs(x + alkali[mid]) < min_val:
            min_val = abs(x + alkali[mid])
            start = mid
        else:
            end = mid
    return min_val, x, alkali[mid]


n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
acid = list()
alkali = list()

for num in num_list:
    if num > 0:
        acid.append(num)
    else:
        alkali.append(num)

if not acid or not alkali:
    if not acid:
        alkali.sort()
        print(*alkali[n - 2 :])
    if not alkali:
        acid.sort()
        print(*acid[n - 2 :])
    exit()

# if len(acid) > len(alkali):
#     l1, l2 = alkali, acid
# else:
#     l1, l2 = acid, alkali

acid.sort()
alkali.sort()
answer = list()
if len(acid) > 1:
    answer.append((abs(sum(acid[:2])), acid[0], acid[1]))
if len(alkali) > 1:
    answer.append(
        (abs(sum(alkali[len(alkali) - 2 :])), alkali[len(alkali) - 2], alkali[-1])
    )

for x in acid:
    answer.append(binary_search(x))

answer.sort()
print(answer)
print(*sorted(answer[0][1:]))
