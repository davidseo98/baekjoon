from itertools import combinations
#combinations는 순서를 고려하지 않은 조합
#permutations는 순서를 고려한 조합 (= 같은 값을 가지더라도 순서가 다르면 다른 경우의 수로 간주)
n, k = map(int, input().split(" "))
weight = []
value = []
total = []
for i in range(n) :
    w, v = map(int, input().split(" "))
    weight.append(w)
    value.append(v) 
    total.append([w,v])
print(weight, value)
cases = []
for i in range(n) :
    cases.append(list(combinations(total, i+1)))

