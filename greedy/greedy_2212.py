import heapq as h
n = int(input()) 
k = int(input())
sensor_locs = list(map(int, input().split()))
sensor_locs.sort()
total = 0
if n <= k :
    print(0)
else :
    sensor_dis = []
    for i in range(n-1) :
        dif = sensor_locs[i+1]-sensor_locs[i]
        h.heappush(sensor_dis, dif)
    while(len(sensor_dis)+1 != k) :
        total += h.heappop(sensor_dis)
    print(total)
