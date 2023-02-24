import heapq

def get_removed(routes):

    heap = []
    max_len = 0
    for i, r in enumerate(routes):

        while heap and heap[0][0] < r[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, (r[1], i))
        
        if len(heap) > max_len:
            result = heap[:]
    
    return result
    
def remove(remove_idx, routes):
    for _, idx in sorted(remove_idx, key = lambda x:x[1], reverse=True):
        routes.pop(idx)
        
def solution(routes):
    answer = 0
    routes.sort()
    
    while routes:
        remove_idx = get_removed(routes)
        remove(remove_idx, routes)
        answer += 1
        
    return answer