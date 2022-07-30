# import sys
# input = sys.stdin.readline

# n = int(input())
# open = list(map(int,input().split()))

# k = int(input())
# looks = [ int(input()) for _ in range(k) ]

# dp=[0]*(k+1)
# for i in range(1,k+1):
#     print(open)
#     move1 = dp[i-1] + abs(open[0]-looks[i-1])
#     move2 = dp[i-1] + abs(open[1]-looks[i-1])
#     if move1 < move2:
#         open[0]=looks[i-1]
#         dp[i]=move1
#     else:
#         open[1]=looks[i-1]
#         dp[i]=move2
# print(dp[-1])

dp = [[[-1]*(n+1) for _ in range(n+1)] for _ in range(k)]

# 열려있는 문들 중 몇번째로 열어야 하는 지, 열려있는 문들
def solve(idx, open1, open2):
    if idx == k:
        return 0

    if dp[idx][open1][open2] != -1:
        return dp[idx][open1][open2]

    open1_cnt = solve(idx+1, looks[idx], open2) + abs(looks[idx] - open1)
    open2_cnt = solve(idx+1, open1, looks[idx]) + abs(looks[idx] - open2)

    dp[idx][open1][open2] = min(open1_cnt, open2_cnt)

    return dp[idx][open1][open2]

print(solve(0,open[0],open[1]))