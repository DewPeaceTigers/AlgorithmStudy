'''
현재 위치의 약수 중에 자기자신을 제외한 수
소수이면 무조건 1
그외에는 자기 자신을 제외한 가장 큰 약수
'''
import math


def check(n):
    if n == 1:
        return 0

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0 and n // i <= 10000000:
            return n // i
    return 1


def solution(begin, end):
    answer = []

    for i in range(begin, end + 1):
        k = 1
        if i == 1:
            k = 0
        for j in range(2, math.floor(math.sqrt(i)) + 1):
            if i % j == 0:
                if i // j <= 10000000:
                    k = i // j
                    break
                else:
                    k = j
        answer.append(k)

    return answer