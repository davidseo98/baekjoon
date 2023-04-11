import sys

def get_lines(board):

    groups = []
    for i in range(square_num // 2):
        line = []
        start_x, end_x = 0 + i, n - 1 - i
        start_y, end_y = 0 + i, m - 1 - i

        for x in range(start_x, end_x + 1):
            line.append(board[x][start_y])
        
        for y in range(start_y + 1, end_y + 1):
            line.append(board[end_x][y])

        for x in range(end_x - 1, start_x - 1, -1):
            line.append(board[x][end_y])

        for y in range(end_y - 1, start_y, -1):
            line.append(board[start_x][y])
        
        groups.append(line)
    
    return groups

def reconstruct(groups):
    temp = [[-1] * m for _ in range(n)]
    for i, line in enumerate(groups):

        start_x, end_x = 0 + i, n - 1 - i
        start_y, end_y = 0 + i, m - 1 - i
        idx = 0
        
        for x in range(start_x, end_x + 1):
            temp[x][start_y] = line[idx]
            idx += 1
        
        for y in range(start_y + 1, end_y + 1):
            temp[end_x][y] = line[idx]
            idx += 1

        for x in range(end_x - 1, start_x - 1, -1):
            temp[x][end_y] = line[idx]
            idx += 1

        for y in range(end_y - 1, start_y, -1):
            temp[start_x][y] = line[idx]
            idx += 1
    
    for line in temp:
        print(*line)

input = sys.stdin.readline

n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
square_num = min(n, m)
groups = get_lines(board)

for i in range(square_num // 2):
    line = groups[i]
    mod = r % len(line)
    new_line = line[-1:-mod-1:-1][::-1] + line[:len(line) - mod]
    groups[i] = new_line

reconstruct(groups)
