"""
파이프를 밀 수 있는 방향
- 가로 : →, ↘
- 세로 : ↘, ↓
- 대각선 : →, ↘, ↓
"""

import sys

input = sys.stdin.readline

N = int(input())
state = [list(map(int, input().split())) for _ in range(N)]

# 가로(0), 세로(1), 대각선(2)
dp = [[[0]*3 for j in range(N)] for i in range(N+1)]

dp[1][1][0] = 1

for i in range(1, N+1):
    for j in range(1, N):
        if i==j==1:
            continue

        if state[i-1][j]==1:
            continue

        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2] # 가로
        dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2] # 세로

        if state[i-2][j]==0 and state[i-1][j-1]==0:
            dp[i][j][2] = sum(dp[i-1][j-1])

print(sum(dp[-1][-1]))