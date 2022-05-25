from copy import deepcopy


def add_unit(total, unit):
    global cur_loc
    unit_size = len(unit)
    for i in range(unit_size):
        total[i + cur_loc] += unit[i]
    return total


def skip_unit(total, unit):
    global cur_loc
    unit_size = len(unit)
    for i in range(unit_size):
        total[i + cur_loc] += [" " * unit_size]
    return total


def change_line(total, unit):
    global cur_loc
    unit_size = len(unit)
    for i in range(unit_size):
        total.append([])
    cur_loc += unit_size


def main_function(stage):
    global cur_loc
    global cnt
    global s
    global u

    cur_loc = 0
    add_unit(s, u)
    add_unit(s, u)

    change_line(s, u)
    add_unit(s, u)
    skip_unit(s, u)
    add_unit(s, u)

    change_line(s, u)
    add_unit(s, u)
    add_unit(s, u)
    add_unit(s, u)

    if cnt == stage:
        return
    else:
        u = deepcopy(s)
        cnt += 1
        main_function(stage)


n = int(input())
z = 0
while 1:
    if n // 3 != 0:
        n = n // 3
        z += 1
    else:
        break

s = [["*"]]
u = [["*"]]

cnt = 0
cur_loc = 0

main_function(z - 1)
for line in s:
    print("".join(line))
