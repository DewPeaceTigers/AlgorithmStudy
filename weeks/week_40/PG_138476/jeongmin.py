# 귤의 개수 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값

def solution(k, tangerine):
    answer = 0
    
    # 크기별 개수 구하기
    info = {}
    for x in tangerine:
        if x in info:
            info[x] +=1
        else:
            info[x] = 1
    
    # 개수가 많은 순으로 정렬
    tangerine_sort = list(info.values())
    tangerine_sort.sort(reverse=True)
    
    # 서로 다른 종류의 수, 고른 귤의 개수
    kind, cnt = 0, 0
    while cnt < k :
        cnt += tangerine_sort[kind]
        kind += 1
    
    answer = kind
    
    return answer