import sys
input = sys.stdin.readline

# 선을 그은 횟수 N(1 ≤ N ≤ 1,000,000) N 입력
N = int(input())

line =[tuple(map(int, input().split())) for _ in range(N)] # 튜플로 해야 시간 초과 안 뜸..
# line =[list(map(int, input().split())) for _ in range(N)] ## 시간 초과 뜸!!!

# 도착점, 출발점 순으로 정렬
line.sort(key=lambda x:[x[0], x[1]])

# 출발점, 도착점 저장
s, e = line[0][0], line[0][1]

# 그려진 선(들)의 총 길이 저장
length = 0

for i in range(N):
  # 시작점이 같은 경우
  if s == line[i][0]:
    e=line[i][1]
  # 시작점 다른 경우
  else:ㄴ
    # e, 시작점 비교
    if e<line[i][0]:
      # 길이 더하고 s, e 대입
      length += e-s
      s, e = line[i][0], line[i][1]
      
    # e>=line[i][0] 이고 e<line[i][1]
    elif e<line[i][1]:
      e = line[i][1]

  # 마지막 차례 길이 더해주기
  if i==N-1:
    length += e-s      

print(length)