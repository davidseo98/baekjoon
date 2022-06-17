import sys

input_string = sys.stdin.readline().rstrip()
pipe_stack = list()
result = 0

for i in range(len(input_string)):
    if input_string[i] == "(":
        pipe_stack.append(0)
    else:
        if input_string[i - 1] == "(":
            pipe_stack.pop()
            result += len(pipe_stack)
        else:
            pipe_stack.pop()
            result += 1

print(result)
