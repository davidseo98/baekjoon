# 구분: 시뮬레이션

from collections import deque

def solution(queue1, queue2):
    
    queue1, queue2 = deque(queue1), deque(queue2)
    diff = sum(queue1) - sum(queue2)
    n = len(queue1)
    count = 0
    
    while diff != 0 and count <= n * 3:
        if diff < 0:
            diff += queue2[0] * 2
            queue1.append(queue2.popleft())
        else:
            diff -= queue1[0] * 2
            queue2.append(queue1.popleft())
        count += 1
    
    # 만약 길이 * 3만큼 순회 했는데도 동일하게 만들지 못했다면 -1
    if count == n * 3 + 1: return -1
    else: return count