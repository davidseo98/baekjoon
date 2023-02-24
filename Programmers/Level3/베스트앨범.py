from collections import defaultdict
import heapq

def solution(genres, plays):
    answer = []
    genre2music = defaultdict(list)
    genre_cnt = defaultdict(int)
    for i in range(len(genres)):
        g = genres[i]
        genre2music[g].append((plays[i], i))
        genre_cnt[g] += plays[i]
                
    ordered_genre = [(value, key) for key, value in genre_cnt.items()]
    ordered_genre.sort(reverse = True)
    
    for _, genre in ordered_genre:
        musics = genre2music[genre]
        musics.sort(key = lambda x : (-x[0], x[1]))
        answer.append(musics[0][1])
        if len(musics) > 1:
            answer.append(musics[1][1])
    
    return answer