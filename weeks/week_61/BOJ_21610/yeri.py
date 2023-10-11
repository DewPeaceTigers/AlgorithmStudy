import sys
from collections import deque,defaultdict
input = sys.stdin.readline

N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
clouds = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
dx =[0,-1,-1,-1,0,1,1,1]
dy =[-1,-1,0,1,1,1,0,-1]

for time in range(M):
    d, s = map(int,input().split())
    d-=1
    grow = []
    visited = [[False]* N for _ in range(N)]
    while clouds:
        r,c = clouds.pop()
        nr = (N+r+dx[d]*s)%N
        nc = (N+c+dy[d]*s)%N
        A[nr][nc]+=1
        grow.append([nr,nc])
        visited[nr][nc] = True

    for r,c in grow:
        cnt = 0
        for d in range(1,8,2):
            nr = r+dx[d]
            nc = c+dy[d]
            if (-1<nr<N and -1<nc<N) and A[nr][nc] !=0: cnt+=1
        A[r][c] += cnt
        
    for i in range(N):
        for j in range(N):
            if A[i][j]>=2 and visited[i][j]==False:
                clouds.append([i,j])
                A[i][j]-=2
result = 0
for a in A: result+= sum(a)
print(result)