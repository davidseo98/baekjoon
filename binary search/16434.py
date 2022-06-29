import sys
import math


def is_possible(mid):
    global rooms, init_attk
    player_attk = init_attk
    player_hp = mid

    for room in rooms:
        if room[0] == 1:
            monster_hp = room[2]
            if math.ceil(monster_hp / player_attk) <= math.ceil(
                player_hp / room[1]
            ):
                player_hp -= (math.ceil(monster_hp / player_attk) - 1) * room[1]
            else:
                return 0
        else:
            player_hp = min(mid, player_hp + room[2])
            player_attk += room[1]

    return 1


n, init_attk = map(int, sys.stdin.readline().split())
rooms = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
hi = 0
for room in rooms:
    if room[0] == 1:
        hi += room[1] * room[2]

lo = 1
answer = lo

while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        answer = mid
        hi = mid - 1
    else:
        lo = mid + 1
print(answer)
