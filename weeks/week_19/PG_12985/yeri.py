import math
def solution(n,a,b):
    time=1
    while True:
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        if a==b : break
        time+=1
    return time