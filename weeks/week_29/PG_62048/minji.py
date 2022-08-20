import math

def solution(w,h):
    answer=w*h
    answer-=math.gcd(w, h)*2*2
    return answer