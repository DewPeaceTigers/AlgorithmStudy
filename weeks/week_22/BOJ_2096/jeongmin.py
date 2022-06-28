"""
메모리 초과..
이 문제를 제대로 풀기 위해서는 '한 줄만 읽기 -> 계산하기 -> 방금 읽은 데이터 버리기' 를 반복해야 한다!
"""

import sys
input = sys.stdin.readline

N = int(input())

# 최소, 최대
dp = [[0]*2 for j in range(N)]

for i in range(N):
    line = list(map(int, input().split()))

    # 첫 줄 초기화
    if i == 0:
        dp = [[line[i]]*2 for i in range(3)]

    # 두번째 줄~ 마지막 줄
    else:
        min1 = min(dp[0][0], dp[1][0])
        min2 = min(dp[1][0], dp[2][0])

        max1 = max(dp[0][1], dp[1][1])
        max2 = max(dp[1][1], dp[2][1])

        dp[0][0] = min1 + line[0]
        dp[0][1] = max1 + line[0]

        dp[1][0] = min(min1, min2) + line[1]
        dp[1][1] = max(max1, max2) + line[1]

        dp[2][0] = min2 + line[2]
        dp[2][1] = max2 + line[2]

n = sum(dp, [])
print(max(n), min(n))