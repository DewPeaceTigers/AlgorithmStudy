import sys

input = sys.stdin.readline

n,k = map(int,input().split())
spaces = [list(map(int,input().split())) for _ in range(n)] # 0: 흰색, 1: 빨강, 2: 파랑
horses=[]
for _ in range(k):
    x,y,d = map(int,input().split())
    horses.append([x-1,y-1,d-1])
pos=[]
for _ in range(n):
    p=[]
    for _ in range(n):
        p.append([])
    pos.append(p)

for i, [x,y,d] in enumerate(horses):
    pos[x][y] = [i]

dx=[0,0,-1,+1]
dy=[+1,-1,0,0]

turn=0
nomoremoved=False
while turn<1000:
    turn+=1
    gameover=False
    nevermoved = True
    for i, [x,y,d] in enumerate(horses):
        if pos[x][y][0]!=i:
            # 현재 말이 가장 아래에 쌓여있는 말이 아닐 경우
            continue
        nx = x+dx[d]; ny=y+dy[d];
        if not(-1<nx<n and -1<ny<n) or spaces[nx][ny]==2: # 경계 밖이거나 파랑색일 경우 방향 반대로
            if d==0: d=1
            elif d==1: d=0
            elif d==2: d=3
            elif d==3: d=2
            nx = x + dx[d];
            ny = y + dy[d];
            horses[i]=[x,y,d]
            if not (-1 < nx < n and -1 < ny < n) or spaces[nx][ny] == 2: # 또라면
                continue
        if spaces[nx][ny]==0 : # 흰색일 경우
            pos[nx][ny].extend(pos[x][y])
            for h in pos[nx][ny]:
                horses[h][0] = nx
                horses[h][1] = ny
            pos[x][y]=[]
        elif spaces[nx][ny]==1: # 빨강일 경우
            pos[nx][ny].extend(reversed(pos[x][y]))
            for h in pos[nx][ny]:
                horses[h][0] = nx
                horses[h][1] = ny
            pos[x][y] = []
        nevermoved=False
        if len(pos[nx][ny])>=4:
            gameover=True
            break
    if gameover: break
    if nevermoved:
        nomoremoved=True
        break
if turn==1000 or nomoremoved: print(-1)
else: print(turn)