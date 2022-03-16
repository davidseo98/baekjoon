n = int(input())
temp = []
result = {}
candidate = []
can_rm_cnt = []
final = []
cnt = 0
 
for i in range(n) :
    s, e = map(int, input().split())
    temp.append([s,e])

temp.sort(key=lambda x:x[0])
for item in temp :
    result[item[0]] = []
for item in temp :
    result[item[0]].append(item[1])

for key in result.keys() :
    result[key].sort()
    candidate.append([key, result[key][0]])

for c in candidate :
    print(c, ": ", c[1]-c[0])
#