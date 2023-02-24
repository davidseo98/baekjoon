def solution(A, B):
    answer = 0
    
    B.sort(reverse = True)
    A.sort()
    
    idx = len(A) - 1
    for b in B:
        
        while idx >= 0 and b <= A[idx]:
            idx -= 1
        
        if b > A[idx]: answer += 1
        
        idx -= 1
        if idx == -1: break
        
    return answer