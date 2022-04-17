# DP를 사용한 풀이!
# 정답 찾아봄..
import sys
input = sys.stdin.readline

# 퇴사 DP 
n = int(input())
T, P = [0 for i in range(n+1)], [0 for i in range(n+1)]
for i in range(n):
    a,b = map(int, input().split())
    T[i] = a
    P[i] = b

# dp[i]는 i번째날까지 일을 했을 때, 최대값이다. 
dp =[0 for i in range(n+1)]

for i in range(len(T)-2, -1, -1):      # 역순으로 진행
    if T[i]+i <= n:       # 날짜를 초과하지 않을 경우.
        dp[i] = max(P[i] + dp[i + T[i]], dp[i+1])   
    else:                 # 날짜를 초과할 경우.
        dp[i] = dp[i+1]
print(dp[0])


""" 
# ‘첫번째 날 + 기간’ 이후부터는 첫번째 날을 포함하는 것이 더 큰 값이기 때문에, 
# for문을 1 ~ ‘첫번째날 + T1’까지 돌리면서 dfs를 수행하였다. 
# 첫번째 날을 선택하였다고 가정할 때, 그 다음 순서로 ‘첫번째날 + T1’~ ‘N번째 날’까지 가능한 모든 경우를 확인한다.

import sys
input = sys.stdin.readline

ans = 0

def dfs(idx, consulting, sum, N):
  global ans
  
  if idx > N:
    ans = max(ans, sum)
    return

  p, t = consulting[idx]
  sum += p

  for i in range(idx, min(idx+t+1, N+1)):
    dfs(i+t, consulting, sum, N)   

  
# 남은 일수 N (1 ≤ N ≤ 15) 입력
N = int(input())

# 걸리는 기간 Ti, 받을 수 있는 금액 Pi 입력 (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)
consulting = [[0, 0] for i in range(N+1)]

for i in range(1, N+1):
  t, p = map(int, input().split())
  if i+t>N+1:
		# 기간이 초과되는 경우의 금액은 0으로 설정함
    p = 0
  # 금액, 기간, 며칠
  consulting[i] = [p, t]

for i in range(1, 1+ consulting[1][1]):
  # print(i, 1+consulting[1][1])
  dfs(i, consulting, 0, N)

print(ans)

"""