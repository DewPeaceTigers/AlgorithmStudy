from collections import deque

N=int(input())
rgb=[]
for i in range(N):
  rgb.append(list(input().rstrip()))
q=deque()

dx=[0, 0, -1, 1]
dy=[1, -1, 0, 0]
visited=[[False]*N for _ in range(N)]
cnt1, cnt2=0, 0

def bfs(x, y):
    q.append((x, y))
    visited[x][y]=True
    current_color=rgb[x][y]
    while q:
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==False and rgb[nx][ny]==current_color:
                visited[nx][ny]=True
                q.append((nx, ny))


for i in range(N):
  for j in range(N):
    if visited[i][j]==False:
      bfs(i, j)
      cnt1+=1

for i in range(N) :
  for j in range(N) :
    if rgb[i][j]=='G':
      rgb[i][j]='R'

visited=[[False]*N for _ in range(N)]
for i in range(N):
  for j in range(N) :
    if visited[i][j]==False:
      bfs(i, j)
      cnt2+=1

print(cnt1, cnt2)