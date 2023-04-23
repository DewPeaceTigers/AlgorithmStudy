import sys
input = sys.stdin.readline

N = int(input())
T = []
P = []

for _ in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)
T.append(0)
P.append(0)
dp = [0]*(N+1)

for i in range(N-1,-1,-1):
    if i+T[i] <= N:
        # ㄱㅏ능하다면
        dp[i] = max(dp[i+1],P[i]+dp[i+T[i]])
    else:
        dp[i] = dp[i+1]
print(dp[0])