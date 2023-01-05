import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
asc, dsc = [1] * (n + 1), [1] * (n + 1)

for i in range(1, n):
    
    if num_list[i] >= num_list[i - 1]: asc[i + 1] = asc[i] + 1
    if num_list[i] <= num_list[i - 1]: dsc[i + 1] = dsc[i] + 1

print(max(max(asc), max(dsc)))