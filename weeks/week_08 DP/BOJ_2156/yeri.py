# ## 못품 knapsack처럼 풀어봤음..

# import sys
# input = sys.stdin.readline

# n = int(input())
# dp=[[int(input()) for _ in range(n)]]
# for i in range(n-1):
#     dp.append([0]*n)
# isThird=[[False]*n for _ in range(n)]


# for i in range(1,n):
#     # i번째 선택할 와인이 j번째 와인임
#     for j in range(n):
#         if j<i:
#             dp[i][j]=dp[i-1][j]
#             isThird[i][j]=False #isThird[i-1][j]
#             continue
#         max_idx=0
#         max_wine=dp[i-1][0]
#         for t in range(1, j):
#             # j 보다 앞에 있는 것에서만 선택 가능
#             if max_wine < dp[i-1][t]:
#                 max_idx=t
#                 max_wine=dp[i-1][t]
#         if not isThird[i-1][max_idx]:
#             # 현재 번호 더해도 됨
#             dp[i][j]=max_wine+dp[0][j]
#             if j == max_idx+1: # 바로 앞 idx가 선택됐다면 (연속)
#                 isThird[i][j]=True
#         else:
#             # 본인 것은 더하지 못함
#             dp[i][j]=max_wine
#             isThird[i][j]=False
# print(max(dp[n-1][:]))

## 점화식 잘 찾기..
n = int(input())
w = [0]
for i in range(n):
    w.append(int(input()))
dp = [0]
dp.append(w[1])
if n > 1:
    dp.append(w[1] + w[2])
for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))
print(dp[n])