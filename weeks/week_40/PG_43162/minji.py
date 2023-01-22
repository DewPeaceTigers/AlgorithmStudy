def solution(n, computers):
    ans = 0
    visit = [0] * n

    def dfs(start):
        visit[start] = 1

        for idx in range(n):
            if idx != start and computers[start][idx] == 1 and visit[idx] == 0:
                dfs(idx)

    for i in range(n):
        if visit[i] == 0:
            dfs(i)
            ans += 1
    return ans
