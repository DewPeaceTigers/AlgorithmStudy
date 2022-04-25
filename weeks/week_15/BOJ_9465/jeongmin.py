# 두 변을 공유하지 않는 스티커 점수의 최댓값

import sys
input= sys.stdin.readline

# 테스트 케스 T 입력
T = int(input())

for _ in range(T):
  # n (1 ≤ n ≤ 100,000) 입력
  n = int(input())
  
  sticker = [list(map(int, input().split())) for _ in range(2)]

  # 최댓값 (열 기준)
  dp = [0]*n

  unselect = [0]*n

  for i in range(1, n):
    # 선택 안함
    unselect[i] = max(sticker[0][i-1], sticker[1][i-1])
    
    # 첫째 줄 선택
    sticker[0][i] = max(unselect[i-1]+sticker[0][i], sticker[1][i-1]+ sticker[0][i])
    
    # 둘째 줄 선택
    sticker[1][i] = max(unselect[i-1] + sticker[1][i], sticker[0][i-1]+sticker[1][i])

  print(max(sticker[0][n-1], sticker[1][n-1]))