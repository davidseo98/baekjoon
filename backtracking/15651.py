def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for i in range(1, n + 1):
        if visited[i]:  # 만약 이미 방문한 숫자라면 출력하지 않는다
            continue
        # visited[i] = True  # 위 경우가 아니라면 방문처리 한다
        s.append(i)  # 출력 문자 리스트에 추가한다
        dfs()  # 재귀적으로 함수를 불러서 위 과정을 반복한다
        s.pop()  # 출력 문자 리스트를 초기화
        visited[i] = False  # 방문 기록을 초기화


n, m = map(int, input().split())
s = []
visited = [False] * (n + 1)

dfs()
