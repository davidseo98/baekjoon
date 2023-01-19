# 구분 : 자료구조, 해싱

from collections import defaultdict

def solution(weights):
    
    possible = [2.0, 4/3, 3/2]
    answer = 0
    weight_dict = defaultdict(int)
    
    # weight의 개수를 딕셔너리에 저장 -> n을 가능한 weight의 개수인 901으로 제한
    for weight in weights:
        weight_dict[weight] += 1
    
    for key, item in weight_dict.items():
        # 동일한 weight로 쌍을 구성하는 경우
        num = weight_dict[key]
        answer += int(num * (num - 1) / 2)
        
        # 서로 다른 weight로 쌍을 구성하는 경우
        for mult in possible:
            value = key * mult
            if value.is_integer() and value in weight_dict.keys():
                answer += num * weight_dict[int(value)]

    return answer