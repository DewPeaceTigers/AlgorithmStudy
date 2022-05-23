import sys
from collections import deque

input = sys.stdin.readline

F,S,G,U,D = map(int,input().split())

visits = [False]*(F+1)
visits[S]=True
q = deque([[S,0]])

while q:
    now, count = q.popleft()
    print(now,count)
    if now == G: break

    if now+U <= F and not visits[now+U]:
        q.append([now + U, count+1])
        visits[now+U]=True
    if now-D > 0 and not visits[now-D]:
        q.append([now - D, count+1])
        visits[now-D]=True
if now == G : print(count)
else : print("use the stairs")