from collections import deque
def solution(routes):
    answer = 0
    routes.sort(key = lambda x:(x[1],x[0]))
    now = -30001
    for s,e in routes:
        if s<= now : continue
        else:
            now = e
            answer+=1
    return answer