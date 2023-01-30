def solution(s):
    answer = True
    stack = []
    for element in s:
        if element == "(":
            stack.append(element)
        else:
            if not stack: return False
            stack.pop()
    
    if stack: return False
    else: return True