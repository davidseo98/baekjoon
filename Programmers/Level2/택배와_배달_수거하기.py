def reduce(array, index, cap):
    while True:

        if cap < array[index]:
            array[index] -= cap
            return index
        
        elif cap == array[index]:
            index -= 1
            while index >= 0 and array[index] == 0:
                index -= 1
            return index
        
        else:
            cap -= array[index]
            index -= 1
        
        if index < 0 : return -1
        
def solution(cap, n, deliveries, pickups):
    answer = 0
    d_i, p_i = -1, -1
    
    for i in range(n - 1, -1, -1):
        if deliveries[i] and d_i == -1: d_i = i
        if pickups[i] and p_i == -1: p_i = i
        if p_i != -1 and d_i != -1: break
            
    while d_i >= 0 or p_i >=0:
        
        answer += (max(d_i, p_i) + 1) * 2
        
        d_i = reduce(deliveries, d_i, cap)
        p_i = reduce(pickups, p_i, cap)
        
    return answer
