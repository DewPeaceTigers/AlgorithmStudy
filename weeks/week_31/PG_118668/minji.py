'''
풀이 참고
'''

def solution(alp, cop, problems):
    answer = 0

    max_alp = 0
    max_cop = 0
    for problem in problems:
        max_alp = max(problem[0], max_alp)
        max_cop = max(problem[1], max_cop)

    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    INF = float('inf')
    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_red, cost in problems:
                if i >= alp_req and j >= cop_req:
                    up_alp, up_cop = min(i + alp_rwd, max_alp), min(j + cop_red, max_cop)  # max_alp 넘어가면 index error 발생
                    dp[up_alp][up_cop] = min(dp[up_alp][up_cop], dp[i][j] + cost)

    return dp[-1][-1]