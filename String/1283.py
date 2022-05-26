def check_1(options, input):
    for i in range(len(input)):
        if input[i][0].lower() not in options:
            options.append(input[i][0].lower())
            input[i] = "[" + input[i][0] + "]" + input[i][1:]
            return " ".join(input)
    return 0


def check_2(options, input):
    full_input = " ".join(input)
    for i in range(len(full_input)):
        if full_input[i].lower() not in options:
            options.append(full_input[i].lower())
            full_input = (
                full_input[:i] + "[" + full_input[i] + "]" + full_input[i + 1 :]
            )
            return full_input
    return 0


n = int(input())
options = [" "]
inputs = list()
result = list()
for i in range(n):
    inputs.append(list(input().split()))

for input in inputs:
    a = check_1(options, input)
    if a:
        result.append(a)
    else:
        b = check_2(options, input)
        if b:
            result.append(b)
        else:
            result.append(" ".join(input))

for r in result:
    print(r)
