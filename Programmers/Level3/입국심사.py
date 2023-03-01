def get_cnt(time, times):
    cnt = 0
    for t in times:
        cnt += time // t
    return cnt

def solution(n, times):
    answer = 0
    lo, hi = 0, 10000000000000
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if get_cnt(mid, times) >= n:
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
        
    return answer