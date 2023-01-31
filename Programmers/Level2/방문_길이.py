from collections import defaultdict

def solution(dirs):
    answer = 0
    visited = defaultdict(int)
    move = {"L" : (0, -1), "R" : (0, 1), "D" : (-1, 0), "U" : (1, 0)}
    cr, cc = 0, 0
    for d in dirs:
        dr, dc = move[d]
        nr, nc = cr + dr, cc + dc
        if -5 <= nr <= 5 and -5 <= nc <= 5:
            if not visited[(cr, cc, nr, nc)] and not visited[(nr, nc, cr, cc)]: 
                answer += 1
                visited[(cr, cc, nr, nc)] = 1
                visited[(nr, nc, cr, cc)] = 1
            cr, cc = nr, nc
    return answer