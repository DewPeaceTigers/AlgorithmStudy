def solution(routes):
    answer = 0
    
    # 나간 시점 기준으로 정렬
    routes.sort(key = lambda x: x[1])
    
    # 카메라를 몇 대 설치해야하는지 저장
    result = 1
    # 카메라 설치 위치
    camera = routes[0][1]
    
    n = len(routes)
    for i in range(1, n):
        if routes[i][0] <= camera:
            continue
        camera = routes[i][1]
        result += 1
        
    answer = result
    
    return answer