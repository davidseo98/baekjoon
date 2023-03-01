def rotate_key(key, m):
    temp = [[0] * m for _ in range(m)]
    for x in range(m):
        for y in range(m):
            temp[y][m - x - 1] = key[x][y]
    return temp

def check_key(key, dx, dy, m):

    for x in range(m):
        for y in range(m):
            u, d, l, r = x, x, y, y
            temp = [(x, y)]
            if key[x][y] == 1:
                for i in range(len(dx)):
                    nx, ny = x + dx[i], y + dy[i]

                    # 만약 홈의 위치에 돌기가 있다면
                    if 0 <= nx < m and 0 <= ny < m and key[nx][ny]:
                        temp.append((nx, ny))
                        u, d = min(u, nx), max(d, nx)
                        l, r = min(l, ny), max(r, ny)
            
            # 만약 모든 홈을 다 채울 수 있다면, 자물쇠와 겹치는 위치에 돌기가 없는지 확인
            if len(temp) == len(dx) + 1:
                is_pos = True
                for i in range(u, d + 1):
                    for j in range(l, r + 1):
                        if key[i][j] and (i, j) not in temp:
                            is_pos = False
                if is_pos: return True
    return False
                

def solution(key, lock):
    
    n, m = len(lock), len(key)
    dx, dy = [], []
    hole_locs = []

    for x in range(n):
        for y in range(n):
            if lock[x][y] == 0: hole_locs.append((x, y))
    
    if len(hole_locs) == 0:
        return True
    
    cx, cy = hole_locs.pop() # 기준이 되는 홈
    for x, y in hole_locs: 
        dx.append(x - cx)
        dy.append(y - cy)
    
    for _ in range(4):
        if check_key(key, dx, dy, m):
            return True
        key = rotate_key(key, m)
    
    return False