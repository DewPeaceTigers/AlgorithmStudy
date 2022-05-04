import sys
from copy import deepcopy

input = sys.stdin.readline

m,n,h=map(int,input().split())

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

tomato_groups=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
ripeds=[]
noTomato=0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato_groups[i][j][k]==1: ripeds.append([i,j,k])
def checkAllRiped():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if(tomato_groups[i][j][k])==0: return False
    return True
day=0
while True:
    if checkAllRiped(): break
    else:
        if not ripeds:
            day=-1
            break
        else:
            day+=1
            new=[]
            for x,y,z in ripeds:
                for d in range(6):
                    nx=x+dx[d]; ny=y+dy[d]; nz=z+dz[d];
                    if not(-1<nx<h and -1<ny<n and -1<nz<m): continue
                    if tomato_groups[nx][ny][nz]==0:
                        tomato_groups[nx][ny][nz]=1
                        new.append([nx,ny,nz]) # 새로 익은 애들
            ripeds=new #deepcopy(new)
print(day)
# 1. 모두 익었는지 체크
# 2. 이전에 익은 토마토가 있는 지 확인
    # 3-1. 없다면 모두 익지 못하는 경우이니 -1 출력
    # 3-2. 해당 익은 토마토들로 익히기
