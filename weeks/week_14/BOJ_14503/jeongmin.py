import sys
input= sys.stdin.readline

# 세로 크기 N, 가로 크기 M 입력 (3 ≤ N, M ≤ 50)
N, M = map(int, input().split()) 

# 로봇 청소기가 있는 칸 (r, c), 바라보는 방향 d 입력
x, y, d = map(int, input().split())

place = [list(map(int, input().split())) for _ in range(N)]

# 방향 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

place[x][y]=2
cnt = 1
change = 0

while True:
  # 왼쪽 방향
  d = (d-1)%4
  
  nx = x + dx[d]
  ny = y + dy[d]
  
  # 현재 위치 바로 왼쪽에 빈 공간이 존재한다면
  if place[nx][ny] == 0:
    place[nx][ny]= 2
    cnt += 1
    x, y = nx, ny
    change = 0
    continue
  else:
    change += 1
    
  # 2a 단계가 연속으로 4번 실행된 경우    
  if change == 4:
    # 바로 뒤쪽 확인
    nx = x + dx[(d+2)%4]
    ny = y + dy[(d+2)%4]

    # 바로 뒤쪽이 벽이라면 작동 멈춤
    if place[nx][ny]==1:
      break
    else: # 한칸 후진
      x, y = nx, ny
      change=0

print(cnt)
# for i in range(N):
#   print(*place[i])