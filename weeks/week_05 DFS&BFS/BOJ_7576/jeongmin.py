import sys
input = sys.stdin.readline

# M, N 입력
M, N = map(int, input().split())

# 토마토 상태 저장
tomato=[]

# 토마토 개수
cnt, t_cnt, day =0, 0, -1

# 익은 토마토 위치
pos = []

# 왼쪽, 오른쪽, 앞, 뒤 네 방향
dr = [[0, -1], [0, 1], [-1, 0], [1, 0]]

for i in range(N):
  t = list(map(int, input().split()))
  for j in range(M):
    if t[j]==0:
      cnt += 1
    elif t[j]==1:
      pos.append([i, j])
      
  tomato.append(t)

# 모든 토마토가 익어있는 상태
if cnt ==len(pos):
  print(0)

else:
  while(pos):
    # 날짜 하루 증가
    day +=1 

    npos=[]
    for p in pos:
      # 네 방향 확인
      for d in dr:
        nr = p[0]+d[0]
        nc = p[1]+d[1]

        if 0<=nr<N and 0<=nc<M and tomato[nr][nc]==0:
          t_cnt+=1
          tomato[nr][nc]=1
          npos.append([nr, nc])

    pos = npos

  # print(tomato)
  # print(t_cnt, day)

  if t_cnt!=cnt:
    print(-1)
  else:
    print(day)