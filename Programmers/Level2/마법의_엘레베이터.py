# 구분 : Brute-Force 
# 

from itertools import product

def check(storey, commands):
    
    result = 0
    
    for index, flag in enumerate(commands):
        if index >= len(str(storey)): break

        # 현재 자리수
        cur = int(str(storey)[::-1][index])
        
        # 만약 참이면 trunc
        if flag:
            storey -= cur * (10 ** index)
            result += cur
        
        # 거짓이면 ceil
        else:
            storey += (10 - cur) * (10 ** index)
            result += (10 - cur)
        
    return result

def solution(storey):
    
    answer = []
    
    # 내림, 올림 모든 경우의 수 돌려서 필요한 돌의 개수 저장
    for candidate in product([1, 0], repeat = len(str(storey)) + 1):
        answer.append(check(storey, candidate))
        
    return min(answer)

if __name__ == "__main__":
    n = int(input())
    print(solution(n))