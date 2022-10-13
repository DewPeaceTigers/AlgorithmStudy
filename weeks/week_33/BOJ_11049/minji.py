'''
pypy3 통과
dp[i][j] -> i부터 j까지 행렬 곱
dp[0][3]
-> dp[0][0]+dp[1][3]
-> dp[0][1]+dp[2][3]
-> dp[0][2]+dp[3][3]

출력은 dp[0][-1]
'''
import sys

INF=sys.maxsize
input=sys.stdin.readline

n=int(input())
matrixs=[list(map(int, input().split())) for _ in range(n)]
dp=[[INF]*n for _ in range(n)]

for i in range(n):
    dp[i][i]=0

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        for k in range(j-i) :
            dp[i][j]=min(dp[i][j], dp[i][i+k]+dp[i+k+1][j]+matrixs[i][0]*matrixs[i+k][1]*matrixs[j][1])

print(dp[0][-1])