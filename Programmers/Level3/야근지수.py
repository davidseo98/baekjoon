import heapq

def solution(n, works):
    answer = 0
    works = [-x for x in works]
    heapq.heapify(works)
    for _ in range(n):
        heapq.heappush(works, heapq.heappop(works) + 1)
    
    for w in works:
        if w > 0: continue
        answer += w ** 2
    return answer