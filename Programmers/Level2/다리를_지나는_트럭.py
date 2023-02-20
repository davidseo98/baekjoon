from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights[:])
    bridge = deque([0] * bridge_length)
    cur_w = 0

    while truck_weights or sum(bridge):
        out = bridge.popleft()
        bridge.append(0)
        cur_w -= out
        
        if truck_weights and cur_w + truck_weights[0] <= weight:
            bridge[-1] = truck_weights.popleft()
            cur_w += bridge[-1]
        answer += 1

    return answer