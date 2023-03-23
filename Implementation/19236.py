import sys, copy

sys.setrecursionlimit(10000)

def move_fish():
    global fish_info, sea

    for fish in range(1, 17):
        if eaten[fish]: continue

        x, y, d = fish_info[fish]
        for i in range(8):
            nx, ny = x + dx[(d + i) % 8], y + dy[(d + i) % 8]
            if 0 <= nx < 4 and 0 <= ny < 4 and sea[nx][ny] != "S":
                
                # 만약 다른 물고기가 있다면
                if sea[nx][ny]:
                    nnum = sea[nx][ny]  # 해당 물고기의 번호 구하기
                    fish_info[nnum][0], fish_info[nnum][1] = x, y # 해당 물고기의 좌표를 현재 물고기의 좌표로 수정
                    sea[x][y] = nnum    # 바다에서도 이를 반영
                
                sea[nx][ny] = fish      # 현재 물고기 위치 변경
                fish_info[fish] = [nx, ny, (d + i) % 8] # 현재 물고기 정보 갱신

                break

def dfs(cnt, sea, fish_info):
    global answer

    move_fish()
    
    candidate = []
    sx, sy, sd = fish_info["S"]
    for len in range(1, 4):
        nx, ny = sx + len * dx[sd], sy + len * dy[sd]
        if 0 <= nx < 4 and 0 <= ny < 4 and sea[nx][ny]:

            candidate.append(sea[nx][ny])
    
    if not candidate:
        answer = max(cnt, answer)
        return

    for fish in candidate:
        eaten[fish] = True
        
        x, y, _ = fish_info[fish]
        sea[x][y] = 0

        fish_info_cp = copy.deepcopy(fish_info)
        sea_cp = copy.deepcopy(sea)

        dfs(cnt + fish, sea_cp, fish_info_cp)
        
        eaten[fish] = False

input = sys.stdin.readline

fish_info = dict()
sea = [[-1] * 4 for _ in range(4)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
eaten = [False] * (17)

for x in range(4):
    line = list(map(int, input().split()))
    for y in range(0, 8, 2):
        num, dir = line[y : y + 2]
        fish_info[num] = [x, y // 2, dir - 1]
        sea[x][y//2] = num

        if x == 0 and y == 0:
            eaten[num] = True
            sea[x][y//2] = "S"
            fish_info["S"] = [x, y, dir]
            
answer = 0

dfs(0, sea, fish_info)

print(answer)