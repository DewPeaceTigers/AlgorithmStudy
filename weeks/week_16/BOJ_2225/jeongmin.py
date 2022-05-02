N, K = map(int, input().split())

# 합이 i가 되는 경우의 수 저장
dp = [1] * (N+1)

# i : 사용하는 정수 개수
for i in range(1, K):
    # 그 합이 j가 되는 경우
    for j in range(1, N+1):
        # dp[j] = sum(dp[0:j+1]) % 1000000000
        dp[j] = (dp[j-1] + dp[j]) % 1000000000
    # print(dp)
print(dp[N])