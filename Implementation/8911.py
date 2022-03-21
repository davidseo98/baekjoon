
n = int(input())
state =[ (0,1), (1,0), (0,-1), (-1,0) ]
turn = {"R" : 1, "L" : -1}
square_size = []
for i in range(n) :
    width = [0]
    height = [0]
    loc = 0
    command = input()
    cur_loc = [0,0]
    for c in command :
        if c in turn.keys() :
            loc = (loc + turn[c])%4
        elif c == "F" :
            cur_loc[0] = cur_loc[0] + state[loc][0]
            cur_loc[1] = cur_loc[1] + state[loc][1]
        else :
            cur_loc[0] = cur_loc[0] - state[loc][0]
            cur_loc[1] = cur_loc[1] - state[loc][1]
        width.append(cur_loc[0])
        height.append(cur_loc[1])
    square_size.append((max(width)-min(width))*(max(height)-min(height)))
for size in square_size :
    print(size)