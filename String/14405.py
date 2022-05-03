s = input()
wrong = 0
word = {"pi": 2, "ka": 2, "chu": 3}
cur_loc = 0
while True:
    if cur_loc == len(s):
        break
    right = 0
    for key in word.keys():
        next_loc = cur_loc + word[key]
        if s[cur_loc:next_loc] == key:
            cur_loc = next_loc
            right = 1
            break
    if right == 0:
        wrong = 1
        break


if wrong == 0:
    print("YES")

else:
    print("NO")
