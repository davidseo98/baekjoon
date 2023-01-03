import sys, math

def is_prime(num):
    if num == 2: return True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 : return False
    return True

input = sys.stdin.readline
n = int(input())

# make prime number list
prime_num = [x for x in range(2, n + 1) if is_prime(x)]
lo, hi, count = 0, 0, 0
sum = prime_num[lo]
length = len(prime_num)

# two pointer algorithm to find count
while True:

    if sum == n:
        sum -= prime_num[lo]
        lo += 1
        count += 1
    elif sum < n:
        hi += 1
        if hi == length: break
        sum += prime_num[hi]
    else:
        sum -= prime_num[lo]
        lo += 1
    

print(count)