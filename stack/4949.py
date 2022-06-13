import sys

all_inputs = list()
pairs = {")": "(", "]": "["}
single = ["(", "["]
need_pair = [")", "]"]

input_list = sys.stdin.readlines()
input_list = "".join(input_list).split(".")
input_list.pop()

for input in input_list:
    if input == "\n":
        continue
    stack = list()
    for i in range(len(input)):
        letter = input[i]
        if letter in single:
            stack.append(letter)
        elif letter in need_pair:
            try:
                past_letter = stack.pop()
                if past_letter == pairs[letter]:
                    continue
                else:
                    stack.append("dummyvalue")
                    break
            except:
                stack.append("dummyvalue")
                break
        else:
            continue
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
