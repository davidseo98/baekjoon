def solution(k, d):
    answer = 0
    candidate = [(x * k) ** 2 for x in range(d // k + 1)]
    
    n = len(candidate)
    start, end = 0, n - 1
    
    while start <= end:

        if candidate[start] + candidate[end] <= d ** 2:
            answer += (1 + (end - start) * 2)
            start += 1
        else:
            end -= 1

    return answer
