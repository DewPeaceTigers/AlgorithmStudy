#pypy 통과
import sys
from collections import deque
input=sys.stdin.readline

T=int(input())

for _ in range(T) :
    A, B=map(int, input().split())
    q=deque()
    q.append((A, ''))
    visit=[False]*10000
    while q :
        now, course=q.popleft()
        visit[now]=True
        if now==B :
            print(course)
            break

        #D
        tmp=(2*now)%10000
        if not visit[tmp] :
            q.append((tmp, course+'D'))
            visit[tmp] = True

        #S
        tmp=(now-1)%10000
        if not visit[tmp] :
            q.append((tmp, course+'S'))
            visit[tmp]=True

        #L
        tmp=(now//1000)+(now%1000)*10
        if not visit[tmp] :
            q.append((tmp, course+'L'))
            visit[tmp] = True

        #R
        tmp=(now//10)+(now%10)*1000
        if not visit[tmp]:
            q.append((tmp, course + 'R'))
            visit[tmp] = True