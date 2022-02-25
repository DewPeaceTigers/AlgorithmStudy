import sys
input= sys.stdin.readline

# N, K 입력 (1 ≤ N ≤1,000,000, 1 ≤ K ≤ 1,000,000,000)
N, K = map(int, input().split())

# 각 캐릭터의 레벨 입력 (1 ≤ Xi ≤ 1,000,000,000)
X = [int(input()) for _ in range(N)]

X.sort()

# 가능한 최대 팀 목표레벨 T 저장
T = 0

start, end = X[0], X[0]+K
while start<=end:
  level = 0
  mid = (start+end)//2

  # 목표레벨과 각 캐릭터 레벨 차이의 합 구하기 
  for x in X:
    if x<mid: 
      level += mid-x

  # 레벨 차이 합 < K
  if level <= K:
    T = mid # 팀 목표레벨 갱신
    start = mid+1
  else:
    end = mid-1

print(T)