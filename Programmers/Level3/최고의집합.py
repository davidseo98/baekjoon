def solution(n, s):

    if n > s: return [-1]

    mid = s // n
    remainder = s % n
    
    answer = [mid] * n
    for i in range(n - 1, n - remainder - 1, -1):
        answer[i] += 1
        
    return answer