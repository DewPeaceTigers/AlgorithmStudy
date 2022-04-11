import sys
input = sys.stdin.readline

from collections import deque

# 보드의 크기 N(2 ≤ N ≤ 100) 입력
N = int(input())

# 사과의 개수 K(0 ≤ K ≤ 100) 입력
K = int(input())

# 사과의 위치 입력
apple = [[False]*N for _ in range(N)]
for _ in range(K):
  r, c = map(int, input().split())
  apple[r-1][c-1] = True

# 뱀의 방향 변환 횟수 L(1 ≤ L ≤ 100) 입력
L = int(input())
dir = deque([list(input().split()) for _ in range(L)])

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 뱀 위치 저장
snake = [[False]*N for _ in range(N)]
snake[0][0] = True

q = deque()
q.append((0, 0)) # 뱀 시작 위치
time = 0 # 경과한 시간(초)
d = 0 # 시작 방향 오른쪽

while q:
  r, c = q[-1]

  # 뱀의 방향 변환 정보 확인
  if dir and int(dir[0][0])== time:
    if dir[0][1]== 'D': # 오른쪽
      d += 1
      if d == 4:
        d = 0
    else: # 왼쪽
      d -= 1
      if d==-1 :
        d = 3
    
    dir.popleft()
    # print(time)

  # 다음칸
  nr = r+ dx[d]
  nc = c+ dy[d]

  time += 1
  # print(nr, nc, time)
  # 벽 또는 자기 자신의 몸과 부딪히는 경우
  if nr>=N or nr<0 or nc>=N or nc<0 or snake[nr][nc]:
    break

  # 다음칸 추가
  q.append((nr, nc))
  snake[nr][nc] = True
  
  # 사과가 있는 경우
  if apple[nr][nc]:
    apple[nr][nc] = False
    continue

  # 꼬리가 위치한 칸 비워줌
  x, y = q.popleft()
  snake[x][y] = False  

print(time)