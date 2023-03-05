import math

def solution(k, d):
    answer = 0

    for i in range(0, d + 1, k):
        y = math.floor(math.sqrt(d * d - i * i))
        answer += y // k + 1
    return answer