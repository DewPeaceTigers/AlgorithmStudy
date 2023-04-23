import sys

input=sys.stdin.readline

n=int(input())

works=[list(map(int, input().split())) for _ in range(n)]

dp=[0]*(n+1)
max_profit=0
for idx, work in enumerate(works) :
    max_profit=max(max_profit, dp[idx])
    if idx+work[0] <= n :
        dp[idx+work[0]]=max(dp[idx+work[0]], max_profit+work[1])
    print(dp)
print(max(dp))