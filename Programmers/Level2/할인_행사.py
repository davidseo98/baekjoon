# 구분 : 슬라이딩 윈도우
# 소요 시간 : 10분

def check(item_count):
    for _, item in item_count.items():
        if item > 0: return False
    return True

def solution(want, number, discount):
    answer = 0
    item_count = {want[i] : number[i] for i in range(len(want))}
    for i in range(len(discount)):
        
        if discount[i] in want: item_count[discount[i]] -= 1
        if i >= 10 and discount[i - 10] in want: item_count[discount[i - 10]] += 1
        
        if check(item_count): answer += 1

    return answer