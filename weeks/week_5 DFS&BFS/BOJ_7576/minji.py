import sys
from collections import deque

M, N=map(int, input().split())
tomatos=[]
# 상하좌우
dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]
queue=deque()
answer=0
for i in range(N) :
    tomatos.append(list(map(int, sys.stdin.readline().split())))

#익은 토마토가 있는 곳 위치 큐에 삽입해둠
for i in range(N):
    for j in range(M) :
        if tomatos[i][j]==1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y=queue.popleft()
        for i in range(4) :
            nx, ny=x+dx[i], y+dy[i] #상하좌우 확인

            if nx < 0 or nx >=N or ny < 0 or ny>=M :
                continue
            if tomatos[nx][ny]==0 :#상하좌우에 안익은 토마토가 있는 경우
                tomatos[nx][ny]=tomatos[x][y]+1 #며칠째에 익었는지
                queue.append((nx, ny))
bfs()
for i in tomatos:
    for j in i :
        if j==0 : #안익은 토마토가 있는 경우
            print(-1)
            exit(0)
    answer=max(answer, max(i)) 
print(answer-1)