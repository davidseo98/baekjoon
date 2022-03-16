n = int(input()) 
diffs = []
for i in range(n) :
    j = int(input())
    nums = sorted(list(map(int, input().split())))
    result = [0 for _ in range(j)] 
    end = j-1
    fnt_cnt = 0
    back_cnt = 0
    for m in range(j) :
        if m%2 == 0:
            result[fnt_cnt] = nums[m]
            fnt_cnt += 1
        else : 
            result[end-back_cnt] = nums[m]
            back_cnt +=1
    max_dif = 0
    for m in range(-1, j-1) :
        if abs(result[m]-result[m+1]) > max_dif :
            max_dif = abs(result[m]-result[m+1])
    diffs.append(max_dif)

for dif in diffs :
    print(dif)
