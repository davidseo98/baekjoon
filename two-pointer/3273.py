import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
x = int(input())

num_list.sort()
lo, hi, count = 0, n - 1, 0

while lo != hi:

    sum = num_list[lo] + num_list[hi]
    if sum == x: 
        count += 1
        lo += 1
    elif sum < x: lo += 1
    else: hi -= 1

print(count)