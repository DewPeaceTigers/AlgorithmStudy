import sys
input = sys.stdin.readline

N = int(input())
matrixs = [ list(map(int,input().split())) for _ in range(N)]
dp = [ [0]*N  for _ in range(N)]

for d in range(1,N):
    # 차이
    for i in range(N-d):
        j = i+d # 현 대각선에서 몇번째 원소인지
        if d == 1:
            dp[i][j] = matrixs[i][0] * matrixs[j][0] * matrixs[j][1]
            continue
        dp[i][j] = int(1e9)
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+matrixs[i][0]*matrixs[k][1]*matrixs[j][1])
for d in dp : print(d)
print(dp[0][N-1])