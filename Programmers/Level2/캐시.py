# 구분 : 해싱

def solution(cacheSize, cities):
    answer = 0
    cache = dict()
    for city in cities:
        city = city.upper()
        if city not in cache.keys():
            answer += 5
        else:
            answer += 1
            
        if len(cache.keys()) < cacheSize:
            cache[city] = 0
        else:
            if city in cache.keys():
                cache[city] = 0
            else:
                cache[city] = 0
                cur = [(key, item) for key, item in cache.items()]
                cur.sort(key = lambda x : x[1])
                cache.pop(cur[-1][0])
                
        for key in cache.keys():
            cache[key] += 1
    return answer