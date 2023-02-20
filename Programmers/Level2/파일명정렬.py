import re

def solution(files):
    split_name = []
    head = re.compile(r"[\D]+[0-9]")
    number = re.compile(r"[0-9]+")
    for i, file in enumerate(files):
        h = head.match(file).group()[:-1]
        temp = number.findall(file)[0] 
        n = temp if len(temp) < 6 else temp[:5]
        split_name.append([h.upper(), int(n), i])
    
    split_name.sort(key = lambda x : (x[0], x[1]))
    
    answer = []
    for name in split_name:
        answer.append(files[name[2]])
    
    return answer