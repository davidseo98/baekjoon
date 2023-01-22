# 구분 : brute-force

from itertools import combinations

def check_score(n1, n2, cards):
    visited = set()
    cur = n1
    count1, count2 = 0, 0
    while cur not in visited:
        visited.add(cur)
        count1 += 1
        cur = cards[cur - 1]
    
    cur = n2
    while cur not in visited:
        visited.add(cur)
        count2 += 1
        cur = cards[cur - 1]
    return count1 * count2

def solution(cards):
    answer = []
    for c1, c2 in combinations(range(1, len(cards) + 1), 2):
        answer.append(check_score(c1, c2, cards))
    return max(answer)