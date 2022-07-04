"""
LIS : 최장 증가 부분 수열
"""
import sys

input = sys.stdin.readline

N = int(input())
child = [int(input()) for _ in range(N)]

dp = [1]*N
for i in range(N):
    for j in range(i):
        if child[j]<child[i]:
            dp[i] = max(dp[i], dp[j]+1)

answer = max(dp)
print(len(child)-answer)