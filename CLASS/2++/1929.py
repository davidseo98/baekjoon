import sys

start, end = map(int, sys.stdin.readline().split())
result = list()
num_list = list(range(start, end + 1))

for i in range(start, end+1) :
    



is_even = True if start % 2 == 0 else False

for i in range(start, end + 1):
    if is_even:
        is_even = not (is_even)
        continue
    is_even = not (is_even)
    for j in range(2, i):
        is_prime = True
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i)
