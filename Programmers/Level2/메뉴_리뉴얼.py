from itertools import combinations
from collections import Counter

# initial solution
def solution(orders, course):
    answer = []

    for c in course:
        result = set()
        max_cnt = 0
        for i in range(len(orders)):
            if len(orders[i]) < c: continue
            for cand in combinations(list(orders[i]), c):
                cnt = 1
                cand = set(cand)
                for j in range(len(orders)):
                    if i == j: continue
                    if cand.issubset(set(orders[j])): cnt +=1
                if cnt < 2: continue
                if cnt > max_cnt:
                    result = {"".join(sorted(list(cand)))}
                    max_cnt = cnt
                elif cnt == max_cnt: 
                    result.add("".join(sorted(list(cand))))
        answer += result
    
    return sorted(answer)

# refined solution

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        candidate = []
        for order in orders:
            candidate += combinations(sorted(order), c)
        most_ordered = Counter(candidate).most_common()
        result = [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]
        answer += ["".join(r) for r in result]
    
    return sorted(answer)