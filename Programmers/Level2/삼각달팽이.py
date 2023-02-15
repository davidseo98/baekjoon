from collections import deque

def solution(n):
    result = []
    answer = {i : ["", ""] for i in range(n)}
    d = 0
    level = 0
    val = 1

    for i in range(n - 1, -1, -1):
        if d == 0:
            for j in range(level, level + i + 1):
                answer[j][0] += str(val) + "."
                val += 1
            level += i

        elif d == 1:
            for j in range(i + 1):
                answer[level][0] += str(val) + "."
                val += 1
            level -= 1
        else:
            for j in range(level, level - i - 1, -1):
                answer[j][1] = str(val) + "." + answer[j][1]
                val += 1
            level -= i - 1
            
        d = (d + 1) % 3

    for i in range(n):
        line = answer[i]
        for element in line[0].split("."):
            if element : result.append(int(element))
        for element in line[1].split("."):
            if element : result.append(int(element))
        
        
    return result