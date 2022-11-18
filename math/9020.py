import sys
import math

def is_prime(num):
    if num == 1: return 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1

def eval(num):
    n1, n2 = -1, -1

    # 절반만 확인 -> 갈 수록 숫자간 차이가 작아진다 -> 자연스럽게 n1, n2이 업데이트 되면 차이가 작아진다.
    for i in range(2, num//2 + 1):
        a, b = i, num - i
        if numbers[a] and numbers[b]:
            n1, n2 = a, b
    
    return n1, n2

# 소수 판별을 중복해서 하지 않기 위해 미리 결과를 판별해서 저장
numbers = [False] * 10001
for i in range(2, 10001):
    if is_prime(i): numbers[i] = True


t = int(sys.stdin.readline())
for _ in range(t):
    num = int(sys.stdin.readline())
    n1, n2 = eval(num)

    # 만약 소수 조합이 나타나지 않은 경우
    if n1 == -1 and n2 == -1:
        print(-1)
        continue

    print(min(n1, n2), max(n1, n2))