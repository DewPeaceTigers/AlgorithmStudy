from collections import deque
n, k=map(int, input().split())
MAX=100000
dist=[0]*(MAX+1)
def bfs():
    q=deque()
    q.append(n)
    while q:
        x=q.popleft()
        if x==k :
            print(dist[k])
            return
        if 0<=x+1<=MAX and dist[x+1]==0 : #걷기
            dist[x+1]=dist[x]+1
            q.append(x+1)
        if 0<=x-1<=MAX and dist[x-1]==0 : #걷기
            dist[x-1]=dist[x]+1
            q.append(x-1)
        if 0<=x*2<=MAX and dist[x*2]==0: #순간이동
            dist[x*2]=dist[x]+1
            q.append(x*2)


bfs()