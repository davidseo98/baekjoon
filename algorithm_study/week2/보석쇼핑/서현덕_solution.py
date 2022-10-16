# DP? Two-Pointer?
"""
1. Unique한 보석 추출
2. 
"""
def solution(gems):
    n = len(gems)
    total_gem_set = set(gems)
    start, end, p_start, p_end = 0, 0, -1, -1
    best = float("inf")
    answer = list()
    while 1 :
        cur_gem_set = set(gems[start:end + 1])
        if cur_gem_set == total_gem_set :
            if end - start < best :
                best = end - start
                answer = [start + 1, end + 1]
            start += 1
        else :
            if end < n :
                end += 1
        if p_start == start and p_end == end :
            break
        
        p_start, p_end = start, end

    return answer