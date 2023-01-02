import sys
import math

def check_prime(num):
    if num == 2 : return True

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

is_prime = [False] * 246913
for i in range(2, 246913):
    if check_prime(i):
        is_prime[i] = True

n = int(sys.stdin.readline())
while n:
    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if is_prime[i] : cnt += 1
    
    print(cnt)
    n = int(sys.stdin.readline())
