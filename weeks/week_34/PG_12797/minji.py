import math

'''
def solution(n, stations, w):
    answer = 0
    start = 1

    for s in stations:
        answer += max(math.ceil((s - w - start) / (2 * w + 1)), 0)
        start = s + w + 1

    if n >= start:
        answer += max(math.ceil((n - start + 1) / (2 * w + 1)), 0)

    return answer
'''
from collections import deque

arr=deque([1, 2, 3, 4, 5])
arr.rotate(1) #시계방향회전
print(arr)