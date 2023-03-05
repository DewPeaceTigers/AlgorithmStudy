'''
첫번째 행 : 첫번째 스티커를 뜯은 경우
두번째 행 : 두번째 스티커를 뜯은 경우

현재 위치를 기준으로 두칸 옆과 세칸 옆 스티커 중에 합이 더 커지는 스티커를 뜯어야함
'''
def solution(sticker):
    n = len(sticker)
    dp = [[0] * n for _ in range(2)]

    if n == 1:
        return sticker[0]

    dp[0][0] = sticker[0]
    dp[0][1] = sticker[0]
    dp[1][1] = sticker[1]

    for i in range(2, n - 1):  # 마지막 스티커를 뜯을 수 없음
        dp[0][i] = max(dp[0][i - 2] + sticker[i], dp[0][i - 1])

    for i in range(2, n):
        dp[1][i] = max(dp[1][i - 2] + sticker[i], dp[1][i - 1])

    return max(dp[0][-2], dp[1][-1])