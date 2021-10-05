def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        answer = 5 * len(cities)
        return answer
    
    for city in cities:
        # 대소문자 구분 -> 소문자로 통일
        city = city.lower()
        if cacheSize > len(cache):  # cache가 덜 찼으면,
            if city not in cache:   # cache miss
                cache.append(city)
                answer += 5
            else:   # cache hit
                cache.pop(cache.index(city))    # 새로 들어오는 city에 해당하는 index를 cache에서 삭제
                cache.append(city)
                answer += 1
        else:   # cache가 가득차서 LRU 알고리즘에 따라, 오래된 cache 부터 삭제
            if city not in cache:   # cache miss
                cache.pop(0)
                cache.append(city)
                answer += 5
            else:   # cache hit
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
    return answer