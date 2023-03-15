from collections import deque

def is_possible(heap, start, t, m, n):
    cur = start
    queue = deque([])
    for _ in range(1, n + 1):
        
        # 대기열 업데이트
        while heap and heap[-1][0] <= cur:
            queue.append(heap.pop())

        # 정원까지 탑승
        for _ in range(m):
            if queue:
                _, is_con = queue.popleft()
                if is_con: return True # 만약 콘이 탑승했다면 참 반환
        
        # 다음 셔틀버스 도착 시간 계산
        c_minute = cur % 100 
        c_hour = cur // 100
        
        add_hour = (c_minute + t) // 60     # 추가되는 시간 
        new_minute = (c_minute + t) % 60    # 남는 분
        
        cur = (c_hour + add_hour) * 100 + new_minute
        
        
    return False

def solution(n, t, m, timetable):
    
    heap = []
    for element in timetable:
        time = int("".join(element.split(":")))
        heap.append((time, 0))
    
    start = 900
    end = start + ((n - 1) * t) // 60 * 100 + ((n - 1) * t) % 60
    
    con_time = end
    while con_time >= 0:
        
        heap_cpy = heap[:]
        heap_cpy.append((con_time, 1))
        heap_cpy.sort(key = lambda x : (-x[0], -x[1]))
        if is_possible(heap_cpy, start, t, m, n):
            
            # 시간을 숫자에서 문자열로 변환하여 반환
            hour = str(con_time // 100)
            minute = str(con_time % 100)
            if len(hour) == 1: hour = "0" + hour
            if len(minute) == 1: minute = "0" + minute
            return hour + ":" + minute
        
        # 만약 특정 정각에서 1분을 빼야된다면
        if con_time % 100 == 0: 
            con_time -= 100 # 한시간을 빼고
            con_time += 59  # 59분을 더한다
        else: con_time -= 1