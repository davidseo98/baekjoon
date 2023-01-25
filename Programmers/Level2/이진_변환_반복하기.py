def solution(s):
    zero_cnt = 0
    loop_cnt = 0
    
    while s != "1":
        one_cnt = s.count("1")
        zero_cnt += s.count("0")
        loop_cnt += 1
        s = bin(one_cnt)[2:]
    return [loop_cnt, zero_cnt]