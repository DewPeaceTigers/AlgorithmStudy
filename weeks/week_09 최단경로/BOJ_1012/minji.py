import sys
T=int(input())
dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]
def bfs(x, y):
    queue=[[x, y]]
    while queue:
        x, y=queue.pop(0)
        for i in range(4) :
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and box[nx][ny]==1 :
                box[nx][ny]=0
                queue.append([nx, ny])
for i in range(T) :
    M, N, K=map(int, input().split())
    box=[[0]*M for i in range(N)]
    count=0
    for j in range(K) :
        a, b=map(int, sys.stdin.readline().split())
        box[b][a]=1
    for x in range(N) :
        for y in range(M) :
            if box[x][y]==1:
                bfs(x, y)
                box[x][y]=0
                count+=1
    print(count)

