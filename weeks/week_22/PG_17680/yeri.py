"""
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
deque(maxlen=cacheSize)<=아주 쉬워짐
"""
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque()
    for city in cities:
        city=city.lower()
        print(city,q,answer)
        if cacheSize==0:
            answer+=5
        else:
            if city not in q:
                # cache miss
                if len(q) == cacheSize:
                    q.popleft()
                answer+=5
                q.append(city)
            else:
                # cache hit
                q.remove(city)
                q.append(city)
                answer+=1
    return answer
