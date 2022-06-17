import sys

input_string = sys.stdin.readline()
pipe_stack = list()
total_pieces = 0

refined_input_list = list()
i = 0
while i < len(input_string) - 1:
    if input_string[i] == "(" and input_string[i + 1] == ")":
        refined_input_list.append("L")
        i += 2
    else:
        refined_input_list.append(input_string[i])
        i += 1
if i == len(input_string) - 1:
    refined_input_list.append(input_string[-1])

while refined_input_list[0] == "L":
    refined_input_list.pop(0)

for char in refined_input_list:
    if char == "(":
        pipe_stack.append(0)
    elif char == ")":
        pipe_num = pipe_stack.pop()
        total_pieces += pipe_num + 1
    elif char == "L":
        # pipe_stack = pipe_stack + ([1] * len(pipe_stack))
        for i in range(len(pipe_stack)):
            pipe_stack[i] += 1
print(total_pieces)
