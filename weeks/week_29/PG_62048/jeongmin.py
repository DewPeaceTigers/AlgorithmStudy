"""
풀이 참고.. https://blog.itcode.dev/posts/2021/12/27/programmers-a0069

최종적인 일반식
(w * h) - (((w / gcd) + (h / gcd) - 1) * gcd)
= (w * h) - (w + h - gcd)
"""

import math

def solution(w,h):

    answer = w*h - (w+h-math.gcd(w,h))
    
    return answer