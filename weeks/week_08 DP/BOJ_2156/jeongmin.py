'''[풀이] 정답 찾아봄..

가능한 3가지 경우 -> 이거를 찾는게 어렵다ㅠ
① 현재 포도주와 이전 포도주를 마시고 전전 포도주는 마시지 않는다. ( wine[i]+wine[i-1]+dp[i-3] )
② 현재 포도주와 전전 포도주를 마시고 이전 포도주는 마시지 않는다. ( wine[i]+dp[i-2] )
③ 현재 포도주를 마시지 않는다. ( dp[i-1] )
'''

import sys
input= sys.stdin.readline

# N 입력(1 ≤ N ≤ 1,000,000)
N = int(input())

wine = [int(input()) for _ in range(N)]

dp = [0]*N

dp[0] = wine[0]

if N>1:
  dp[1] = wine[0]+wine[1]
if N>2:
  dp[2] = max(wine[2]+wine[1], wine[2]+wine[0], dp[1])

for i in range(3, N):
  dp[i] = max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+ wine[i], dp[i-1])  

print(dp[N-1])