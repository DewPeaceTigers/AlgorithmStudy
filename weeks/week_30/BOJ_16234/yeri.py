import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int,input().split())
A = [ list(map(int,input().split())) for _ in range(N) ]

day = 0
dx = [-1,0,1,0]
dy = [0,-1,0,1]
while True:
    isMove = False
    visit = [[False]*N for _ in range(N)]
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                union = A[i][j]
                q = deque([[i,j]])
                list_union = deque([[i,j]])
                visit[i][j]=True
                while q:
                    x,y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if not(-1<nx<N and -1<ny<N) or visit[nx][ny]: continue
                        if L<=abs(A[x][y]-A[nx][ny])<=R:
                            isMove = True
                            visit[nx][ny] = True
                            union+=A[nx][ny]
                            q.append([nx,ny])
                            list_union.append([nx,ny])
                share = union//len(list_union)
                for x,y in list_union:
                    temp[x][y] = share
    if not isMove : break
    day+=1
    for i in range(N):
        A[i] = temp[i][:]
print(day)