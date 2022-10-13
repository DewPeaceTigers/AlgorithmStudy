def solution(routes):
    answer = 0
    
    # 나간 지점 오름차순 정렬
    routes.sort(key=lambda x:x[1])
    
    cnt = 1
    camera = routes[0][1]
    for route in routes:
        if camera < route[0]:
            # 카메라 수 1 증가
            cnt += 1
            camera = route[1]
    
    answer = cnt
    
    return answer