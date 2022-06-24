import sys
import math


def check_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return 0
    return 1


start, end = map(int, sys.stdin.readline().split())
num_list = list(range(start, end + 1))
prime_list = list()

for num in num_list:
    if num == 1:
        continue
    if check_prime(num):
        prime_list.append(num)

for prime in prime_list:
    print(prime)
