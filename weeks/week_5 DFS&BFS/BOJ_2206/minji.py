'''
못품
visited[x][y][w] w가 0이면 벽을 부숨 1이면 아직 벽을 안부숨
'''
from collections import deque
N, M=map(int, input().split())
matrix=[]
for i in range(N) :
  matrix.append(list(map(int, list(input().strip()))))

#상하좌우
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def bfs() :
  q=deque()
  q.append((0, 0, 1)) #3번째 원소는 벽을 부섰는지 아닌지
  visited=[[[0]*2 for i in range(M)] for i in range(N)]
  visited[0][0][1]=1 #(0, 0)에서 시작
  while q:
    x, y, z = q.popleft()
    if x==N-1 and y==M-1 : #x, y가 (N, M)이 되면 종료
      return visited[x][y][z]
    for i in range(4) : #상하좌우 이동
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<N and 0<=ny<M : #범위 안에 있으면
        if matrix[nx][ny]==1 and z==1 : #벽이 있고 아직 벽을 부수지 않았다면
          visited[nx][ny][0]=visited[x][y][1] +1 #벽을 부수고 감
          q.append((nx, ny, 0))
        elif matrix[nx][ny]==0 and visited[nx][ny][z]==0 : #벽을 이미 부순 상태 벽이 없고 방문을 안한경우
          visited[nx][ny][z] = visited[x][y][z]+1
          q.append((nx, ny, z))
  return -1

print(bfs())