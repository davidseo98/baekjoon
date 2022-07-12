import sys


def dfs(cur_loc):
    global answer
    if sum(case) == s and len(case) > 0:
        answer += 1
    for i in range(cur_loc, n):
        if visited[i]:  # 만약 이미 방문한 숫자라면 출력하지 않는다
            continue
        visited[i] = True  # 위 경우가 아니라면 방문처리 한다
        case.append(num_list[i])  # 출력 문자 리스트에 추가한다
        dfs(i)  # 재귀적으로 함수를 불러서 위 과정을 반복한다
        case.pop()  # 출력 문자 리스트를 초기화
        visited[i] = False  # 방문 기록을 초기화


n, s = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
case = list()
visited = [False] * n
answer = 0

dfs(0)

print(answer)
