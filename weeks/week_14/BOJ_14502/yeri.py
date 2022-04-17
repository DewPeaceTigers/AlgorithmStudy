import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline
n,m=map(int,input().split())
spaces=[list(map(int,input().split())) for _ in range(n)]
virus=[]

for i, space in enumerate(spaces):
    for j, s in enumerate(space):
        if s == 2:
            virus.append([i,j])

def spread(q,spaces):
    dx=[-1,0,+1,0]
    dy=[0,-1,0,+1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i];
            if (-1<nx<n and -1<ny<m) and spaces[nx][ny]==0:
                spaces[nx][ny]=2
                q.append([nx,ny])
max_area=0
visited=[[False]*m for _ in range(n)]
def choose(cnt):
    global max_area
    if cnt==3:
        area=0
        temp=deepcopy(spaces)
        for v in virus:
            spread(deque([v]),temp)
        for t in temp :
            print(t)
            area+=t.count(0)
        print('--')
        max_area=max(area,max_area)
        return
    else:
        for i in range(n):
            for j in range(m):
                if spaces[i][j] ==0 :
                    spaces[i][j]=3
                    choose(cnt+1)
                    spaces[i][j]=0
choose(0)
print(max_area)

