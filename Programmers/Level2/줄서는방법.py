# 구분 : 수학

import math

def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))
    for i in range(1, n + 1):
        value = math.factorial(n - i)
        idx = math.ceil(k / value) - 1
        answer.append(numbers[idx])
        numbers.pop(idx)
        k = k % value
    return answer