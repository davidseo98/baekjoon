import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

common_num = list()
while 1:
    is_divided = False
    for i in range(2, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            common_num.append(i)
            n, m = n // i, m // i
            is_divided = True
    if is_divided == False:
        break

max_common = 1
min_common = 1
for num in common_num:
    max_common *= num
print(max_common)
print(max_common * n * m)
