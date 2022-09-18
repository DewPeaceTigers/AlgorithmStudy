'''
첫번째 행과 열을 다 1로 채웠는데 안풀림
-> 첫번째 행과 열에서 웅덩이가 있어서 막히면 그 뒤로는 가는 방법이 없음

'''
def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[n][m]