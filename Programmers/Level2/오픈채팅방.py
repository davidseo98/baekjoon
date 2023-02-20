# 구분 : 해싱

def solution(record):
    answer = []
    temp = []
    id2name = dict()
    for r in record:
        c = r.split()
        if c[0] == "Enter":
            id2name[c[1]] = c[2]
            temp.append([c[1], "님이 들어왔습니다."])
        elif c[0] == "Leave":
            temp.append([c[1], "님이 나갔습니다."])
        else:
            id2name[c[1]] = c[2]

    for line in temp:
        line[0] = id2name[line[0]]
        answer.append("".join(line))
    return answer