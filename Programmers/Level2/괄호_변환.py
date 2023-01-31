def eval(string):

    stack = []
    for letter in string:
        if letter == "(":
            stack.append(letter)
        else: 
            if stack: stack.pop()
            else: return False
    return True

def change(w):

    if eval(w) or not w: return w
    
    u, v, loc = w[0], "", 1
    while u.count("(") != u.count(")"):
        u += w[loc]
        loc += 1
    v = w[loc:]
    if eval(u): 
        return u + change(v)
    
    else:
        temp = "("
        temp += change(v)
        temp += ")"
        temp2 = ""
        for letter in u[1:len(u) - 1]:
            if letter == ")": temp2 += "(" 
            else: temp2 += ")"
        return temp + temp2
        
def solution(p):
    answer = change(p)
    return answer