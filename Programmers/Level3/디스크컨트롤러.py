import heapq

def solution(jobs):
    
    heapq.heapify(jobs)
    
    n = len(jobs)
    answer = 0
    heap = []
    time, end = jobs[0][0], jobs[0][0]

    while True:
        
        previous = len(heap)
        
        # 현재 요청이 온 작업 heap에 추가
        while jobs and jobs[0][0] == time:
            cur = heapq.heappop(jobs)
            heapq.heappush(heap, (cur[1], cur[0]))
        
        # 만약 진행할 작업이 있고, 직전 작업이 끝난 경우
        if heap and time >= end:
            duration, _ = heapq.heappop(heap)
            end = time + duration
            answer += duration
        
        # 이번 타임이 시작했을 때 있었던 작업 대기 시간 추가
        answer += previous
        
        if len(heap) == 0 and len(jobs) == 0: break
        
        time += 1

    return answer//n