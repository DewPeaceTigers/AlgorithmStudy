'''[풀이]
stairs 2차원 리스트를 사용한다.
- stairs[N][n] : 길이가 N이고 끝 숫자가 n인 계단 수의 개수 저장
- N: 계단수, n: 숫자(0~9)

정답 : (stairs[N]의 합) % 1,000,000,000
'''

import sys
input= sys.stdin.readline

# N 입력(1 ≤ N ≤ 100)
N = int(input())

ans =0

# stairs[계단수][숫자]
stairs= [[0]*10 for _ in range(N+1)]

# N이 1인 경우 초기화
for i in range(1, 10):
  stairs[1][i]+=1

for i in range(1, N):
  for j, s in enumerate(stairs[i]):
    if j>0:
      # 다음 숫자로 1 큰 숫자 (경우의 수만큼 더하기)
      stairs[i+1][j-1]+= s
    if j<9:
      # 다음 숫자로 1 작은 숫자 (경우의 수만큼 더하기)
      stairs[i+1][j+1]+= s

ans = sum(stairs[N])%1000000000

print(ans)