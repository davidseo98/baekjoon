n = int(input())
meetings = {}
meetings_list = []

for i in range(n) :
    s, e = map(int, input().split())
    if meetings.get(s) == None :
        meetings[s] = e
    else :
        if meetings[s] > e :
            meetings[s] = e
for key, value in meetings.items() :
    meetings_list.append([key, value])
meetings_list.sort(key = lambda x : x[0])

while(1) :
    overlap_cnt = [0 for _ in range(len(meetings_list))]
    for i in range(len(meetings_list)) :
        rest = [x for x in meetings_list if x != meetings_list[i]]
        start = meetings_list[i][0]
        end = meetings_list[i][1]
        for other_meeting in rest :
            if start<other_meeting[0]<end or start<other_meeting[1]<end or other_meeting[0]<start<other_meeting[1] :
                overlap_cnt[i] += 1
    print(overlap_cnt)
    print(meetings_list)
    if sum(overlap_cnt) == 0 :
        break
    max_overlap_loc = overlap_cnt.index(max(overlap_cnt))
    meetings_list.pop(max_overlap_loc)
    

print(len(meetings_list))