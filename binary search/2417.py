
n = int(input())

def is_possible(mid):
    return (mid * mid >= n)


# 이분탐색을 진행할 구간 지정
lo = 0
hi = n
answer = lo

# 이분탐색 start
while lo <= hi:
    mid = (lo + hi) // 2
    
    if is_possible(mid):
        answer = mid
        hi = mid - 1
    else:
        lo = mid + 1
        
        
# 정답 출력
print (answer)