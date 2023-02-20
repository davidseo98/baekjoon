import math

def get_runtime(s_time, e_time):
    s_hour, s_min = map(int, s_time.split(":"))
    e_hour, e_min = map(int, e_time.split(":"))
    runtime = (e_hour - s_hour) * 60 + (e_min - s_min)
    return runtime

def check_song(m, melody):
    if len(m) > len(melody): return False
    for i in range(len(melody) - len(m) + 1):
        if m == melody[i:i+len(m)]:
            if (i + len(m) < len(melody) and melody[i + len(m)] != "#") or i + len(m) == len(melody):
                return True

    
    return False

def get_melody(melody, time):
    
    cnt = 0
    temp = ""
    idx = 0
    while cnt != time :
        if idx == len(melody) - 1:
            temp += melody[idx]
        else:
            if melody[idx + 1] == "#":
                temp += melody[idx:idx+2]
                idx += 1
            else:
                temp += melody[idx]
        cnt += 1
        idx = (idx + 1) % len(melody)
    
    return temp
    
def solution(m, musicinfos):
    
    answer = []
    
    for i, music in enumerate(musicinfos):
        st, et, title, melody = music.split(",")
        time = get_runtime(st, et)
        sharp_cnt = melody.count("#")
        melody = get_melody(melody, time)
        if check_song(m, melody): answer.append([time, i, title])
    
    if not answer: return "(None)"
    
    return sorted(answer, key = lambda x : (-x[0], x[1]))[0][2]
    