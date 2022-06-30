import sys
import heapq

n = int(sys.stdin.readline())
positive = list()
negative = list()
zero_count = 0
one_count = 0

for _ in range(n):
    num = int(sys.stdin.readline())
    if num > 1:
        positive.append(num)
    elif num == 1:
        one_count += 1
    elif num == 0:
        zero_count += 1
    else:
        negative.append(num)

result = one_count
positive.sort()
negative = sorted(negative, reverse=True)

while 1:
    if len(positive) == 1:
        result += positive[0]
        break
    elif len(positive) == 0:
        break
    num1 = positive.pop()
    num2 = positive.pop()
    result += num1 * num2

while 1:
    if len(negative) == 1:
        if zero_count > 0 :
            break
        result += negative[0]
        break
    elif len(negative) == 0:
        break
    num1 = negative.pop()
    num2 = negative.pop()
    result += num1 * num2

print(result)
