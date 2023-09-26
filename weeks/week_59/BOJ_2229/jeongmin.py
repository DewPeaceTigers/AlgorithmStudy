# 풀이 찾아봄! https://blog.naver.com/PostView.nhn?blogId=occidere&logNo=221535723529
# 다이나믹 프로그래밍을 활용하는 문제
# dp[i] : i번째까지 적당히 그룹핑 했을 때의 최댓값

"""
k 번째 점수를 입력받았으면

k 번째 점수 혼자 그룹  +  k - 1 번째 까지 적당히 그룹핑 했을 때의 최대값
k - 1 번째 점수 그룹  +  k - 2 번째 까지 적당히 그룹핑 했을 때의 최대값
.....
k - (k-2) 번째 점수 그룹  +  1번째 점수 혼자 그룹핑 했을 때의 최대값

순서대로 계산을 하며 갱신해나가면 된다
"""

import sys

input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))

dp = [0]*N

for k in range(N):

    result = 0
    for x in range(k, -1, -1):
        # M-m : x~k 구간에서 최고점수, 최하점수 차이
        M, m = max(scores[x:k+1]), min(scores[x:k+1])
        # dp[x-1] : 0~x-1까지 적당히 그룹핑 했을 때의 최대값
        result = max(result, M-m+dp[x-1])
    dp[k] = result

print(dp[N-1])
