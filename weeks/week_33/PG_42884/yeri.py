def solution(routes):
    routes.sort(key= lambda x:(x[1],x[0]))
    camera = routes[0][1]
    answer = 1
    for start,end in routes:
        if start > camera or camera > end:
            camera = end
            answer+=1
    return answer