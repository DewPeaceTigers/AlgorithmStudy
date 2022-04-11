import sys
input=sys.stdin.readline

N,M=map(int,input().split())
box=[list(map(int,input().split())) for _ in range(N)]
#visited=[[False]*M for _ in range(N)]
def dfs(mino,sum):
    # 전부 다 검색해봐야할때, 가장 큰 값을 이용해서 현재 만들 수 있는 가장 큰 값과 max를 비교하면 가지치기가 가능하다.
    global max_num
    dx=[-1,0,+1,0]
    dy=[0,-1,0,+1]
    if len(mino)==4:
        max_num=max(max_num,sum)
    else:
        x,y=mino[-1]
        for i in range(4):
            nx=x+dx[i]; ny=y+dy[i];
            if  [nx,ny] not in mino and (-1<nx<N and -1<ny<M):
                mino.append([nx,ny])
                dfs(mino,sum+box[nx][ny])
                mino.pop()
        if len(mino)==3:
            x,y=mino[1] # 중앙 # ㅗ 모양
            for i in range(4):
                nx=x+dx[i]; ny=y+dy[i];
                if [nx,ny] not in mino and (-1<nx<N and -1<ny<M):
                    mino.append([nx,ny])
                    dfs(mino,sum+box[nx][ny])
                    mino.pop()

max_num=0
for i in range(N):
    for j in range(M):
        #visited[i][j]=True
        dfs([[i,j]],box[i][j])
print(max_num)
