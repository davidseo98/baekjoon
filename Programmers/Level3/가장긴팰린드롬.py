def is_possible(l, s):
    
    for idx in range(len(s) - l + 1):
        if l % 2 == 0 and s[idx : idx + l//2] == s[idx + l//2: idx + l][::-1]:
            return True
        if l % 2 == 1 and s[idx: idx + l//2] == s[idx + l//2 + 1: idx + l][::-1]:
            return True
    
    return False
            

def solution(s):
    answer = 0
    
    for l in range(len(s), 0, -1):
        if is_possible(l, s): return l
    
    return answer