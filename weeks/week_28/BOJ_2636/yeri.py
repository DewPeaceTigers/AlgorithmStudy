import sys
input = sys.stdin.readline

N, M = map(int,input().split())
board = []
sx,sy=-1,-1
for i in range(N):
    board.append(list(map(int,input().split())))
    for j in range(M):
        if board[i][j]==0 and sx == -1 and sy == -1:
            sx,sy = i,j
time=1
dx=[-1,0,+1,0]
dy=[0,-1,0,+1]
cnt=0
time=0
while True:
    q = [[sx,sy]]
    visited=[[False]*M for _ in range(N)]
    visited[sx][sy]=True
    nomore =True
    while q:
        x,y = q.pop()
        if board[x][y]==1:
            board[x][y]=0
            if nomore:
                # 치즈 개수 초기화
                # 치즈가 아직 남아있다.
                nomore = False
                cnt=0
            cnt+=1
            continue
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if not(-1<nx<N and -1<ny<M):continue
            if visited[nx][ny]: continue
            q.append([nx,ny])
            visited[nx][ny]=True
    if nomore : break
    time+=1
print(time)
print(cnt)