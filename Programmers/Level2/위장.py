# 해시
from collections import defaultdict

def solution(clothes):
    answer = 1
    c_dict = defaultdict(int)
    for name, key in clothes:
        c_dict[key] += 1
    
    for key, item in c_dict.items():
        answer *= (item + 1)
    
    return answer - 1