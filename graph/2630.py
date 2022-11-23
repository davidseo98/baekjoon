import sys
sys.setrecursionlimit(1000000)

def check_paper(sx, sy, len):
    global WHITE, BLUE
    val_type = graph[sx][sy]
    for x in range(sx, sx + len):
        for y in range(sy, sy + len):
            if graph[x][y] != val_type:
                new_len = len // 2
                for next in [[sx, sy], [sx, sy + new_len], [sx + new_len, sy], [sx + new_len, sy + new_len]]:
                    check_paper(next[0], next[1], new_len)
                return
    
    if val_type == 1: BLUE += 1
    else: WHITE += 1




n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
WHITE = 0
BLUE = 0

check_paper(0, 0, n)
print(WHITE)
print(BLUE)