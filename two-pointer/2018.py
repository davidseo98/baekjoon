import sys 

n = int(sys.stdin.readline())
left, right, count = 0, 0, 0
sum = left + right

while right <= n:
    
    if sum == n:
        count += 1
        right += 1
        sum += right
    elif sum > n:
        # 값이 너무 커서 현재 배열의 첫번째 값을 뺴려고 하면, 먼저 뺴고, left를 그 다음에 줄여야 한다
        sum -= left 
        left += 1
    else :
        # 값이 너무 작아서 마지막 값의 다음 값을 더하려고 하면, right를 먼저 1 키우고 값을 더해야 한다.
        right += 1 
        sum += right

print(count + 1)