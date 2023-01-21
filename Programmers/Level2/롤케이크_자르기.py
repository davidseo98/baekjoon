# 구분 : 자료구조?
# 소요시간 : 6분 22초

def solution(topping):
    answer = 0
    left, right = [0] * 10001, [0] * 10001
    l_count, r_count = 0, 0
    
    # 오른쪽 조각 토핑 종류 수 구하기
    for t in topping:
        if right[t] == 0: r_count += 1
        right[t] += 1
    
    # 자를 수 있는 경우의 수 순회
    for t in topping:
        
        if left[t] == 0: l_count += 1       # 왼쪽 조각에 새로운 토핑 등장
        left[t] += 1
        right[t] -= 1
        if right[t] == 0: r_count -= 1      # 오른쪽 조각에 토핑 없어짐
        
        if l_count == r_count :answer += 1
        
    return answer