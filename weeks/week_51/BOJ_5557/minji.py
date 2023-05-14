import sys

input=sys.stdin.readline

n=int(input())
nums=list(map(int, input().split()))

dp=[[0]*21 for _ in range(n-1)] #dp[i][j] i번째까지 j를 만들 수 있는 수

dp[0][nums[0]]=1
for i in range(1, n-1) :
    for j in range(21) :
        if dp[i-1][j] > 0:
            if j+nums[i]<=20 :
                dp[i][j+nums[i]]+=dp[i-1][j]
            if j-nums[i]>=0 :
                dp[i][j-nums[i]]+=dp[i-1][j]

print(dp[-1][nums[-1]])