# 구분 : 자료구조, 그리디
# 소요시간: 14분 35초

def solution(order):
    answer = 0      # 정답이자 인덱스 역할 수행
    conv = 1        # 컨베이어 벨트 (순서대로 상자가 전달되기 때문에 숫자로 설정 가능)
    sub_conv = []   # 보조 컨베이어 벨트

    while True:
        
        if answer == len(order): break 
        
        # 만약 현재 상자가 컨베이어 벨트 혹은 보조 컨베이어 벨트에 바로 있다면
        if order[answer] == conv: 
            answer += 1
            conv += 1
            continue
        elif sub_conv and order[answer] == sub_conv[-1]:
            answer += 1
            sub_conv.pop()
            continue
        
        # 컨베이어 벨트 나중에 필요한 상자가 있다면
        if order[answer] > conv:
            sub_conv.append(conv)
            conv += 1
        
        else:
            if sub_conv and order[answer] == sub_conv[-1]: 
                answer += 1
                sub_conv.pop()
            else: break

    return answer