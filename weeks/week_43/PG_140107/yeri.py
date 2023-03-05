import math
def solution(k, d):
    answer=0
    for x in range(0,d+1,k):
        y = (d**2-x**2)**0.5
        answer+=math.ceil(y/k) + (1 if y%k == 0 else 0)
    return answer