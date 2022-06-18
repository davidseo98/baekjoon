mid_equation = list(input())
rear_equation = ""
sign_stack = list()
for char in mid_equation:
    if char.isalpha():
        rear_equation += char
    else:
        if char == "*" or char == "/":
            while sign_stack and (sign_stack[-1] == "*" or sign_stack[-1] == "/"):
                rear_equation += sign_stack.pop()
            sign_stack.append(char)
        elif char == "+" or char == "-":
            while sign_stack and sign_stack[-1] != "(":
                rear_equation += sign_stack.pop()
            sign_stack.append(char)
        elif char == "(":
            sign_stack.append(char)
        elif char == ")":
            while sign_stack and sign_stack[-1] != "(":
                rear_equation += sign_stack.pop()
            sign_stack.pop()
while sign_stack:
    rear_equation += sign_stack.pop()

print(rear_equation)
