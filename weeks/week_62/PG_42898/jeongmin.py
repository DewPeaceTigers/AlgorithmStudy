# 물의 잠긴 지역이 (행, 열) 순이 아니라 (열, 행)으로 주어짐 -> 이것때문에 계속 런타임 에러,,

def solution(m, n, puddles):
    answer = 0

    # dp[i][j]: (i, j) 위치까지의 최단 경로 개수
    dp = [[0]*m for _ in range(n)]

    # 물에 잠긴 지역 표시
    puddle = [[False]*m for _ in range(n)]
    for c, r in puddles:
        puddle[r-1][c-1] = True

    # 가장자리
    for i in range(n):
        if puddle[i][0]:
            break
        dp[i][0] = 1

    for i in range(m):
        if puddle[0][i]:
            break
        dp[0][i] = 1

    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    for i in range(1, n):
        for j in range(1, m):
            # 물에 잠긴 지역이라면 무시
            if puddle[i][j]:
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    answer = (dp[n-1][m-1]) % 1000000007

    return answer
