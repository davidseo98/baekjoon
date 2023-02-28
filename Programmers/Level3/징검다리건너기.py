def is_possible(mid, stones, k):
    cnt = 0
    for s in stones:
        if s < mid: cnt += 1
        else: cnt = 0

        if cnt == k: return False
    return True

def solution(stones, k):
    
    lo, hi = 0, max(stones)
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if is_possible(mid, stones, k):
            answer = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return answer