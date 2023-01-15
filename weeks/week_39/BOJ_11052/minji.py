import sys

input=sys.stdin.readline

n=int(input())
cards=list(map(int, input().split()))

dp=[0]*(n+1)

for i in range(1, n+1) :
    for k in range(1, i+1) :
        dp[i]=max(dp[i], dp[i-k]+cards[k-1])
print(dp[n])