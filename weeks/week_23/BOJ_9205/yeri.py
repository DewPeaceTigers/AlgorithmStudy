import sys
import math
from collections import deque

input = sys.stdin.readline


def getDist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


tests = int(input())

for _ in range(tests):
    n = int(input())

    home = list(map(int, input().split()))
    convs = [list(map(int, input().split())) for _ in range(n)]
    fest = list(map(int, input().split()))

    visit = [False]*(n+1)
    q = deque()
    q.append(home)
    isOk=False

    while q:
        x,y = q.popleft()
        if getDist([x,y],fest) <= 1000:
            isOk=True
            break
        for i in range(n):
            if not visit[i]:
                nx, ny = convs[i]
                if getDist([x,y],[nx,ny]) <= 1000:
                    q.append([nx,ny])
                    visit[i]=True
    if isOk : print('happy')
    else : print('sad')