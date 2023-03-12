from collections import deque

import sys

input = sys.stdin.readline

T = int(input())

# A를 B로 변환
def calc(a, b):
    min_comm = ''
    min_length = 1e9

    q = deque([(a, '')])
    visited[a] = True
    while q:
        x, cmd = q.popleft()

        # A를 B로 바꿈!
        if x == b:
            if len(cmd) < min_length:
                min_length = len(cmd)
                min_comm = cmd
                return min_comm
              
        # D
        n = (x*2)%10000
        if not visited[n]:
            q.append((n, cmd+'D'))
            visited[n] = True

        # S
        n = (x-1)%10000
        if not visited[n]:
            q.append((n, cmd+'S'))
            visited[n] = True

        # L
        n = (x*10 + x//1000)%10000
        if not visited[n]:
            q.append((n, cmd+'L'))
            visited[n] = True

        # R
        n = ((x%10)*1000 + x//10)%10000
        if not visited[n]:
            q.append((n, cmd+'R'))
            visited[n] = True


for t in range(T):

    A, B = map(int, input().split())

    visited = [False] * 10000  

    print(calc(A, B))