from collections import deque
from itertools import product
from copy import deepcopy

def find_start(board, col, h):

    for i in range(h):
        if board[i][col]:
            return i, col
    return -1, -1

def bomb(board, col, w, h):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    x, y = find_start(board, col, h) # 해당 열에서 값이 있는 맨 윗 행의 좌표 구함
    if x == -1 and y == -1: return 0 # 만약에 열에 터트릴 벽돌이 없는 경우

    queue = deque([(x, y)])
    exploded = set()
    exploded.add((x, y))

    while queue:
        cx, cy = queue.popleft()
        # 벽돌의 폭파 범위를 모두 순회
        for l in range(board[cx][cy]):
            for i in range(4):
                nx, ny = cx + l * dx[i], cy + l * dy[i]
                if 0 <= nx < h and 0 <= ny < w and board[nx][ny] and (nx, ny) not in exploded:
                    exploded.add((nx, ny))
                    queue.append((nx, ny))

    return exploded

def update(board, exploded, w, h):
    # 폭파시키기 -> 0으로 만들기
    for x, y in exploded:
        board[x][y] = 0

    # 열을 기준으로 실행
    for col in range(w):
        zero_loc = 0
        row = h - 1
        # 맨 아래부터 맨 위에 행까지
        while row >= 0:
            # 벽돌이 현재 행에 존재하고, 아래에 폭파된 벽돌이 있는 경우
            if board[row][col] and zero_loc:
                board[zero_loc][col] = board[row][col] # 벽돌을 아래로 이동시킴
                board[row][col] = 0 # 현재 행에서 벽돌을 없앰
                row = zero_loc - 1  # 옮겨진 위치에서 한칸 높은 위치부터 다시 탐색
                zero_loc = 0        # 폭파된 벽돌 좌표도 reset
            # 벽돌이 없고, 0을 가르키는 좌표가 아직 지정되지 않았을 때
            elif not board[row][col] and not zero_loc:
                zero_loc = row
                row -= 1
            # (벽돌이 없고 0을 가르키는 좌표 있음) 또는 (벽돌이 있고, 0을 가르키는 좌표 없음) 
            else:
                row -= 1

def simulate(board, candidates, w, h):

    answer = float('inf')

    for c in candidates:
        cpy_board = deepcopy(board) # 원래 보드를 복제

        for col in c:
            exploded = bomb(cpy_board, col, w, h) # 터지는 좌표 구하기
            if not exploded: break # 폭파시킬 벽돌이 없는 경우, 폭탄을 낭비한 것으로 탐색 그만
            update(cpy_board, exploded, w, h) # 터진 좌표 압축하기

        cnt = 0
        # 남아있는 벽돌 개수 구하고, 정답 업데이트
        for i in range(h):
            for j in range(w):
                if cpy_board[i][j]: cnt += 1

        answer = min(answer, cnt)

    return answer


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]

    candidates = product(list(range(w)), repeat=n) # 가능한 모든 케이스 만들기
    answer = simulate(board, candidates, w, h) # 시뮬레이션 실행

    print(f"#{test_case} {answer}")
    # ///////////////////////////////////////////////////////////////////////////////////
