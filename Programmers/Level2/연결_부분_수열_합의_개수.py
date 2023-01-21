# 구분 : 구현? 시뮬레이션?
# 소요시간 : 11분 47초

def solution(elements):
    numbers = set()
    for start in range(len(elements)):
        s = 0
        for dist in range(len(elements)):
            idx = (start + dist) % len(elements)
            s += elements[idx]
            if s not in numbers: numbers.add(s)

    return len(numbers)