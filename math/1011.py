import sys


def find_least_cnt(s, f):
    target = f - s  # 이동해야 하는 거리
    threshold = 1  # 임계값
    addition = 1  # 추가하는 값
    answer = 1  # 최소 이동 횟수
    while 1:
        if target <= threshold:
            break
        if answer % 2 == 0:
            threshold += addition
            answer += 1
        else:
            threshold += addition
            addition += 1
            answer += 1
    return answer


n = int(sys.stdin.readline())
for _ in range(n):
    start, finish = map(int, sys.stdin.readline().split())
    print(find_least_cnt(start, finish))
