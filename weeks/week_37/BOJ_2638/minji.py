import sys
from collections import deque

input=sys.stdin.readline

n, m=map(int, input().split())

cheeses=[list(map(int, input().split())) for _ in range(n)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def bfs() :
    q=deque()
    q.append([0, 0])
    visit[0][0]=1
    while q :
        x, y=q.popleft()
        for i in range(4) :
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0 :
                if cheeses[nx][ny]>=1 :
                    cheeses[nx][ny]+=1
                else:
                    visit[nx][ny]=1
                    q.append([nx, ny])
time=0

while 1 :
    visit=[[0]*m for _ in range(n)]
    bfs()
    flag=0
    for i in range(n) :
        for j in range(m) :
            if cheeses[i][j]>=3 :
                cheeses[i][j]=0
                flag=1
            elif cheeses[i][j]==2 :
                cheeses[i][j]=1
    if flag==1 :
        time+=1
    else:
        break
print(time)