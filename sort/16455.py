import heapq


def kth(a: list, k: int) -> int:
    dif = len(a) - k
    
    return sorted(a)[k - 1]
