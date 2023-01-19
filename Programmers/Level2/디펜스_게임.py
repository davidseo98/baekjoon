# 구분 : 자료구조 (힙)

import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    for e in enemy:
        
        heapq.heappush(heap, -e)
        
        # 만약 더 이상 적을 막아낼 수 없는 수준에 도달
        if e > n:
            # 남아있는 스킬이 없다면 끝
            if k == 0: break
            
            biggest = -heapq.heappop(heap)
            # 누적된 적 중 가장 많은 경우에 스킬을 쓰더라도 막지 못한다면 끝
            if n - e > biggest: break
            
            # 스킬 사용 반영
            n += (biggest - e)
            k -= 1
        
        else:
            n -= e
            
        answer += 1
    return answer