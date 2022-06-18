alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
equation = list(input())
letter2value = dict()
value_stack = list()

for i in range(n):
    letter2value[alphabet[i]] = int(input())

for char in equation:

    if char in letter2value.keys():
        value_stack.append(letter2value[char])
    else:
        value_2 = value_stack.pop()
        value_1 = value_stack.pop()
        if char == "*":
            value_stack.append(value_1 * value_2)
        elif char == "/":
            value_stack.append(value_1 / value_2)
        elif char == "-":
            value_stack.append(value_1 - value_2)
        elif char == "+":
            value_stack.append(value_1 + value_2)

print("%.2f" % value_stack[0])
