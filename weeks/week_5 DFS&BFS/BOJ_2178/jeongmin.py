import sys
input = sys.stdin.readline

from collections import deque

# N, M(2 ≤ N, M ≤ 100) 입력
N, M = map(int, input().split())

# 미로정보 저장
miro=[]

for _ in range(N):
  miro.append(list(map(int, input().rstrip())))
  
# 상, 하, 좌, 우
dc = [0, 0, -1, 1]
dr = [-1,1, 0, 0]

q = deque()
q.append((0, 0))

def bfs(N, M):
  while q:
    r, c = q.popleft()
    # print(pos)

    for i in range(4):
      nr = r+dr[i]
      nc = c+dc[i]
  
      # 이동할 수 있는 칸 일때
      if 0<=nr<N and 0<=nc<M and miro[nr][nc]!=0:

        if miro[nr][nc] ==1:
          miro[nr][nc]= miro[r][c]+1
          q.append((nr, nc))

bfs(N, M)
print(miro[N-1][M-1])