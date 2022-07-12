"""
N = int(input())  # 아이들의 수
people = [int(input()) for _ in range(N)]  # 아이들 번호 순서 정보

# 2차원 dp
dp = [[0] * N for _ in range(N)]

# 가장 긴 증가하는 부분수열
for i in range(N):
    dp[i][i] = 1  # i를 시작점으로 설정.
    for j in range(i + 1, N):
        for k in range(j):
            if people[k] < people[j]:
                dp[i][j] = max(dp[i][j], dp[i][k] + 1)

# 가장 긴 증가하는 수열 길이 계산
lis = 0
for i in range(N):
    lis = max(lis, max(dp[i]))

# 전체 길이 - 가장 긴 증가하는 부분수열
answer = N - lis
print(answer)

# https://jjangsungwon.tistory.com/47
"""
