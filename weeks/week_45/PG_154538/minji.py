from collections import deque


def solution(x, y, n):
    answer = 0
    dp = [float('inf')] * (y + 1)
    q = deque()
    q.append(x)
    dp[x] = 0
    while q:
        now = q.popleft()

        if now == y:
            return dp[y]
        # x에 n을 더하는 경우
        tmp = now + n
        if tmp <= y and dp[tmp] > dp[now] + 1:
            dp[tmp] = dp[now] + 1
            q.append(tmp)

        # x에 2곱하는 경우
        tmp = now * 2
        if tmp <= y and dp[tmp] > dp[now] + 1:
            dp[tmp] = dp[now] + 1
            q.append(tmp)

        # x에 3 곱하는 경우
        tmp = now * 3
        if tmp <= y and dp[tmp] > dp[now] + 1:
            dp[tmp] = dp[now] + 1
            q.append(tmp)

    return -1