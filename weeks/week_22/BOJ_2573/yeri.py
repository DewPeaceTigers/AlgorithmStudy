import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
spaces=[list(map(int,input().split())) for _ in range(n)]
ices={}
dx=[0,0,-1,+1]
dy=[-1,+1,0,0]
for i in range(n):
    for j in range(m):
        if spaces[i][j]!=0:
            count=0
            for d in range(4):
                nx=i+dx[d]
                ny=j+dy[d]
                if not(-1<nx<n and -1<ny<m): continue
                if spaces[nx][ny]==0: count+=1
            ices[i,j]=count
# if len(ices)==0:
#     print(0)
#     sys.exit()
time=0
while True:
    time+=1
    isZero=[]
    for x,y in ices:
        spaces[x][y]-=ices[x,y] # 주위 0 개수만큼 내려감
        if spaces[x][y]<0:
            spaces[x][y]=0
        if spaces[x][y]==0:
            isZero.append((x,y))
    for x,y in isZero:
        # 0이되면 주위 칸에 0이 된 것이니
        ices.pop((x,y))
        for d in range(4): # 주위에 0개수 추가
            nx = x + dx[d]
            ny = y + dy[d]
            if not(-1<nx<n and -1<ny<m): continue
            if spaces[nx][ny]!=0: ices[nx,ny]+=1 # 주위 개수 올리기
    if len(ices)==0:
        # 빙산이 다 녹아서 분리되지 않음
        time=0
        break
    first = list(ices.keys())[0]
    q = deque([first])
    visit = [ [False]*m for _ in range(n)]
    visit[first[0]][first[1]]=True
    count=0
    while q:
        x,y = q.popleft()
        count+=1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not (-1 < nx < n and -1 < ny < m): continue
            if spaces[nx][ny] != 0 and not visit[nx][ny]:
                q.append((nx,ny))
                visit[nx][ny]=True
    if count != len(ices):
        # 서로 개수가 다르니 길이 나눠진 것
        break
print(time)