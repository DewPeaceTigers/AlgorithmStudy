# 풀이 찾아봄..
# n가지 종류의 동전이 있다. 가치의 합이 k원이 되도록하는 경우의 수

import sys
input= sys.stdin.readline

n, k = map(int, input().split())

# 코인의 종류
c = [int(input()) for _ in range(n)]

# dp[i] : 합이 i원이 되는 경우의 수 
dp = [0] * (k+1) 
# 인덱스 0은 동전을 1개만 쓸 때의 경우의 수를 고려하기 위해 선언
dp[0] = 1

for i in c:
  for j in range(i, k+1):
    if j-i >=0:
      dp[j] += dp[j-i]

print(dp[k])