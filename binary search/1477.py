def is_possible(mid):
    global distances
    count = 0
    for dist in distances:
        if dist > mid:
            count += (dist - 1) // mid
    if count <= m:
        return 1
    else:
        return 0


n, m, l = map(int, input().split())
stations = list(map(int, input().split()))
stations.append(0)
stations.append(l)
stations.sort()
distances = list()
for i in range(n + 1):
    distances.append(stations[i + 1] - stations[i])

hi = l - 1
lo = 1
answer = lo

while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        answer = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(answer)
