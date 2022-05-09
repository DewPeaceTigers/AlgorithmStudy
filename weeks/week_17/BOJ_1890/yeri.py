import sys
input = sys.stdin.readline
n = int(input())
boxes = [list(map(int,input().split())) for _ in range(n)]

dp=[[0]*n for _ in range(n)]
dp[0][0]=1
for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1 : break
        for d in range(2):
            nx = i + (boxes[i][j] if d==0 else 0)
            ny = j + (boxes[i][j] if d==1 else 0)
            if not(-1<nx<n and -1<ny<n): continue
            dp[nx][ny]+=dp[i][j]

print(dp[n-1][n-1])

# 현재 위치까지 올 수 있는 경우의 수