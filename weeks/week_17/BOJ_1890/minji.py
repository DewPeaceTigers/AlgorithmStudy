import sys

input=sys.stdin.readline

n=int(input())
boards=[]
dp=[[0]*n for _ in range(n)]
dp[0][0]=1

for _ in range(n) :
    boards.append(list(map(int, input().split())))

for i in range(n) :
    for j in range(n) :
        if i==n-1 or j==n-1 :
            break
        down=boards[i][j]+i
        right=boards[i][j]+j

        if down < n :
            dp[down][j]+=dp[i][j]
        if right<n:
            dp[i][right]+=dp[i][j]

print(dp[n-1][n-1])