def find_length(string, num):
    temp = ""
    cur = string[:num]
    cnt = 1
    idx = num
    
    while idx <= len(string):
        
        # 다음에 주어진 길이의 문자열이 한칸 더 있는 경우
        if idx + num <= len(string):
            
            # 문자열 칸이 동일하다면
            if cur == string[idx:idx+num]:
                cnt += 1
                idx += num
                
            else:
                if cnt == 1:
                    temp += cur
                    
                else:
                    temp += str(cnt) + cur
                    
                cur = string[idx:idx + num]
                idx += num
                cnt = 1
        
        # 문자열이 한칸 길이만큼 남지 않았을 때
        else:
            if cnt == 1:
                    temp += cur
            else:
                temp += str(cnt) + cur
            temp += string[idx:]
            break
                
    
    return len(temp)
            

def solution(s):

    answer = len(s)
    
    for length in range(1, len(s)):
        answer = min(answer, find_length(s, length))
    
    return answer