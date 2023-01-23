# 구분 : brute-force, simulation
# 소요시간 : 대략 20분

def solution(word):

    string = ""
    next_dict = {"AEIOU"[i] : "AEIOU"[i + 1] for i in range(4)}
    cnt = 0
    
    while string != word:
        # 만약 5글자가 아니라면 A 추가
        if len(string) != 5 : string += "A"
        else:
            # 현재 글자 조합으로 마지막에 도달하면 모든 U 제거 후 마지막 글자 다음으로 변경
            if string[4] == "U":
                end = 4
                for s in string[::-1]:
                    if s == "U": end -= 1
                    else: break
                string = string[:end] + next_dict[string[end]]
            # 마지막에 도달할 때까지 마지막 글자를 다음 글자로 변경
            else: 
                string = string[:4] + next_dict[string[4]]
        cnt += 1
    return cnt