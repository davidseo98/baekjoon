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

    x, y = find_start(board, col, h)
    if x == -1 and y == -1: return 0

    queue = deque([(x, y)])
    exploded = set()
    exploded.add((x, y))

    while queue:
        cx, cy = queue.popleft()

        for l in range(board[cx][cy]):
            for i in range(4):
                nx, ny = cx + l * dx[i], cy + l * dy[i]
                if 0 <= nx < h and 0 <= ny < w and board[nx][ny] and (nx, ny) not in exploded:
                    exploded.add((nx, ny))
                    queue.append((nx, ny))

    return exploded

def update(board, exploded, w, h):
    for x, y in exploded:
        board[x][y] = 0

    for col in range(w):
        zero_loc = 0
        row = h - 1

        while row >= 0:
            if board[row][col] and zero_loc:
                board[zero_loc][col] = board[row][col]
                board[row][col] = 0
                row = zero_loc - 1
                zero_loc = 0
            elif not board[row][col] and not zero_loc:
                zero_loc = row
                row -= 1
            else:
                row -= 1
def simulate(board, candidates, w, h):

    answer = float('inf')

    for c in candidates:
        cpy_board = deepcopy(board)
        not_possible = False

        for col in c:
            exploded = bomb(cpy_board, col, w, h) # 터지는 좌표 구하기
            if not exploded:
                not_possible = True
                break
            update(cpy_board, exploded, w, h)   # 터진 좌표 압축하기

        cnt = 0
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

    candidates = product(list(range(w)), repeat=n)

    answer = simulate(board, candidates, w, h)
    print(f"#{test_case} {answer}")
    # ///////////////////////////////////////////////////////////////////////////////////
