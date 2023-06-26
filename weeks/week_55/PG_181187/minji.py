import math

def solution(r1, r2):
    answer = 0

    for x in range(1, r2 + 1):
        maxY = math.floor(math.sqrt(r2 ** 2 - x ** 2))
        minY = 0 if x > r1 else math.ceil(math.sqrt(r1 ** 2 - x ** 2))
        answer += maxY - minY + 1

    answer *= 4
    return answer