import sys

input = sys.stdin.readline

def get_seats(likes):

    seats = []
    for x in range(n):
        for y in range(n):
            if classroom[x][y]: continue
            like_cnt = 0
            empty_cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if classroom[nx][ny] == 0: empty_cnt += 1
                    if classroom[nx][ny] in likes: like_cnt += 1
            seats.append((-like_cnt, -empty_cnt, x, y))
    
    return seats

def get_satisfaction(students):
    cnt2val = {0 : 0, 1 : 1, 2 : 10, 3 : 100, 4 : 1000}
    result = 0
    for x in range(n):
        for y in range(n):
            like_cnt = 0
            likes = students[classroom[x][y]]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if classroom[nx][ny] in likes: like_cnt += 1
            result += cnt2val[like_cnt]
            
    return result


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n = int(input())
students = dict()

for _ in range(n ** 2):
    data = list(map(int, input().split()))
    students[data[0]] = data[1:]

classroom = [[0] * n for _ in range(n)]

for stu, likes in students.items():

    seats = get_seats(likes)
    seats.sort(key = lambda x : (x[0], x[1], x[2], x[3]))

    x, y = seats[0][2:]
    classroom[x][y] = stu

print(get_satisfaction(students))



