import sys 

input = sys.stdin.readline 

N = int(input())

# Ti : 상담을 완료하는데 걸리는 기간
# Pi : 상담을 했을 때 받을 수 있는 금액
# cosult[i] = [Ti, Pi] 
consult = [list(map(int, input().split())) for _ in range(N)]

# dp[i] : i일까지 얻을 수 있는 최대 수익
dp = [0] * (N+1) # (N+1)일째 되는 날 퇴사
for i in range(N):
    t, p = consult[i]
    # print(t, p)
    if i + t < N + 1 :
        # 상담 진행
        dp[i+t] = max(dp[i+t], dp[i]+p)
    if i < N: 
        # 상담 진행 X
        dp[i+1] = max(dp[i+1], dp[i])

# print(dp)
print(max(dp))