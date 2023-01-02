import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
count, sum = 0, num_list[left]

while right < n:

    if sum == m:
        count += 1
        sum -= num_list[left]
        left += 1

    elif sum < m:
        right += 1
        # 오른쪽 인덱스를 하나 더한 다음에 값을 더하기 때문에, 인덱스가
        # 범위를 초과하지 않는지 확인 필요
        if right == n : break
        sum += num_list[right]
        
    else:
        sum -= num_list[left]
        left += 1
    
print(count)