import math

def solution(k, d):
    answer = 0
    
    r = d/k
    
    # (0, 0), (a*k, 0), (0, b*k) 개수
    cnt = 2*int(r) + 1
    
    # 위의 경우를 제외한 (a*k, b*k) 개수
    for i in range(1, math.ceil(r)):
        cnt += int(math.sqrt(r**2-i**2))

    answer = cnt

    return answer