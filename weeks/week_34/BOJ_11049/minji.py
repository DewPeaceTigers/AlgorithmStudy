'''
대각선으로 dp 채워나가야함...왜???
'''
import sys
n=int(input())

matrixs=[list(map(int, input().split())) for _ in range(n)]

INF=sys.maxsize
dp=[[INF]*n for _ in range(n)]
for i in range(n):
    dp[i][i]=0
