import sys

n = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
answer = 0
while sum(b) > 0:
    odd_count = 0
    for i in range(n):
        if b[i] % 2 == 0:
            continue
        else:
            b[i] -= 1
            odd_count += 1
    if odd_count:
        answer += odd_count
    else:
        for i in range(n):
            b[i] = b[i] // 2
        answer += 1
print(answer)
