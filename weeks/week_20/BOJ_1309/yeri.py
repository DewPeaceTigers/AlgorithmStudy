import sys
input = sys.stdin.readline

n = int(input())

dp=[ [0]*3 for _ in range(n)]
dp[0][0]=1 # 아무것도 선택하지 않음
dp[0][1]=1 # 왼 쪽
dp[0][2]=1 # 오른 쪽
for i in range(1,n):
    dp[i][0]=dp[i-1][0]+dp[i-1][1]+dp[i-1][2]
    dp[i][1]=dp[i-1][0]+dp[i-1][2]
    dp[i][2]=dp[i-1][0]+dp[i-1][1]

print(dp[n-1][0]+dp[n-1][1]+dp[n-1][2])