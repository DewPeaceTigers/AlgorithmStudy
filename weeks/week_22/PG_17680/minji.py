'''
LRU 가장 최근에 사용안된 캐시는 다시 대기 상태로

'''
def solution(cacheSize, cities):
    answer = 0
    cache=[]
    for city in cities :
        #캐시의 사이즈가 0이면 cities 리스트의 길이만큼 cache miss 발생
        if cacheSize==0 : 
            answer+=len(cities)*5
            break
        
        if len(cache)==0 : #비어있으면 cache miss
            answer+=5
            cache.append(city.lower())
        else: #cache에 도시가 하나라도 있으면
            if city.lower() in cache : #cache에 현재 도시가 있는 경우(cache hit)
                answer+=1
                index=cache.index(city.lower()) #cache에서의 현재 도시의 index
                cache.append(cache.pop(index)) #가장 최근에 사용되었으니까 맨 뒤로(LRU 알고리즘)
            else: #cache에 현재 도시가 없는 경우(cache miss)
                answer+=5
                if(len(cache)==cacheSize) : #cachesize 초과되는 경우
                    cache.pop(0)
                    cache.append(city.lower())
                else :
                    cache.append(city.lower())
        
    return answer