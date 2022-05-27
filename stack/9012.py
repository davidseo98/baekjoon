n = int(input())

test_cases = list()
for i in range(n):
    test_cases.append(input())

for test_case in test_cases:
    stack = list()
    for i in range(len(test_case)):
        if test_case[i] == "(":
            stack.append("(")
        elif test_case[i] == ")":
            try:
                stack.pop()
            except:
                stack.append("dummyvalue")
                break

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
