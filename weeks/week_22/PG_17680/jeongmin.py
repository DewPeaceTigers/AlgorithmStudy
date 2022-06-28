from collections import deque

def solution(cacheSize, cities):
    # 캐시를 적용하지 않은 경우
    if cacheSize==0:
        return len(cities)*5
    
    time = 0
    
    q = deque()
    
    for city in cities:
        # 소문자로 변경
        city = city.lower()
        
        # hit
        if city in q:
            q.remove(city)
            q.append(city)
            time += 1
            
        # miss
        else:
            # LRU 적용
            if len(q)==cacheSize:
                q.popleft()
            q.append(city)
            time += 5
    
    answer = time
    
    return answer