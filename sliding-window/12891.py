import sys
from collections import defaultdict

def check_pw(count_dict):
    for i, letter in enumerate(check):
        if count_dict[letter] < required[i]: return False
    return True

input = sys.stdin.readline

n, m = map(int, input().split())
string = input().rstrip()
required = list(map(int, input().split()))

check = ['A', 'C', 'G', 'T']
count_dict = defaultdict(int)
answer = 0

# 첫번째 부분 문자열 확인
for letter in ['A', 'C', 'G', 'T'] : count_dict[letter] = string[:m].count(letter)
if check_pw(count_dict): answer += 1

# 나머지 부분 문자열 확인
start, end = 0, m - 1
for i in range(1, n - m + 1):

    count_dict[string[start + i - 1]] -= 1
    count_dict[string[end + i]] += 1
    if check_pw(count_dict): answer += 1

print(answer)

